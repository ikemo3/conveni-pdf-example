import requests


def fetch(name) -> str:
    response = requests.get(f"http://terrible-api:8001/IF01/{name}")
    return response.content.decode("shift_jis")
