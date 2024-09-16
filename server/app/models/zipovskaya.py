from sqlmodel import SQLModel, Field


class Zipovskaya(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    cold: int = Field(default=None, nullable=True)
    warm: int = Field(default=None, nullable=True)
    electric: int = Field(default=None, nullable=True)

