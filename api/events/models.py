import pydantic


class EventCreate(pydantic.BaseModel):
    name: str
    description: str
    latitude: float
    longitude: float


class RegisterEvent(pydantic.BaseModel):
    user_id: int
    event_id: int


class EventMembersResponse(pydantic.BaseModel):
    event_id: int
    members: list
