---
name: skeleton-designer
description: Build lightweight interfaces with Skeleton CSS. Use for minimalist UI, fast prototyping, semantic HTML-first layouts, and low-complexity designs.
---

# Skeleton Designer

## Description
A specialized frontend design skill based on Frontend Designer for creating lightweight, responsive interfaces with Skeleton CSS and semantic HTML.

## Priority Rules
Prioritize in this order when trade-offs conflict:
1. Accessibility
2. Semantic HTML structure
3. Minimal CSS footprint
4. Responsive behavior

## When to Use
- Building clean minimalist UI quickly
- Prototyping responsive interfaces
- Using a lightweight CSS framework
- Prioritizing fast page load and low complexity
- Building semantic HTML-first layouts

## Instructions
1. **Set up files** - Include `normalize.css` and `skeleton.css` (from assets or CDN), create `app.css` for custom styles
2. **Build semantic HTML structure** - Use `.container` > `.row` > `.column/.columns` grid layout; refer to Component Catalog for form, button, table patterns
3. **Choose grid layout** - Map design to 12-column grid; use `.four.columns`, `.six.columns`, etc. per Grid System Specifics; let Skeleton handle responsive stacking
4. **Compose with Skeleton defaults** - Rely on Skeleton's `<h1>`–`<h6>`, `<button>`, `<input>`, `<table>` styles; avoid overriding unless necessary
5. **Extend in app.css only** - Add custom colors, spacing, cards, or utility classes in `app.css`; keep it minimal (< 200 lines)
6. **Test mobile breakpoints** - Verify layout at 400px and 550px; ensure keyboard navigation and color contrast (WCAG 2.1 AA)
7. **Validate semantics** - Use proper heading hierarchy, label inputs, ensure alt text on images

## Input Recovery Rules
- Assume Skeleton CSS when version is not specified
- Ask for clarification only when specific styling requirements significantly affect the approach

## Constraints
- Do not add external libraries unless essential
- Do not overload with custom CSS
- Do not skip semantic HTML for visual convenience

## File Structure
Always create:
- `normalize.css` — resets browser defaults (from assets, or link via CDN)
- `skeleton.css` — framework base (from assets, or link via CDN)
- `app.css` — **custom layer for colors, spacing, typography tokens** (default name unless specified otherwise)

## Skeleton CSS Highlights
- Very small CSS footprint (~400 lines)
- 12-column responsive grid with media queries at 400px and 550px
- Clean typography and form defaults (h1–h6, p, label, input, button, table)
- Easy to customize with CSS class composition
- No JavaScript dependency
- Good baseline for semantic HTML-first layouts
- Grid classes: `.one.column` through `.twelve.columns` (or `.one.columns` through `.twelve.columns`)
- Container breakpoint behavior: fluid < 400px, 85% width at 400px, 80% at 550px+

## Component Catalog

### Grid and Layout
**Basic container and columns** (12-column layout):
```html
<div class="container">
  <div class="row">
    <div class="six columns"><!-- 50% width --></div>
    <div class="six columns"><!-- 50% width --></div>
  </div>
  <div class="row">
    <div class="four columns"><!-- ~33% --></div>
    <div class="four columns"><!-- ~33% --></div>
    <div class="four columns"><!-- ~33% --></div>
  </div>
</div>
```

### Typography and Headings
Skeleton provides default styles for `<h1>` through `<h6>`, `<p>`, `<strong>`, `<em>`, without additional classes required.

### Forms
**Form elements with defaults**:
```html
<label for="username">Username</label>
<input class="u-full-width" type="text" id="username">

<label for="message">Message</label>
<textarea class="u-full-width" id="message"></textarea>

<input type="checkbox" id="agree">
<label for="agree">I agree to the terms</label>

<button class="button-primary">Submit</button>
<button>Secondary Action</button>
```

### Buttons
```html
<button class="button-primary">Primary Action</button>
<button class="button">Default Button</button>
<a class="button" href="#about">Link as Button</a>
```

### Tables
```html
<table class="u-full-width">
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John</td>
      <td>john@example.com</td>
    </tr>
  </tbody>
</table>
```

### Lists
Skeleton defaults work for `<ul>`, `<ol>`, `<dl>` without extra classes.

