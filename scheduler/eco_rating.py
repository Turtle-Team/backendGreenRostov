import json

from database import Database
from database.operations import OperationBillData


from openai import OpenAI

import setting


class NeuroCommentator:
    def __init__(self):
        self.client = OpenAI(api_key=setting.OPENAI_API_KEY, base_url="https://api.deepseek.com")
        self.pre_prompt = """Твоя задача это выдавать итог по углеродному следу (СО2) в килограммах в точности до тысячных. 
        Мне нужен итог строго в формате [{"name": Продукт, "eco_rating": Итог, "desk": Обоснование твоего выбора},...].
        Я тебе даю список продуктов, ты мне даешь итог строго по формату.\n\n"""

    def generate_comment(self, quest):
        prompt = f"{self.pre_prompt}Продукты: {quest}"

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt},
            ],
            stream=False,
            temperature=1
        )

        return response.choices[0].message.content.strip()


def create_patrol():
    session = Database().get_marker()
    no_eco_rating = session.query(OperationBillData).filter(OperationBillData.eco_rating == None).all()
    nc = NeuroCommentator()
    for bill in no_eco_rating:
        bill: OperationBillData
        answer = nc.generate_comment(bill.nomenclature)
        answer = json.loads(answer.replace('json', '').replace('`','').replace('\n', ''))
        session.query(OperationBillData).where(OperationBillData.id == bill.id).update({'eco_rating': answer[-1]['eco_rating']})
        session.commit()

create_patrol()

