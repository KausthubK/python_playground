from pydantic import BaseModel, conint, constr


class User(BaseModel):
    age: conint(ge=1) # type: ignore
    first_name: constr(min_length=2) # type: ignore
    last_name: constr(min_length=2) # type: ignore
