"""Convert Markdown presentation to PPTX.

Usage:
    python md2pptx.py input.md [output.pptx]

Parses slides in the format:
    ## Slide N. Title
    ```slide
    +-- ASCII art box --+
    | content           |
    +-------------------+
    ```
    __Comment:__ Speaker notes

Requires: python-pptx (pip install python-pptx)
"""

import re
import sys
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.enum.text import PP_ALIGN
except ImportError:
    print("Error: python-pptx is required. Install with: pip install python-pptx")
    sys.exit(1)


def parse_markdown(filepath):
    text = Path(filepath).read_text(encoding="utf-8")
    slides = []
    # Match each slide block: ## Slide N. Title ... ```slide ... ``` ... __Comment:__ ...
    pattern = re.compile(
        r"^##\s+Slide\s+(?P<number>[\d]+)\.\s+(?P<title>.+?)$\s*"
        r"```slide(?P<type>:\w+)?\s*\n(?P<slide_content>.*?)```\s*"
        r"(?P<comment>__Comment:__\s*(.*?))?(?=\n##\s+Slide|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    for match in pattern.finditer(text):
        slide_type = match.group("type")
        if slide_type:
            slide_type = slide_type[1:]  # Remove leading colon
        
        content = match.group("slide_content").strip()
        # Validate height: 15 lines
        if len(content.splitlines()) != 15:
            print(f"Warning: Slide {match.group('number')} has {len(content.splitlines())} lines instead of 15.")
        
        slides.append(
            {
                "number": match.group("number"),
                "title": match.group("title").strip(),
                "slide_content": content,
                "comment": match.group("comment").strip() if match.group("comment") else "",
                "type": slide_type if slide_type else "content",
            }
        )
    return slides


def extract_text_from_ascii_box(ascii_content):
    lines = ascii_content.splitlines()
    text_lines = []
    for line in lines:
        # Remove ASCII borders: +---+ borders and | vertical bars
        stripped = line.strip()
        if stripped.startswith("+") and stripped.endswith("+"):
            continue
        # Remove leading/trailing | and trim
        if "|" in stripped:
            parts = stripped.split("|")
            inner = "|".join(parts[1:-1])
        else:
            inner = stripped
        
        # Handle alignment
        text = inner.strip()
        alignment = PP_ALIGN.CENTER
        if text.startswith(":"):
            alignment = PP_ALIGN.LEFT
            text = text[1:].strip()
        elif text.endswith(":"):
            alignment = PP_ALIGN.RIGHT
            text = text[:-1].strip()
            
        if text:
            text_lines.append((text, alignment))
    return text_lines


def add_slide(prs, slide_data):
    slide_layout = prs.slide_layouts[6]  # blank layout
    slide = prs.slides.add_slide(slide_layout)

    # --- Title ---
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = slide_data["title"]
    p.font.size = Pt(28)
    p.font.bold = True

    # --- Content from ASCII box ---
    content_lines = extract_text_from_ascii_box(slide_data["slide_content"])
    content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.1), Inches(9), Inches(5.5))
    tf = content_box.text_frame
    tf.word_wrap = True

    for i, (text, alignment) in enumerate(content_lines):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = text
        p.alignment = alignment
        p.font.size = Pt(18)
        p.space_after = Pt(6)

    # --- Speaker notes ---
    comment_text = slide_data["comment"]
    if comment_text:
        comment_text = re.sub(r"^__Comment:__\s*", "", comment_text).strip()
        notes_slide = slide.notes_slide
        notes_tf = notes_slide.notes_text_frame
        notes_tf.text = comment_text


def convert(md_path, pptx_path):
    slides = parse_markdown(md_path)
    if not slides:
        print(f"No slides found in {md_path}")
        sys.exit(1)

    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    for s in slides:
        add_slide(prs, s)

    prs.save(pptx_path)
    print(f"Converted {len(slides)} slides -> {pptx_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print(f"File not found: {md_path}")
        sys.exit(1)

    pptx_path = Path(sys.argv[2]) if len(sys.argv) > 2 else md_path.with_suffix(".pptx")
    convert(md_path, pptx_path)
