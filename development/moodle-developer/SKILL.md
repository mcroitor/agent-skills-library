---
name: moodle-developer
description: Develop and customize Moodle LMS solutions. Use for plugin development, theme customization, API integration, performance tuning, and Moodle administration.
---

# Moodle Developer

## Description
A skill for developing, customizing, and operating Moodle LMS solutions. It combines PHP engineering with Moodle-specific architecture, plugin development, theming, and performance tuning.

## Priority Rules
Prioritize in this order when trade-offs conflict:
1. Data integrity and user access control
2. Moodle API compliance
3. Performance and scalability
4. Maintainability and upgrade safety

## When to Use
- Installing and configuring Moodle
- Building custom Moodle plugins
- Customizing themes and UX
- Integrating external services (API, SSO)
- Optimizing Moodle performance
- Debugging and maintaining Moodle instances
- Extending learning workflows and reports

## Instructions
1. **Learn Moodle architecture** - core modules, plugin types, APIs
2. **Set up local environment** - reproducible dev setup
3. **Model functional scope** - roles, courses, activities, blocks
4. **Develop plugin** - follow plugin skeleton and naming rules
5. **Use Moodle APIs** - data, forms, events, capabilities
6. **Write tests** - PHPUnit and Behat scenarios
7. **Tune performance** - cache strategy and DB optimization
8. **Secure implementation** - validation, permissions, tokens
9. **Document and version** - changelog and upgrade path

## Input Recovery Rules
- Assume modern Moodle (4.x+) when version is not specified
- Ask for clarification only when plugin type or Moodle version significantly affects development approach

## Constraints
- Do not bypass Moodle APIs for database access
- Do not skip capability checks
- Do not ignore upgrade compatibility

## Moodle Structure
- Core components
- Plugins and local extensions
- Themes
- Admin and lib subsystems

## Plugin Types
- Activity modules
- Blocks
- Authentication plugins
- Enrollment plugins
- Filters
- Reports
- Web services

## Development Essentials
- `version.php`, `settings.php`
- `db/upgrade.php` for schema migrations
- `lang/en/...` localization files
- `classes/` PSR-4 classes
- `templates/` Mustache templates
- `tests/` PHPUnit/Behat tests

## Moodle API Areas
- Data API
- Forms API
- Events and observers
- Web Services API
- Capabilities and contexts

## Performance and Security
- Cache API usage
- MariaDB indexing and query tuning
- Safe output handling and CSRF checks
- Role/capability validation for all actions

## Tooling
- VS Code or PhpStorm
- Composer
- PHPUnit and Behat
- Git
- Moodle plugin directory and docs
