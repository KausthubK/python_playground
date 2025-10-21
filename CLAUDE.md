# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal Python playground repository for testing and experimenting with various Python concepts, libraries, and techniques. It's organized as a collection of independent experiments in separate directories, each exploring a specific topic or technology.

## Architecture & Structure

**Multi-Project Layout**: The repository is NOT a single Python package. Each top-level directory is an independent experiment or learning module with its own dependencies. Some directories have their own `pyproject.toml` files and virtual environments.

**Key Experiment Directories**:
- `dataclass_explore/` - Dataclass experiments including nested validation package (`dataframe_validation/`)
- `mockery/` - Testing examples using pytest, pydantic, hypothesis, and pytest-mock
- `schemas_examples/` - Schema validation examples using pydantic, pyarrow, and pandera
- `pyarrow_stuff/` - PyArrow struct manipulation and experiments
- `profiling_stuff/` - Performance profiling using py-spy
- `imagey_stuff/` - Image manipulation experiments
- `async_stuff/` - Async/await examples
- `sqlite_experiments/` - SQLite database operations

**Standalone Scripts**: Many directories (e.g., `arguments/`, `bytes/`, `exceptions/`, `http/`, `looping/`, etc.) contain simple standalone Python scripts demonstrating specific concepts without dependencies.

## Development Commands

### Running Code

Since this is a collection of experiments, there's no single "run" command. Navigate to the specific experiment directory and run the Python file directly:

```bash
python <directory>/<script>.py
```

For directories with Poetry dependencies:
```bash
cd <directory>
poetry install
poetry run python <script>.py
```

### Testing

Tests use pytest and are located in `tests/` subdirectories or as `test_*.py` files:

```bash
# For projects with pytest (e.g., mockery, dataclass_explore)
cd <directory>
poetry run pytest
```

### Profiling

The `profiling_stuff/` directory uses py-spy for performance profiling:

```bash
cd profiling_stuff
./run.sh  # Runs py-spy record with speedscope output
```

This generates a `example_profile` file that can be viewed with speedscope.

### Common Dependencies

When working across different experiments, note these commonly used libraries:
- **Testing**: pytest, hypothesis, pytest-mock
- **Data validation**: pydantic, pandera
- **Data manipulation**: pyarrow, pandas
- **Performance**: py-spy

## Python Version

All projects use Python 3.10+ as specified in their `pyproject.toml` files.
