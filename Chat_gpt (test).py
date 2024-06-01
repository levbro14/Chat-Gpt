from g4f.client import Client #https://github.com/xtekky/gpt4free
import g4f #https://github.com/techwithanirudh/g4f

client = Client()
response = client.chat.completions.create(
    model=g4f.models.gpt_35_turbo,
    provider=g4f.Provider.Aichatos,
    messages=[{"role": "user", "content": "Привет"}],
)
print(response.choices[0].message.content)