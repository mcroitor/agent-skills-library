---
name: ocr-specialist
description: Extract and normalize text from images and scanned documents. Use for OCR pipeline setup, multilingual recognition, layout-aware extraction, quality validation, and post-processing to structured outputs.
---

# OCR Specialist

## Description
A skill for extracting, cleaning, and structuring text from images, PDFs, and scanned documents with a focus on accuracy, layout preservation, and reliable downstream use.

## Priority Rules
Prioritize in this order when trade-offs conflict; if two priorities overlap, prefer the higher item:
1. Text extraction accuracy and semantic fidelity
2. Data privacy and secure handling of source files
3. Layout and structure preservation
4. Throughput and processing speed

## When to Use
- Digitizing scanned documents and printed materials
- Extracting text from photos, screenshots, and PDFs
- Building OCR workflows for multilingual datasets
- Converting unstructured scans into searchable text
- Preparing OCR outputs for translation, analysis, or indexing

## Instructions
1. **Identify input profile** - determine file types, languages, scan quality, and expected output format
2. **Preprocess sources** - deskew, denoise, enhance contrast, and segment relevant regions
3. **Run OCR extraction** - choose OCR engine and language packs, then process pages or batches
4. **Post-process text** - normalize whitespace, fix common OCR artifacts, and recover paragraph structure
5. **Preserve structure** - capture layout elements such as headings, tables, and lists when required
6. **Validate quality** - spot-check low-confidence regions and compute quality metrics
7. **Export results** - produce target format (TXT, Markdown, JSON, CSV, searchable PDF)
8. **Document assumptions** - record model/engine settings, language choices, and known limitations

## Input Recovery Rules
- Assume mixed-quality scanned documents when source quality is not specified
- Assume UTF-8 text output and one output file per source unless requested otherwise
- Ask for clarification only when language set, required structure fidelity, or target format materially affects extraction strategy

## Constraints
- Do not claim perfect recognition quality; report uncertainty and low-confidence regions
- Do not discard non-text elements without explicit instruction when structure matters
- Do not process sensitive documents without privacy and retention requirements

## Deliverables
- Extracted text with normalized formatting
- Structured output variant (Markdown/JSON/CSV) when needed
- OCR quality summary with confidence notes and unresolved regions
- Processing configuration summary for reproducibility

## Tools and Practices
- OCR engines: Tesseract, EasyOCR, PaddleOCR, cloud OCR APIs
- Preprocessing: OpenCV-based denoise, thresholding, orientation correction
- Document parsing: PDF text-layer detection, page zoning, table extraction
- Validation: confidence thresholding, human-in-the-loop review for critical fields

## Output Contract
Return all of the following:
1. Short extraction summary (source type, languages, page count)
2. Extracted content in requested format
3. Quality notes (confidence, suspected errors, missing regions)
4. Assumptions, settings, and next-step recommendations
