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
