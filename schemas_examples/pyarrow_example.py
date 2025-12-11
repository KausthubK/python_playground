"""
PyArrow Schema Validation Example
Run: python pyarrow_example.py
"""
import pyarrow as pa
import pyarrow.compute as pc


# Define schema using PyArrow
user_schema = pa.schema([
    ('user_id', pa.int64(), False),  # not nullable
    ('username', pa.string(), False),
    ('email', pa.string(), False),
    ('age', pa.int64(), False),
    ('is_active', pa.bool_(), False)
])


def process_users_arrow(table: pa.Table) -> pa.Table:
    """Process user data with PyArrow schema validation."""
    print("\n[PyArrow] Processing users...")

    # Validate input schema
    if not table.schema.equals(user_schema):
        raise ValueError(
            f"Input schema mismatch.\nExpected: {user_schema}\nGot: {table.schema}"
        )

    # Apply transformations using PyArrow compute functions
    username_lower = pc.utf8_lower(table['username'])

    # Create new table with transformed data
    result = pa.table({
        'user_id': table['user_id'],
        'username': username_lower,
        'email': table['email'],
        'age': table['age'],
        'is_active': table['is_active']
    }, schema=user_schema)

    return result


def main():
    print("=" * 60)
    print("PYARROW SCHEMA VALIDATION EXAMPLE")
    print("=" * 60)

    # Valid data
    print("\n1. Testing with VALID data:")
    table_valid = pa.table({
        'user_id': [1, 2, 3],
        'username': ['Alice', 'Bob', 'Charlie'],
        'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
        'age': [25, 30, 35],
        'is_active': [True, True, False]
    }, schema=user_schema)

    print("\nInput Table:")
    print(table_valid.to_pandas())

    result = process_users_arrow(table_valid)

    print("\nOutput Table (usernames lowercased):")
    print(result.to_pandas())
    print("\n✓ Validation passed!")

    # Invalid schema (missing column)
    print("\n" + "=" * 60)
    print("2. Testing with INVALID schema (missing 'is_active' column):")

    invalid_schema = pa.schema([
        ('user_id', pa.int64(), False),
        ('username', pa.string(), False),
        ('email', pa.string(), False),
        ('age', pa.int64(), False)
        # Missing 'is_active' column
    ])

    table_invalid = pa.table({
        'user_id': [4, 5],
        'username': ['Dave', 'Eve'],
        'email': ['dave@example.com', 'eve@example.com'],
        'age': [25, 30]
    }, schema=invalid_schema)

    print("\nInput Table:")
    print(table_invalid.to_pandas())

    try:
        result = process_users_arrow(table_invalid)
        print("\nOutput Table:")
        print(result.to_pandas())
    except ValueError as e:
        print("\n✗ Validation failed (as expected)!")
        print(f"Error: {e}")

    # Note about value constraints
    print("\n" + "=" * 60)
    print("NOTE: PyArrow focuses on TYPE validation, not VALUE constraints.")
    print("For example, PyArrow won't validate if age < 18 (that's app logic).")
    print("Pandera excels at value-level validation with Field constraints.")
    print("=" * 60)


if __name__ == "__main__":
    main()
