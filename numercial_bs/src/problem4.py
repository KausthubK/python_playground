"""
Problem 4: Composable Data Pipeline (Python OOP)
==================================================
~10 minutes | Pure Python (you may use typing imports)

Implement a Pipeline class that chains data transformations.

Requirements:

class Pipeline:
    def add_step(self, name: str, fn: Callable) -> "Pipeline"
        - Registers a named transformation step (fn takes one arg, returns one value)
        - Returns self to allow method chaining
        - Raises ValueError if a step with that name already exists

    def remove_step(self, name: str) -> "Pipeline"
        - Removes a step by name
        - Raises KeyError if the step doesn't exist
        - Returns self to allow method chaining

    def execute(self, data)
        - Runs all steps in insertion order, passing each step's output as
          the next step's input
        - Returns the final result
        - If no steps, returns data unchanged

    def steps(self) -> list[str]
        - Returns the list of step names in insertion order

Usage example:
    result = (
        Pipeline()
        .add_step("double", lambda x: x * 2)
        .add_step("add_one", lambda x: x + 1)
        .execute(5)
    )
    # result == 11  (5 * 2 = 10, 10 + 1 = 11)

Constraint: No external imports. Preserve insertion order of steps.
"""


class Pipeline:
    def add_step(self, name: str, fn) -> "Pipeline":
        raise NotImplementedError

    def remove_step(self, name: str) -> "Pipeline":
        raise NotImplementedError

    def execute(self, data):
        raise NotImplementedError

    def steps(self) -> list[str]:
        raise NotImplementedError
