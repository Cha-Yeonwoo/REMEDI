import requests

url = "https://api.d-id.com/talks/tlk_kjYVyRrMnz7IMBrLTbMCN"

headers = {
    "accept": "application/json",
    "authorization": "Basic Yy5raXR0eTAzMDcwOEBnbWFpbC5jb20:0w-ldp-Ca9p83E89hM3B-"
}

response = requests.get(url, headers=headers)

print(response.text)