import openai
import time

openai.api_key = "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" # API KEY 를 넣어주세요

messages = [
{"role": "system", "content": "You are a helpful assistant."}
]

content = input()
start = time.time()
print("content : ", content)

messages.append({"role": "user", "content": content})

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages
)

chat_response = completion.choices[0].message.content
end = time.time()
sec = (end - start)
print(f'ChatGPT: {chat_response}')
print(round(sec, 4), "초")