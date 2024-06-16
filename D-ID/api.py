import requests

url = "https://api.d-id.com/audios"

files = { "audio": ("sampleaudio.wav", open("/mnt/disk1/ivymm02/D-ID/myvoice.wav", "rb"), "audio/wav") }
headers = {
    "accept": "application/json",
    "authorization": "Basic Yy5raXR0eTAzMDcwOEBnbWFpbC5jb20:cmsPOyJpDuQkfIU8aksoR"
}

voice_response = requests.post(url, files=files, headers=headers)

voice_url = voice_response.json().get('url')
# print(voice_response.text)
# print('VOICE:', voice_url)

url = "https://api.d-id.com/images"

files = { "image": ("sampleimg.png", open("/mnt/disk1/ivymm02/jobs_toon.png", "rb"), "image/png") }
headers = {
    "accept": "application/json",
    "authorization": "Basic Yy5raXR0eTAzMDcwOEBnbWFpbC5jb20:cmsPOyJpDuQkfIU8aksoR"
}

img_response = requests.post(url, files=files, headers=headers)
img_url =  img_response.json().get('url')

# print(img_response.text)
# print('Image:', img_url)

url = "https://api.d-id.com/talks"

payload = {
    "script": {
        "type": "audio",
        "subtitles": 'false',
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        },
        "audio_url": voice_url
    },
    "config": {
        "fluent": 'false',
        "pad_audio": "0.0"
    },
    "source_url": img_url
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic Yy5raXR0eTAzMDcwOEBnbWFpbC5jb20:cmsPOyJpDuQkfIU8aksoR"
}

response = requests.post(url, json=payload, headers=headers)

# print(response.text)

video_id = str(response.json()['id'])
print(video_id)
with open('id.txt', 'w') as f:
    f.write(video_id)

# url = "https://api.d-id.com/talks/"+video_id
# print(url)
# final_headers = {
#     "accept": "application/json",
#     "authorization": "Basic Yy5raXR0eTAzMDcwOEBnbWFpbC5jb20:cmsPOyJpDuQkfIU8aksoR"
# }

# final_response = requests.get(str(url), headers=final_headers)

# print(final_response.text)


