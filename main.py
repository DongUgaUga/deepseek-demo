from openai import OpenAI
import time
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("환경변수 'DEEPSEEK_API_KEY'가 설정되지 않았습니다.")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

system_message = {"role": "system", "content": "너는 이제부터 수화를 번역할 거야. 내가 단어들을 던져주면 그걸 자연스러운 하나의 문장으로 만들어줘. 부가적인 설명은 하지 말고, 오로지 하나의 문장만 출력해."}

while True:
    user_input = input()
    if user_input == "" : break

    messages = [system_message, {"role": "user", "content": user_input}]

    start_time = time.time()
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        max_tokens=1024,
        temperature=0
    )

    content = response.choices[0].message.content
    end_time = time.time()
    response_time = end_time - start_time

    print(f"\"{content}\", 응답 속도: {response_time:.2f} (sec)")