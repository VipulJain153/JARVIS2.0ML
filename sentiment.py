import os
import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "HI,how are you"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
