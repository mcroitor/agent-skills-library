# Example Request - Standard Rubric Output for C++ "IntStack"

This example demonstrates the default behavior of the Rubric Designer skill: a standard request returns the grading rubric only, presented as the Criteria and Levels Table. Use it as a reference when the user asks to create a rubric but does not ask for full documentation.

---

## Note (not part of the default output)

> **The main output of this skill is the Criteria and Levels Table in Section 3.**
>
> This example shows the default (rubric-only) output: the Criteria and Levels Table alone, with all assumptions, weights, and penalties embedded in the table and notes. For full documentation with alignment, scoring model, calibration, and checklists, see [example-rubric-academic-writing-definition.md](example-rubric-academic-writing-definition.md).
---

## Example Request (input to the skill)

> Create a grading rubric for this assignment.
>
> Define a `IntStack` class in C++.
>
> Required operations: `push(int)`, `pop()`, `top()`, `empty()`, `size()`. The stack must report overflow and underflow and must not leak memory.
>
> The implementation must compile with `g++ -std=c++17 -Wall -Wextra -fsanitize=address,undefined` and must pass a small `main()` driver that exercises push/pop/top/empty/size in order.
>
> Submission: `IntStack` class definition, without implementation source code.

## Expected Default Output

The standard response returns only the Criteria and Levels Table. Assumptions, inferred objectives, weights, and penalties are embedded directly in the table and notes.

| ID  | Criterion | Weight `q_i` | Penalty `D_i` per error | 0% | 25% | 50% | 75% | 100% | Notes |
| --- | ------------------------------------- | ------------ | ----------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| C-1 | Stack state model and invariant       | 1            | 10                      | The implementation has no coherent state model, or the state cannot support stack behavior | A state model exists but the invariant is missing or contradicted by the implementation | The state model is present and the invariant is only partially enforced or documented                      | The state model and invariant are mostly clear; one minor gap remains in documentation or preservation   | The implementation uses a coherent state model, and the invariant is clearly documented or directly observable in code and preserved across operations                           | The rubric does not require a specific internal representation                                                                                |
| C-2 | Public API matches the brief          | 1            | 5                       | One or more required methods are missing or have the wrong signature                       | All methods are declared but at least one required signature is wrong                   | All required methods are declared with minor qualifier inconsistencies that do not change the intended API | All required methods are declared with the expected signatures; one minor inessential difference remains | The public API exposes `push(int)`, `pop()`, `top()`, `empty()`, and `size()` in a form consistent with the brief and with clearly documented error signaling for invalid states | Error signaling may use exceptions or another explicit, documented mechanism consistent with the brief                                        |
| C-3 | Correct observable LIFO behavior      | 3            | 5                       | Driver fails to run or produces wrong order on any operation                               | Driver runs; more than one operation gives a wrong result                               | Driver runs; exactly one operation gives a wrong result                                                    | Driver runs; all operations correct but boundary behavior (empty stack, full stack) is not exercised     | All operations give the expected results for push, pop, top, empty, size on a non-empty and an empty stack                                                                       | This criterion is weighted highest because it is the core learning outcome                                                                    |
| C-4 | Overflow and underflow handling       | 2            | 5                       | No handling: silent wrap-around, crash, or UB on overflow/underflow                        | One of overflow/underflow is handled; the other is not                                  | Both overflow and underflow are handled but the signal is ambiguous (e.g., a magic return value)           | Both are handled with a clear, documented signal; one case leaks a side effect                           | Both overflow and underflow are handled with explicit, documented signals (exception type, enum, or boolean flag) and no side effects beyond the signal                          | The brief does not prescribe the exact mechanism                                                                                              |
| C-5 | Memory safety and resource management | 2            | 10                      | Build with ASan/UBSan fails or reports leak/UB on any test                                 | Build with sanitizers succeeds but reports one of: leak, double-free, out-of-bounds     | Build with sanitizers succeeds; one non-critical warning remains                                           | Build with sanitizers succeeds; warnings are clean except for one minor issue unrelated to memory safety | Build with `-Wall -Wextra -fsanitize=address,undefined` is warning-clean; no leaks and no undefined behavior are observed                                                        | If the student used raw `new[]`/`delete[]` correctly, full credit is still awarded; only observable behavior and sanitizer results are graded |

Sum of weights: `sum(q_i) = 1 + 1 + 3 + 2 + 2 = 9`.
