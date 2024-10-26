import pydantic


class ReturnAnswer(pydantic.BaseModel):
    question: str
    answer: str

class Question(pydantic.BaseModel):
    question: str