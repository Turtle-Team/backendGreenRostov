import pydantic


class UvData(pydantic.BaseModel):
    uv: float