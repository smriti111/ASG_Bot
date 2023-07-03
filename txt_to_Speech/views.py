from django.shortcuts import render
from django.http import HttpResponse
import openai
import requests

#openai
openai.api_key = "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"

# Create your views here.
def prompt(request):
    if request.method=='POST':
        USER_PROMPT = request.POST.get("user_prompt")
        print("prompt-value - ",USER_PROMPT)
        message = USER_PROMPT 
        reply = chat_with_model(message)
        txt = reply
        message = audio(txt)

        return render(request,"audio.html",{"message":message})
    else:
        return render(request,"prompt.html")



def chat_with_model(message):
    context = "You are chatting with a bot which acts and responds like Ashneer Grover from India"
    prompt = f"Chat:\n{context}\nUser: {message}\n"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )

    reply = response.choices[0].text.strip()
    print("answer from ashneer ",reply)
    return reply




def audio(txt):
    # global USER_PROMPT
    # message=USER_PROMPT
    # print("the query from user is . ",message)
    # reply = chat_with_model(message)
    text= txt
    colon_index = text.find(":")
    if colon_index != -1:
        text_without_bot = text[colon_index + 2:]
        clone_txt= text_without_bot
    else:
        clone_txt= text
  

    # Voice Clone code:--->

    Eleven_Labs_API_KEY="5395c1b9978581680cd3250f76387cd4"
    Ashneer_Voice_Id = "VbnAIBlibhaxtxNtayxQ"

    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/VbnAIBlibhaxtxNtayxQ"

    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": Eleven_Labs_API_KEY
    }

    data = {
    "text": clone_txt,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.75,
        "similarity_boost": 0.95
    }
    }


    response = requests.post(url, json=data, headers=headers)

    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    print("inside the audio function ",response)

    message="Audio has been successfully downloaded"

    return message
