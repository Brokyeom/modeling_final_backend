import gradio as gr
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(input_text):
    temp = 25
    messages = [
        { "role": "system", "content": "오늘 기온에 맞춰 오늘 작물에게 맞는 행동을 추천해야 합니다. 사용자가 특정 작물과 현재 기온에 대한 정보를 제공하면, 해당 기온에서의 작물 관리에 대한 오늘의 관리법을 제공해야 합니다. 답변은 다음과 같은 형식을 따라야 합니다: '{temp}도에서는 {input}에게 ~~ 한 온도입니다. 다음과 같이 행동하는 것을 추천합니다: 1. ~~ 2. ~~ 3. ~~'"  },
        {"role": "assistant", "content": f'{temp}도에서는 {input_text}에게 ~~ 한 온도입니다. 다음과 같이 행동하는 것을 추천합니다: 1. ~~ 2. ~~ 3. ~~'},
        {"role": "assistant", "content": f'{temp}도에서는 {input_text}에게 ~~ 한 온도입니다. 다음과 같이 행동하는 것을 추천합니다: 1. ~~ 2. ~~ 3. ~~'},
        {"role": "assistant", "content": f'{temp}도에서는 {input_text}에게 ~~ 한 온도입니다. 다음과 같이 행동하는 것을 추천합니다: 1. ~~ 2. ~~ 3. ~~'},
        {"role": "assistant", "content": f'{temp}도에서는 {input_text}에게 ~~ 한 온도입니다. 다음과 같이 행동하는 것을 추천합니다: 1. ~~ 2. ~~ 3. ~~'},
        {"role": "assistant", "content": f'{temp}도에서는 {input_text}에게 ~~ 한 온도입니다. 다음과 같이 행동하는 것을 추천합니다: 1. ~~ 2. ~~ 3. ~~'},
        {"role": "user", "content": f'나는 {input_text} 를 기르고 있어. 오늘 기온은 섭씨{temp}도야 오늘 {input_text}가 잘 자라게 하는 방법에는 무엇이 있을까?'}
    ]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.1
    )

    assistant_content = completion.choices[0].message['content'].strip()

    return assistant_content

iface = gr.Interface(
    fn=chat_with_gpt, 
    inputs="text",
    outputs="text", 
    title="AgriChat",
)

iface.launch()

