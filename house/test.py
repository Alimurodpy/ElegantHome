import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/control/sketch",
    headers={
        "authorization": f"Bearer sk-KT6YnUm02bJA19UGvHApiTM41TtnQtOsrZ9ADbE25HhRGxO2",
        "accept": "image/*"
    },
    files={
        "image": open("C:/Users/victus/Desktop/Screenshots/test.png", "rb")
    },
    data={
        "prompt": "a medieval castle on a hill",
        "control_strength": 0.7,
        "output_format": "webp"
    },
)

if response.status_code == 200:
    with open("./castle.webp", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))