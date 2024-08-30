from pydantic import BaseModel


class Zipovskaya(BaseModel):
    cold: int | None
    warm: int | None
    electric: int | None