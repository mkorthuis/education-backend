// Text from a scanned PDF with macOS's Vision framework, for extract_education_freedom_account_expenditures.py: each page
// rendered at OCR_SCALE (default 3), its recognized text grouped into rows by position, a row's pieces
// joined left to right with tabs. Pages scanned upside down are read the right way up.
//
//     swiftc -O -o efa_ocr efa_ocr.swift
//     OCR_SCALE=3 ./efa_ocr report.pdf reading1.txt && OCR_SCALE=4.5 ./efa_ocr report.pdf reading2.txt
import Foundation
import PDFKit
import Vision

typealias Piece = (y: CGFloat, x: CGFloat, h: CGFloat, text: String)

let args = CommandLine.arguments
guard args.count == 3, let document = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    FileHandle.standardError.write("usage: efa_ocr <in.pdf> <out.txt>\n".data(using: .utf8)!); exit(1)
}
let scale = CGFloat(Double(ProcessInfo.processInfo.environment["OCR_SCALE"] ?? "3")!)
let amount = try! NSRegularExpression(pattern: "\\d\\.\\d\\d")

var output = ""
for index in 0..<document.pageCount {
    guard let page = document.page(at: index) else { continue }
    let bounds = page.bounds(for: .mediaBox)
    let image = page.thumbnail(of: CGSize(width: bounds.width * scale, height: bounds.height * scale), for: .mediaBox)
    guard let tiff = image.tiffRepresentation, let bitmap = NSBitmapImageRep(data: tiff), let cgImage = bitmap.cgImage else { continue }

    func read(_ orientation: CGImagePropertyOrientation) throws -> [Piece] {
        let request = VNRecognizeTextRequest()
        request.recognitionLevel = .accurate
        request.usesLanguageCorrection = false
        try VNImageRequestHandler(cgImage: cgImage, orientation: orientation, options: [:]).perform([request])
        return (request.results ?? []).compactMap { observation in
            guard let text = observation.topCandidates(1).first?.string else { return nil }
            let box = observation.boundingBox
            // A reading of the page turned over comes back in the unturned page's coordinates: mirror both
            return orientation == .down ? (box.midY, 1 - box.maxX, box.height, text) : (1 - box.midY, box.minX, box.height, text)
        }
    }
    func amounts(_ pieces: [Piece]) -> Int {
        pieces.filter { amount.firstMatch(in: $0.text, range: NSRange($0.text.startIndex..., in: $0.text)) != nil }.count
    }
    let upright = try read(.up)
    let flipped = amounts(upright) < 5 || upright.contains(where: { $0.text.contains("SZOZ") || $0.text.contains("%00") }) ? try read(.down) : []
    let pieces = amounts(flipped) > amounts(upright) ? flipped : upright

    // Rows: pieces whose vertical centres are within half a line of each other
    var rows: [[Piece]] = []
    for piece in pieces.sorted(by: { $0.y < $1.y }) {
        if let last = rows.last, let first = last.first, abs(first.y - piece.y) < max(first.h, piece.h) * 0.5 {
            rows[rows.count - 1].append(piece)
        } else {
            rows.append([piece])
        }
    }
    output += "=== page \(index + 1)\n"
    for row in rows {
        output += row.sorted(by: { $0.x < $1.x }).map { $0.text }.joined(separator: "\t") + "\n"
    }
}
try output.write(toFile: args[2], atomically: true, encoding: .utf8)
print("\(args[1]): \(document.pageCount) pages")
