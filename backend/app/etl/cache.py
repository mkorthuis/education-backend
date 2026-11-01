"""
On-disk cache of parsed source files, so rebuilds skip re-reading unchanged workbooks.

Each entry is keyed by the SHA-256 of the source file's contents plus a caller-supplied key
(the parsing code, its config, library versions and any arguments). Changing the file, the
parser or the config therefore misses the cache instead of returning stale results.

The cache lives in backend/.etl_cache (git-ignored). Set ETL_CACHE_DIR to move it, or to an
empty value to turn caching off. Deleting the folder is always safe.
"""
import hashlib
import json
import os
from typing import Callable

_DEFAULT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".etl_cache"))
CACHE_DIR = os.environ.get("ETL_CACHE_DIR", _DEFAULT_DIR)


def fingerprint(*parts) -> str:
    """A stable hash of the given values (code, config text, versions, arguments)."""
    digest = hashlib.sha256()
    for part in parts:
        digest.update(part if isinstance(part, bytes) else str(part).encode())
        digest.update(b"\0")
    return digest.hexdigest()


def file_fingerprint(path: str) -> str:
    """The SHA-256 of a file's contents."""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def cached(namespace: str, path: str, key: str, compute: Callable[[], object]):
    """
    The cached result of compute() for this file and key, computing and storing it on a miss.

    The result must be JSON-serializable; tuples come back as lists.
    """
    if not CACHE_DIR:
        return compute()
    entry_key = fingerprint(file_fingerprint(path), key)
    entry = os.path.join(CACHE_DIR, namespace, entry_key[:2], f"{entry_key}.json")
    if os.path.exists(entry):
        with open(entry) as f:
            return json.load(f)

    result = compute()
    os.makedirs(os.path.dirname(entry), exist_ok=True)
    # Write to a temporary file first so an interrupted run never leaves a partial entry
    temporary = f"{entry}.{os.getpid()}.tmp"
    with open(temporary, "w") as f:
        json.dump(result, f)
    os.replace(temporary, entry)
    return result
