import requests

url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"

headers = {
    'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com",
    'x-rapidapi-key': "3ab8be4998msh149217184c899e4p1ae6cbjsn6b408b58f652"
    }

API = 'https://api.mymemory.translated.net/get?q='

def translate_text(input_lang, output_lang, text):
    querystring = {"langpair": input_lang + "|" + output_lang, "q": text}

    response = requests.request("GET", url, headers=headers, params=querystring)
    #response = requests.get(API + text + '&langpair=' + input_lang + '|' + output_lang)
    return response