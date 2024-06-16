import requests

url = "https://api.d-id.com/talks"

payload = {
    "script": {
        "type": "audio",
        "subtitles": False,
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        },
        "audio_url": "s3://d-id-audios-prod/google-oauth2|105896968890442581577/GBvG2vEjPpX3gB0cd5Bhp/sampleaudio.wav"
    },
    "config": {
        "fluent": False,
        "pad_audio": "0.0"
    },
    "source_url": "s3://d-id-images-prod/google-oauth2|105896968890442581577/img_gfgjgWNyFKCB80NjRTiif/sampleimg.png"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic Yy5raXR0eTAzMDcwOEBnbWFpbC5jb20:0w-ldp-Ca9p83E89hM3B-"
}

response = requests.post(url, json=payload, headers=headers)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")