import fastapi
from .router import route
from ..user import utils
from .models import ReturnAnswer, Question
from .ml import NeuroCommentator

@route.post("/test")
def test_expert(quest: Question,  user: dict = fastapi.Depends(utils.get_current_user)):
    return ReturnAnswer(question=quest.question, answer=user['sub'])


@route.post("")
def neuro_expert(quest: Question,  user: dict = fastapi.Depends(utils.get_current_user)):
    answer = NeuroCommentator().generate_comment(quest)
    return ReturnAnswer(question=quest.question, answer=answer)