from google import genai

client = genai.Client(api_key="AIzaSyCua-FU7PdQ7slNtfWaq43a9JTdbb2CLdo")

models = client.models.list()
for m in models:
    print(m.name)
