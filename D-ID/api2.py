import requests
import sys
import time

f = open('id.txt', 'r')
video_id = str(f.readlines()[0])
print("ID", video_id)
f.close()
time.sleep(5)
url = "https://api.d-id.com/talks/"+str(video_id)
print(url)
final_headers = {
    "accept": "application/json",
    "authorization": "Basic Yy5raXR0eTAzMDcwOEBnbWFpbC5jb20:cmsPOyJpDuQkfIU8aksoR"
}

final_response = requests.get(str(url), headers=final_headers)

print(final_response.text)


