# Profiling Python Code with py-spy

This repository demonstrates how to profile Python code using the `py-spy` tool. Profiling is essential for identifying performance bottlenecks in your code, and `py-spy` provides a simple way to do this without modifying your code.

## Prerequisites

- `py-spy` (can be installed via pip or used through Poetry)

## Run the Profiler

```
py-spy record -s -i -f speedscope -r 20 -o example_profile -- python ex.py
```

This command will profile the `ex.py` script and generate a `example_profile` file in the Speedscope format, which can be viewed using the [Speedscope](https://www.speedscope.app/) web application, or with a compatible viewer (see [Speedscope VSCode extension](https://marketplace.visualstudio.com/items?itemName=sransara.speedscope-in-vscode)).
