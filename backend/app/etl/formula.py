"""A small, safe evaluator for the adequacy aid formulas: numbers, names, + - * /, comparisons (1 or 0),
min, max and clamp. Nothing else is allowed, so a formula in the config can't run code."""
import ast
import operator

_BINARY = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}
_COMPARE = {ast.Lt: operator.lt, ast.LtE: operator.le, ast.Gt: operator.gt, ast.GtE: operator.ge, ast.Eq: operator.eq}
_FUNCTIONS = {"min": min, "max": max, "clamp": lambda x, low, high: max(low, min(high, x))}


def names(formula: str) -> set:
    """The component and parameter codes a formula uses."""
    return {node.id for node in ast.walk(ast.parse(formula, mode="eval"))
            if isinstance(node, ast.Name) and node.id not in _FUNCTIONS}


def evaluate(formula: str, values: dict) -> float:
    def walk(node):
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return float(node.value)
        if isinstance(node, ast.Name):
            if node.id not in values:
                raise KeyError(f"{node.id} isn't a component or parameter of this year")
            return float(values[node.id])
        if isinstance(node, ast.BinOp) and type(node.op) in _BINARY:
            return _BINARY[type(node.op)](walk(node.left), walk(node.right))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            return -walk(node.operand) if isinstance(node.op, ast.USub) else walk(node.operand)
        if isinstance(node, ast.Compare) and len(node.ops) == 1 and type(node.ops[0]) in _COMPARE:
            return 1.0 if _COMPARE[type(node.ops[0])](walk(node.left), walk(node.comparators[0])) else 0.0
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in _FUNCTIONS and not node.keywords:
            return float(_FUNCTIONS[node.func.id](*(walk(arg) for arg in node.args)))
        raise ValueError(f"Not allowed in a formula: {ast.dump(node)[:80]}")
    return walk(ast.parse(formula, mode="eval"))
