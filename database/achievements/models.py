import pydantic

class AllAchievements(pydantic.BaseModel):
    achievements_id: int
    user_id: int
    header: str
    text: str
    exp: int
    image: str
    complete: bool = False