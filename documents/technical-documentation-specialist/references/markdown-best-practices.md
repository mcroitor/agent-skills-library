# Markdown Best Practices

These guidelines ensure maximum compatibility across different Markdown processors and renderers, based on recommendations from the [Markdown Guide](https://www.markdownguide.org/basic-syntax/).

## General Formatting

- **Headings**:
  - Always put a space between the number signs (`#`) and the heading name (e.g., `# Heading`, not `#Heading`).
  - Put blank lines before and after a heading.
- **Paragraphs**:
  - Do not indent paragraphs with spaces or tabs unless the paragraph is in a list.
- **Horizontal Rules**:
  - Put blank lines before and after horizontal rules (`---`, `***`, or `___`).

## Emphasis and Styling

- **Bold and Italic**:
  - Use asterisks (`*` or `**`) instead of underscores when emphasizing the middle of a word (e.g., `Love**is**bold`) to ensure compatibility across all processors.

## Lists and Blockquotes

- **Ordered Lists**:
  - Use periods only as delimiters (e.g., `1. First item`). Avoid using parentheses (e.g., `1)`).
- **Unordered Lists**:
  - Do not mix and match delimiters (`-`, `*`, `+`) within the same list; pick one and be consistent.
- **Blockquotes**:
  - Put blank lines before and after blockquotes.

## Links and Images

- **URL Encoding**:
  - URL encode spaces as `%20`.
  - URL encode opening parentheses `(` as `%28` and closing parentheses `)` as `%29`.

## HTML Integration

- **Block-level Elements**:
  - Use blank lines to separate block-level HTML elements (like `<div>`, `<table>`, `<pre>`, and `<p>`) from surrounding content.
  - Do not indent HTML tags with tabs or spaces.
- **Markdown in HTML**:
  - Remember that Markdown syntax is generally not processed inside block-level HTML tags.
