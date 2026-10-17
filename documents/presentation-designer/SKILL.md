---
name: presentation-designer
description: Helps to create a Markdown presentation from a scientific paper or lesson. Can convert Markdown presentation to PPTX and PPTX to Markdown. Supports speaker notes, slide templates (title, section, content, two-columns), and three visual styles (academic, dark, minimal).
compatibility: Python 3.8+ with python-pptx (pip install python-pptx)
metadata:
  author: Mihail Croitor
  version: "1.3"
---

# Presentation Designer

## Description

Designs structured slide decks from dense source material (papers, lessons) using fixed 66x15 ASCII-art layouts. Every slide pairs a minimal on-slide visual with a detailed `__Comment:__` speaker narrative that can be rendered to PPTX and back.

## When to Use

- Converting a scientific paper, thesis, or technical report into a presentation.
- Designing a lecture or lesson plan for educational purposes.
- Creating a structured outline for a presentation before moving it to a tool like PowerPoint.
- Standardizing the visual layout of slides across different presentations using predefined ASCII templates.
- Round-tripping between Markdown and PPTX (either direction) for delivery, editing, or version control.

## Instructions

1. **Analyze Source Material** - Extract key arguments, findings, and structure from the input document (paper, lesson, etc.).
2. **Define Presentation Outline** - Create a logical sequence of slides (e.g., Introduction -> Problem -> Methodology -> Results -> Conclusion). The logical flow must be between title slide, that contains presentation name, author's name, affiliation; subsequent slides should follow the narrative structure of the content. The last slide should be the section slide with the text "Thank You" and "Questions?".
3. **Select Slide Templates** - For each slide in the outline, choose the most appropriate template from `templates/`:
    - `title.md` for the opening slide.
    - `section.md` for transition slides between major parts.
    - `content.md` for standard bullet points.
    - `two-columns.md` for comparisons or side-by-side information.
