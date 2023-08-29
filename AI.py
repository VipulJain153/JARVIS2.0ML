import openai,datetime
from nlp import speak
openai.api_key = ""
def ai(query):
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=query,
  temperature=2,
  max_tokens=2048,
  top_p=1,
  best_of=20,
  frequency_penalty=0,
  presence_penalty=0
)
    with open(datetime.datetime.now().strftime('Prompt %Y-%m-%d %H:%M:%S'),'w') as f:f.write(response)
def chat(query,chatStr):
    chatStr+=f'\n\nUser: {query}\n Jarvis: '
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=chatStr,
  temperature=2,
  max_tokens=2048,
  top_p=1,
  best_of=20,
  frequency_penalty=0,
  presence_penalty=0
)
    speak(response.get("choices")[0].get("text"))
    chatStr+=response.get("choices")[0].get("text")
    print(f'\nUser: {query}\n Jarvis: {response.get("choices")[0].get("text")}')
    return chatStr
