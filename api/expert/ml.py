from openai import OpenAI

import setting


class NeuroCommentator:
    def __init__(self):
        self.client = OpenAI(api_key=setting.OPENAI_API_KEY, base_url="https://api.deepseek.com")
        self.pre_prompt = """Ты - советник по эклогии. К тебе обратился пользователь с вопросом. 
        Тебе надо на него ответить если это вопрос связана с экологией, в ином случае отвечай пользователю что его вопрос не связан с экологией и проси его задать вопрос про экологию.
        Не используй разметку для текста, пиши только предложениями будто бы ты настоящий человек.
        """

    def generate_comment(self, quest):
        prompt = f"{self.pre_prompt}\nВопрос пользователя: {quest}"

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt},
            ],
            stream=False,
            temperature=1
        )

        return response.choices[0].message.content.strip()