### Code and Preformatted Text
```html
<pre><code>const x = 42;</code></pre>
```

### Utility Classes
- `.u-full-width` — width: 100%
- `.u-max-full-width` — max-width: 100%
- `.u-pull-left` — float: left
- `.u-pull-right` — float: right

## Grid System Specifics

### Breakpoints
- **Mobile-first** (< 400px): Full-width columns, single column layout
- **Small devices** (≥ 400px): Container becomes 85% width
- **Larger devices** (≥ 550px): Container is 80% width, columns gain left margin (4%) for spacing

### Column Classes
Use `.column` or `.columns` (both work):
- `.one.column` / `.one.columns` — 4.67% (1/12)
- `.two.columns` — 13.33% (2/12)
- `.three.columns` — 22% (3/12)
- `.four.columns` — 30.67% (4/12)
- `.six.columns` — 48.33% (6/12)
- `.twelve.columns` — 100% (full width)

### Responsive Behavior
Columns stack on mobile (< 550px) and distribute horizontally on larger screens. Always use semantic `.row` divs to group columns.

## Code Patterns

### Two-Column Layout
```html
<div class="container">
  <div class="row">
    <div class="eight columns">
      <h2>Main Content</h2>
      <p>Primary content area...</p>
    </div>
    <div class="four columns">
      <h3>Sidebar</h3>
      <p>Secondary content...</p>
    </div>
  </div>
</div>
```

### Three-Column Grid
```html
<div class="container">
  <div class="row">
    <div class="four columns">
      <h3>Card 1</h3>
      <p>Description</p>
    </div>
    <div class="four columns">
      <h3>Card 2</h3>
      <p>Description</p>
    </div>
    <div class="four columns">
      <h3>Card 3</h3>
      <p>Description</p>
    </div>
  </div>
</div>
```

### Form Layout
```html
<div class="container">
  <div class="row">
    <div class="six columns">
      <label for="firstName">First Name</label>
      <input class="u-full-width" type="text" id="firstName">
    </div>
    <div class="six columns">
      <label for="lastName">Last Name</label>
      <input class="u-full-width" type="text" id="lastName">
    </div>
  </div>
  <button class="button-primary" type="submit">Submit</button>
</div>
```

## Extension Patterns

### Custom Colors and Spacing (in `app.css`)
```css
/* Override button colors */
.button.button-primary {
  background-color: #2196F3;
  border-color: #1976D2;
}

/* Add custom spacing utility */
.u-margin-top {
  margin-top: 2rem;
}

/* Add custom card style */
.card {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 1rem;
  background-color: #f9f9f9;
}
```

### CSS Variables for Theming
```css
:root {
  --primary-color: #2196F3;
  --spacing-unit: 1rem;
  --border-radius: 4px;
}

.button.button-primary {
  background-color: var(--primary-color);
}
```

## When NOT to Use Skeleton CSS
- **Complex component libraries needed** — Use Bootstrap or Tailwind if you need modals, dropdowns, carousels
- **Heavy customization required** — If design is very custom or uses complex layout patterns (CSS Grid, advanced Flexbox), Tailwind may be more efficient
- **Design system scope** — If building a large design system with many theme variations, Tailwind's config is more scalable
- **Team size/consistency** — For large teams that need strict design enforcement, a component-based framework is better
- **Admin panels with heavy data** — Bootstrap's data table and component library is more mature for complex UIs

## When TO Use Skeleton CSS (Best Fit)
✅ Landing pages and marketing sites  
✅ Simple CRUD interfaces  
✅ Documentation sites  
✅ Prototypes and MVPs  
✅ Projects with minimal custom styling  
✅ Lightweight applications prioritizing load time  

## Tools and Practices
- Skeleton CSS v2.0.4 (or latest compatible)
- Normalize.css for browser reset
- HTML5 semantics
- CSS3 custom properties for theming
- Minimal custom CSS in `app.css`
- DevTools responsive mode for breakpoint testing
- WCAG 2.1 accessibility basics (keyboard navigation, color contrast)

## Required Assets
When creating a Skeleton project, always include:
1. `normalize.css` — browser reset layer (from assets)
2. `skeleton.css` — framework layer (from assets)
3. `app.css` — **custom layer (create new file)** — for project-specific colors, spacing, typography, and component extensions
