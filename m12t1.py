import requests

def hae_chuck_norris_vitsi():
    # Tehdään GET-pyyntö Chuck Norris API:in
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    # Tarkistetaan, että pyyntö onnistui
    if response.status_code == 200:
        # Saadaan vitsi JSON-muodossa
        data = response.json()
        return data['value']
    else:
        return "Vitsiä ei voitu hakea."

if __name__ == "__main__":
    # Hae ja tulosta satunnainen vitsi
    vitsi = hae_chuck_norris_vitsi()
    print(vitsi)
