import openai
from openai import OpenAI


# OpenAI API 키 설정
openai.api_key = 'sk-proj-ALuUAoRTCEJjMbwJRm1LT3BlbkFJBzlMfCEzmUiQN1PKc6a5'

def send_message(message):
    try:
        client = OpenAI()
        client.api_key = 'sk-proj-ALuUAoRTCEJjMbwJRm1LT3BlbkFJBzlMfCEzmUiQN1PKc6a5'
        stream =  client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
            ]
            )
        return stream
    except Exception as e:
        print(f"An error occurred: {e}")

# 보낼 메시지
message = "AI 기술의 미래에 대해 설명해주세요."

# 함수 호출 및 결과 출력
result = send_message(message)
if result:
    print(result['choices'][0]['message']['content'])