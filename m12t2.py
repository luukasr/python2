import requests

# OpenWeatherMap API:n URL ja API-avain
API_KEY = 'YOUR_API_KEY'  # Aseta tähän oma API-avaimesi
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def hae_saa(paikkakunta):
    # Parametrit API-pyynnölle
    params = {
        'q': paikkakunta,
        'appid': API_KEY,
        'units': 'metric'  # Käytetään Celsius-asteita
    }

    # Tehdään pyyntö OpenWeatherMap API:lle
    response = requests.get(BASE_URL, params=params)

    # Tarkistetaan, että pyyntö onnistui
    if response.status_code == 200:
        data = response.json()

        # Haetaan säätilan ja lämpötilan tiedot
        säätila = data['weather'][0]['description']
        lämpötila = data['main']['temp']

        return säätila, lämpötila
    else:
        return None, None


if __name__ == "__main__":
    paikkakunta = input("Anna paikkakunnan nimi: ")

    säätila, lämpötila = hae_saa(paikkakunta)

    if säätila is not None:
        print(f"Säätilanne paikkakunnalla {paikkakunta}: {säätila}")
        print(f"Lämpötila: {lämpötila} °C")
    else:
        print("Säätietoja ei löytynyt tälle paikkakunnalle.")
