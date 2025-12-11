"""
Pandera Schema Validation Example
Run: python pandera_example.py
"""
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame, Series


# Define schema using Pandera
class UserSchema(pa.DataFrameModel):
    user_id: Series[int] = pa.Field(gt=0)
    username: Series[str] = pa.Field(str_length={"min_value": 3, "max_value": 50})
    email: Series[str] = pa.Field(str_contains="@")
    age: Series[int] = pa.Field(ge=18, le=120)
    is_active: Series[bool]

    class Config:
        strict = True
        coerce = True


# Function with Pandera schema validation
@pa.check_types
def process_users(users: DataFrame[UserSchema]) -> DataFrame[UserSchema]:
    """Process user data with automatic schema validation."""
    print("\n[Pandera] Processing users...")
    # Apply some transformations
    users = users.copy()
    users['username'] = users['username'].str.lower()
    return users


def main():
    print("=" * 60)
    print("PANDERA SCHEMA VALIDATION EXAMPLE")
    print("=" * 60)

    # Valid data
    print("\n1. Testing with VALID data:")
    df_valid = pd.DataFrame({
        'user_id': [1, 2, 3],
        'username': ['Alice', 'Bob', 'Charlie'],
        'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
        'age': [25, 30, 35],
        'is_active': [True, True, False]
    })

    print("\nInput DataFrame:")
    print(df_valid)

    result = process_users(df_valid)

    print("\nOutput DataFrame (usernames lowercased):")
    print(result)
    print("\n✓ Validation passed!")

    # Invalid data
    print("\n" + "=" * 60)
    print("2. Testing with INVALID data (age < 18):")
    df_invalid = pd.DataFrame({
        'user_id': [4, 5],
        'username': ['Dave', 'Eve'],
        'email': ['dave@example.com', 'eve@example.com'],
        'age': [16, 17],  # Invalid: below minimum age
        'is_active': [True, False]
    })

    print("\nInput DataFrame:")
    print(df_invalid)

    try:
        result = process_users(df_invalid)
        print("\nOutput DataFrame:")
        print(result)
    except pa.errors.SchemaError as e:
        print("\n✗ Validation failed (as expected)!")
        print(f"Error: {e}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
