
import openai
openai.api_key = "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"

import tweepy

# Autentica la aplicación de Twitter utilizando las claves de acceso
auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAACFelAEAAAAAazOrc9K%2BbvpSZ58ggsacVWOhGRQ%3DWUB8Ow6Z2lAJKoQkuq4qLG0poqEG8jtY57O1eQu1dakU5bb7EX")


api = tweepy.API(auth)

# Recupera las tendencias más recientes de Twitter
trends = api.get_place_trends(2972)
for obj in trends:
    for trend in obj["trends"]:

        print(trend["name"])

#trend_list = trends[0]["trends"]
#trends = [trend["name"] for trend in trend_list]
#print(f"Las tendencias más recientes en Twitter son: {}")

# Utiliza ChatGPT para escribir un artículo sobre las tenden
def generate_text(prompt, model):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

# Utiliza ChatGPT para escribir un artículo sobre las tendencias más recientes en Twitter
article = ""
for trend in trends:
    prompt = f"Escribe un artículo sobre la tendencia en Twitter '{trend}'"
    model = "text-davinci-002"
    article += generate_text(prompt, model)

# Imprime el artículo generado por ChatGPT
print(article)
