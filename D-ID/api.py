import requests
import time
import argparse

parser = argparse.ArgumentParser(description="D-ID API call")
parser.add_argument("--img", type=str, required=True, help="Input image")
parser.add_argument("--voice", type=str, required=True, help="Input speech")
args = parser.parse_args()

url = "https://api.d-id.com/audios"

# files = { "audio": ("sampleaudio.wav", open("/mnt/disk1/ivymm02/D-ID/myvoice.wav", "rb"), "audio/wav") }
files = { "audio": ("sampleaudio.wav", open(args.voice, "rb"), "audio/wav") }
headers = {
    "accept": "application/json",
    "authorization": "Basic Yy5raXR0eTAzMDcwOEBnbWFpbC5jb20:cmsPOyJpDuQkfIU8aksoR"
}

voice_response = requests.post(url, files=files, headers=headers)

voice_url = voice_response.json().get('url')

url = "https://api.d-id.com/images"

files = { "image": ("sampleimg.png", open(args.img, "rb"), "image/png") }
headers = {
    "accept": "application/json",
    "authorization": "Basic Yy5raXR0eTAzMDcwOEBnbWFpbC5jb20:cmsPOyJpDuQkfIU8aksoR"
}

img_response = requests.post(url, files=files, headers=headers)
img_url =  img_response.json().get('url')


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


video_id = str(response.json()['id'])

time.sleep(5)

url = "https://api.d-id.com/talks/"+video_id

final_headers = {
    "accept": "application/json",
    "authorization": "Basic Yy5raXR0eTAzMDcwOEBnbWFpbC5jb20:cmsPOyJpDuQkfIU8aksoR"
}

final_response = requests.get(str(url), headers=final_headers)

print(final_response.json()["result_url"])


