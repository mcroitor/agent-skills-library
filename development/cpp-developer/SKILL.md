---
name: cpp-developer
description: Use when implementing, debugging, refactoring, testing, reviewing, or optimizing C++ code, including .cpp/.cc/.h/.hpp files, CMake projects, compiler or linker errors, segfaults, undefined behavior, memory leaks, data races, dangling references, ownership and lifetime issues, concurrency, embedded or real-time targets, and profile-guided performance work.
---

# C++ Developer

Safety-first guidance for implementing and validating C++ changes while avoiding speculative optimization.

## Priority Rules
Prioritize in this order when trade-offs conflict:
1. Correctness, memory safety, and clear behavior
2. Explicit performance and resource requirements
3. Maintainability and simplicity
4. Portability

A performance target is a measurable requirement; do not equate it with maximizing performance at any cost.

## Style Precedence
1. Conventions and configuration of the existing project (file names, extensions, naming, formatting, error handling)
2. Google C++ Style Guide (https://google.github.io/styleguide/cppguide.html) for new code and new projects
3. Other guidance in this skill

Do not mix styles within one file. Where this skill conflicts with the Google C++ Style Guide, follow the guide unless the project states otherwise. Refer to the guide for details instead of restating them.

## Instructions
1. **Plan architecture when needed** - for tasks spanning multiple components, define module boundaries, ownership, and interfaces; for an isolated function or local change, follow the existing design
2. **Use safe memory patterns** - RAII, values, and smart pointers
3. **Write modern C++** - use the project's C++ standard and only features its toolchain supports
4. **Leverage STL** - containers, algorithms, iterators
5. **Test behavior** - cover normal cases, boundaries, preconditions, and error handling
6. **Measure performance** - profile representative workloads before tuning and verify any improvement
7. **Document APIs** - concise comments for public interfaces, in the project's comment style

## Language Standard
- Use the project's C++ standard. If it is not specified, assume C++20.
- Use C++23 only when requested and when the target compiler and standard library support the required features.
- If the project targets a standard below C++20, do not use unavailable features (`std::span`, `std::jthread`, concepts, and so on); use project-appropriate alternatives.
- Ask for clarification only when performance requirements or the target platform significantly affect the approach.

## Ownership and Interfaces
- Express ownership explicitly.
- Prefer values for ordinary object ownership; use `std::unique_ptr` by default when dynamic ownership is needed.
- Use `std::shared_ptr` only when shared lifetime ownership is required.
- Use references for required non-owning access and raw pointers for optional or non-owning observation or interoperability, when the lifetime contract is clear.
- Use RAII for resource management; avoid manual cleanup unless required by the API or runtime.
- Make copyability and movability of a class explicit; prefer defaults that need no hand-written special members.
- Separate declarations (`.h`/`.hpp`) from implementations (`.cc`/`.cpp`) to reduce compilation dependencies. Templates and `inline` or `constexpr` definitions stay in headers.
- Follow the project's file extensions; use `.h` and `.cc` for new projects.

## Best Practices
- Use named constants (`constexpr` or `const`) for non-obvious values instead of unexplained magic literals. Keep inherently clear values such as `0` in ordinary indexing or arithmetic expressions inline.
- Prefer object-oriented design when it improves encapsulation, models domain concepts, or manages state and lifetimes. Do not introduce classes solely to force an OOP structure onto simple stateless algorithms or small utilities. Prefer composition over implementation inheritance.
- Keep functions focused on a single responsibility. Favor low cyclomatic complexity and simplify branching when it obscures behavior; use line count as a prompt to review, not as a quality target.
- Use `const` correctly on parameters, methods, and non-local variables.
- Use move semantics to transfer ownership of expensive-to-copy objects; mark move constructors and move assignment operators `noexcept` when possible.
- Use `constexpr` when compile-time evaluation is useful, and `consteval` only when the API contract requires compile-time evaluation.
- Prefer concepts over SFINAE when the target standard supports them. Avoid excessive template complexity.
- Guard against integer pitfalls: avoid mixing signed and unsigned types, check for overflow where input is untrusted, and use checked access (`at()` or explicit bounds checks) when indices are not proven valid.

## Error Handling
- Follow the project's and API's established error-handling conventions.
- In new code under Google Style, do not use exceptions; report expected failures with status or result types (such as `std::expected` when the standard allows it, or the project's equivalent).
- Where the project or platform uses exceptions, use them for exceptional failures only; keep exception and non-exception code separated at clear boundaries and convert errors there.
- Preserve invariants, propagate failures with useful context, and never silently swallow errors.

### Embedded Targets
- Follow the project's configuration: when required, do not rely on exceptions or RTTI, avoid dynamic allocation after initialization, and use the project's status or error-code conventions.
- Keep operations bounded and respect the target's timing, memory, and other resource constraints.

## Testing and Validation
- Test boundary cases, preconditions, and error-handling paths (and exceptions where the project uses them).
- Validate at least a Debug build; also validate performance-critical changes in Release.
- Use the project's existing test framework; for new projects, Catch2 (https://github.com/catchorg/Catch2) is the default choice.
- If the environment cannot build or run tests, state which checks were not performed and why. Never imply unrun checks passed.

## Safety Tooling
- Use AddressSanitizer and UndefinedBehaviorSanitizer where supported (`-fsanitize=address,undefined` with GCC or Clang, `/fsanitize=address` with MSVC); use ThreadSanitizer for suitable concurrent code.
- Enable `-Wall -Wextra` with GCC or Clang and `/W4` with MSVC, and address relevant warnings. Consider `-Werror` or `/WX` in CI when project policy allows.
- Run `clang-tidy` or the project's equivalent static analysis where available.

## Concurrency and Lifetime Safety
- Prefer `std::jthread` for scoped thread lifetime and `std::scoped_lock` when locking multiple mutexes; use alternatives when the target standard or API requires them.
- Protect shared mutable state with a mutex. Use atomics for simple independent flags or counters, not as a substitute for protecting compound state.
- Use `std::memory_order_seq_cst` by default. Choose weaker ordering only when necessary and when the guarantees are understood and validated.
- Treat `std::span`, `std::string_view`, references, pointers, iterators, and lambda reference captures as non-owning. Ensure the referenced object outlives every use.
- Do not retain views or iterators past the lifetime of their source; account for iterator invalidation after container mutations or reallocations. Avoid reference captures when a lambda may outlive the captured scope or run asynchronously.

## Technologies
- Build systems: CMake, Make
- Toolchains: GCC, Clang, MSVC
- Select libraries during design based on requirements, target-platform support, maintenance, licensing, and existing project dependencies.

## Output Contract
- Deliver the requested code and include or update build configuration (such as `CMakeLists.txt`) and tests when the change requires them.
- Summarize the changes and report build, test, and tooling results; clearly identify any checks that could not be run.