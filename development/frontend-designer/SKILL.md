---
name: frontend-designer
description: Design responsive and accessible frontend interfaces. Use for UI architecture, component systems, responsive layouts, and design system implementation.
---

# Frontend Designer

## Description
A base skill for designing responsive, accessible, and maintainable frontend interfaces across different CSS approaches and design systems. If design decisions conflict because of time, scope, or resource constraints, prioritize accessibility first, then responsiveness, then delivery speed.

## Priority Rules
Prioritize in this order when trade-offs conflict:
1. Accessibility
2. Responsiveness
3. Delivery speed
4. Visual polish

## When to Use
- Designing UI architecture before framework-specific implementation
- Creating consistent component systems and layout rules
- Building responsive interfaces for desktop and mobile
- Enforcing accessibility and semantic HTML standards
- Preparing foundation for Bootstrap, Tailwind, or Skeleton implementations

## Instructions
1. **Understand design goals** - users, brand, and task flow
2. **Sketch layout** - wireframes and information hierarchy
3. **Define layout system** - grid, spacing scale, and breakpoints
4. **Create reusable components** - buttons, forms, cards, navigation, sections
5. **Apply customization** - spacing, colors, typography tokens
6. **Ensure responsiveness** - mobile-first behavior and adaptive patterns, while preserving the priority order: accessibility, responsiveness, then delivery speed
7. **Optimize assets** - compress images and keep CSS clean without unnecessary rules
8. **Test browsers/accessibility** - keyboard flow and contrast; if a conflict remains, keep accessibility first, then responsiveness, then delivery speed

## Input Recovery Rules
- Assume mobile-first responsive design when specific breakpoints are not specified
- Ask for clarification only when target browsers or accessibility requirements significantly affect the approach

## Constraints
- Do not sacrifice accessibility for visual polish
- Do not use non-semantic HTML without justification
- Do not skip keyboard navigation testing

## Framework Extension Strategy
- Use this skill as the base for framework-specific designer skills
- Keep component semantics independent from framework classes
- Document mappings from design tokens to framework utilities/components
- Prefer composition over one-off overrides

## Tools and Practices
- HTML5 semantics
- CSS3 (Flexbox/Grid/Custom Properties)
- Design tokens and reusable naming conventions
- Responsive design patterns
- Optional SCSS/SASS
- DevTools and Figma workflow
- WCAG 2.1 accessibility basics