4. **Populate Slide Content** - Fill the ASCII boxes with concise, high-impact text. Avoid overcrowding slides; use keywords and short phrases.
5. **Draft Speaker Comments** - Write detailed explanations under each slide using the `__Comment:__` syntax. These comments should contain the narrative that the presenter will actually speak.
6. **Review and Refine** - Ensure a smooth transition between slides and that the visual balance of the ASCII boxes is maintained.
7. **Convert Markdown to PPTX** - Run `python scripts/md2pptx.py presentation.md [output.pptx] [--style NAME]` to generate a PowerPoint file. The `--style` flag selects a visual theme (`academic` by default, or `dark` / `minimal` — see [Presentation Styles](#presentation-styles)).
8. **Convert PPTX to Markdown** - Run `python scripts/pptx2md.py presentation.pptx` to extract slides into Markdown. Review and manually restore ASCII layout and comments if needed.

## Tools and Practices

- **ASCII Slide Layouts**: Using fixed-width text boxes to represent slide visuals directly in Markdown.
- **Template-Based Design**: Leveraging predefined templates to ensure consistency in layout.
- **Separation of Concerns**: Keeping "on-slide" content minimal and "spoken" content detailed in comments.
- **Python Conversion Scripts**: Using `scripts/md2pptx.py` and `scripts/pptx2md.py` for bidirectional conversion between `.md` and `.pptx` formats.
- **Post-Conversion Recovery**: Manual review and touch-up after PPTX → Markdown conversion to restore ASCII slide boxes and speaker comments.

## Technologies and Standards

- **Markdown**: The primary format for the presentation file.
- **ASCII Art**: Used for visual slide representation within code blocks.
- **PPTX**: The output format for delivery in PowerPoint.
- **Python + python-pptx**: Scripts in `scripts/` handle Markdown ↔ PPTX conversion.

## Presentation Styles

The `md2pptx.py` script applies a visual style to every slide (background fill, text color, and font). Styles are defined in `assets/styles.json` and selected with the `--style` flag. **`academic` is the default.**

| Style      | Background | Foreground | Font           | Intended use                          |
| ---------- | ---------- | ---------- | -------------- | ------------------------------------- |
| `academic` | `#FFFBF0`  | `#000F55`  | JetBrains Mono | Default. Printed-paper look, blue ink |
| `dark`     | `#000F55`  | `#FFFFFF`  | JetBrains Mono | Projectors, dark lecture halls        |
| `minimal`  | `#FFFFFF`  | `#000000`  | JetBrains Mono | Clean, print-friendly                 |

- **Font fallback**: `JetBrains Mono` is set on every text run. PPTX stores a single font name per run, so no fallback chain is encoded. If the font is not installed on the viewer's machine, PowerPoint substitutes its own default font. Install JetBrains Mono on machines that open the deck for the intended look.
- **Adding a style**: Add a new entry to `assets/styles.json` with `background`, `foreground` (hex), and `font` keys; it becomes available to `--style` automatically.

## Best Practices

- **Rule of Ten**: Aim for no more than ten bullet points per slide and ten words per bullet point.
- **Visual Hierarchy**: Use headers and bold text within slides to emphasize key points.
- **Narrative Flow**: Ensure the `__Comment:__` sections create a cohesive story when read sequentially.
- **Consistency**: Stick to the provided templates to maintain a professional and uniform look.
- **Convert Early, Convert Often**: Validate the PPTX output early to catch layout issues before investing time in details.
- **Lossy Awareness**: ASCII art formatting is best-effort during PPTX → Markdown conversion; always review and adjust the output.

## Examples

- See `examples/presentation_ecodam2025.md` for a full implementation of a scientific presentation.

## Recommendations

- Use `two-columns.md` when comparing "Before vs After" or "Problem vs Solution".

## Constraints

- **Fixed Dimensions**: 
    - Width: 66 characters (64 content + 2 borders).
    - Height: 15 lines total (13 content lines + 2 border lines). The `md2pptx.py` script warns if a slide box deviates from 15 lines.
- **Slide Numbering**: Slide numbers are 1-based. The first slide (`## Slide 1.`) is the title slide; `## Slide N.` counts up for every subsequent slide.
- **Text Alignment**: 
    - Left-aligned: `<<Text` or `Text` (default)
    - Right-aligned: `>>Text`
    - Centered: `=Text`
- **Slide Type Specification**: Use `slide:[type]` in the code block tag (e.g., ` ```slide:title `). Defaults to `content` if type is omitted.
- **Format Strictness**: Each slide must follow the pattern: `## Slide X. Title` -> ```slide:[type] ... ``` -> `__Comment:__` followed by narrative text.

## Limitations

- **Fixed layout**: Slides are rendered at a fixed size with no text auto-fitting; content longer than the 15-line box may overflow or be clipped in the PPTX export.
- **Text only**: Images, tables, charts, and embedded media are not supported; the ASCII format is text-only.
- **Borders are presentational**: ASCII box borders and structure are discarded when converting to PPTX; only inner text, alignment, and the single/two-column layout are rendered.
- **Lossy PPTX conversion**: `pptx2md.py` restores a best-effort ASCII approximation; always review and adjust the output.

## Deliverables / Artifacts

- A Markdown file (`.md`) containing a sequence of slides and speaker notes.
- A PPTX file (`.pptx`) generated from the Markdown for delivery in PowerPoint.

## Output Contract

The output must be a Markdown document structured as follows:
1. **Slide Header**: `## Slide [Number]. [Title]`
2. **Slide Visual**: A code block tagged with `slide` containing the ASCII art box.
3. **Speaker Notes**: A line starting with `__Comment:__` followed by the narrative text.

Example:

````markdown
## Slide 1. Introduction

```slide:content
+----------------------------------------------------------------+
| Introduction                                                   |
|                                                                |
+----------------------------------------------------------------+
| - Point A                                                      |
| - Point B                                                      |
|                                                                |
|                                                                |
|                                                                |
|                                                                |
|                                                                |
|                                                                |
|                                                                |
|                                                                |
+----------------------------------------------------------------+
```

__Comment:__ This is the detailed explanation for Slide 1.
````

When converting to PPTX, the output contract also includes a `.pptx` file with each Markdown slide mapped to a PowerPoint slide. Speaker notes (`__Comment:__`) become PowerPoint speaker notes. ASCII art slide borders are discarded; only the inner text content is preserved.

## Input Recovery Rules

- **Missing Content**: If the source material lacks a specific section (e.g., no "Future Work"), omit the slide or ask the user if they would like to add the content.
- **Overly Dense Text**: If a section is too large for one slide, split it into multiple slides (e.g., "Methodology 1/2", "Methodology 2/2").
- **Ambiguous Structure**: If the document structure is unclear, propose an outline to the user before generating the slides.
- **PPTX Without Speaker Notes**: If the source PPTX has no speaker notes, leave the `__Comment:__` section empty so the user can fill it in later.
- **PPTX With Complex Layouts**: If the source PPTX contains tables, images, or non-text elements, extract only the textual content and inform the user about elements that were not converted.
