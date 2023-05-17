import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

temp = 20

input_plant = input("확인하고자 하는 작물을 입력하세요 : ")

messages = [
    {"role": "assistant", "content": "반드시 다음과 같은 형식으로만 대답해줘. \n" +
                                      f"현재 기온은 {temp}도 입니다. \n" +
                                      f"{temp}도에서 {input_plant}의 최적 생육을 위해 아래와 같은 행동을 취하세요.\n"},
    {"role": "user", "content": input_plant}
]

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature= 0.2
)

assistant_content = completion.choices[0].message['content'].strip()

print('답변 : ', assistant_content)

