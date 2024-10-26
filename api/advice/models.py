import pydantic


class RandomAdvice(pydantic.BaseModel):
    id: int
    name: str
    description: str
