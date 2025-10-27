from datetime import date

from pydantic import BaseModel


class Person(BaseModel):
    """A Pydantic model representing a person."""

    first_name: str
    last_name: str
    date_of_birth: date


if __name__ == "__main__":
    person = Person(
        first_name="Alice",
        last_name="Smith",
        date_of_birth=date(1990, 5, 15)
    )

    print(f"First Name: {person.first_name}")
    print(f"Last Name: {person.last_name}")
    print(f"Date of Birth: {person.date_of_birth}")
    print(f"\nFull details:\n{person}")
