"""Convert PPTX to Markdown presentation.

Usage:
    python pptx2md.py input.pptx [output.md]

Extracts slide titles, content text, and speaker notes, then formats them
into the skill's Markdown format with ASCII art boxes.

Requires: python-pptx (pip install python-pptx)
"""

import re
import sys
from pathlib import Path

try:
    from pptx import Presentation
except ImportError:
    print("Error: python-pptx is required. Install with: pip install python-pptx")
    sys.exit(1)


BOX_WIDTH = 66


def extract_slide_text(slide):
    texts = []
    for shape in slide.shapes:
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                t = para.text.strip()
                if t:
                    texts.append(t)
    return texts


def get_speaker_notes(slide):
    try:
        notes_slide = slide.notes_slide
        return notes_slide.notes_text_frame.text.strip()
    except Exception:
        return ""


def guess_title(texts):
    if not texts:
        return "Untitled"
    # First non-empty line that looks like a title (short, no leading dash/bullet)
    for t in texts:
        if len(t) < 120 and not t.startswith("-") and not t.startswith("•"):
            return t
    return texts[0]


def make_ascii_box(lines):
    top = "+" + "-" * (BOX_WIDTH - 2) + "+"
    bottom = top
    result = [top]
    
    # Ensure exactly 13 lines of content (15 total - 2 borders)
    # In a real implementation, we'd split the content into header and body
    # For now, we pad with empty lines to reach the fixed height
    for i in range(13):
        if i < len(lines):
            line = lines[i][:BOX_WIDTH - 4]
            result.append("| " + line.ljust(BOX_WIDTH - 4) + " |")
        else:
            result.append("| " + " " * (BOX_WIDTH - 4) + " |")
            
    result.append(bottom)
    return "\n".join(result)


def wrap_text(text, width=BOX_WIDTH - 4):
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= width:
            current = (current + " " + w).strip()
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines if lines else [text]


def convert(pptx_path, md_path):
    prs = Presentation(pptx_path)
    slides = prs.slides
    md_lines = []
    slide_num = 0

    for slide in slides:
        texts = extract_slide_text(slide)
        notes = get_speaker_notes(slide)

        if not texts:
            continue

        title = guess_title(texts)
        # Remove the title from content to avoid duplication
        body_texts = [t for t in texts if t != title]

        # Flatten and wrap body text
        all_body = " ".join(body_texts)
        wrapped_lines = wrap_text(all_body)

        slide_num += 1
        md_lines.append(f"## Slide {slide_num}. {title}")
        md_lines.append("")
        md_lines.append("```slide")
        md_lines.append(make_ascii_box(wrapped_lines))
        md_lines.append("```")
        if notes:
            md_lines.append("")
            md_lines.append(f"__Comment:__ {notes}")
        md_lines.append("")

    content = "\n".join(md_lines)
    md_path.write_text(content, encoding="utf-8")
    print(f"Converted {slide_num} slides -> {md_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    pptx_path = Path(sys.argv[1])
    if not pptx_path.exists():
        print(f"File not found: {pptx_path}")
        sys.exit(1)

    md_path = Path(sys.argv[2]) if len(sys.argv) > 2 else pptx_path.with_suffix(".md")
    convert(pptx_path, md_path)
