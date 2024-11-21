from flask import Flask, jsonify
import json

app = Flask(__name__)


# Ladataan lentokenttätiedot JSON-tiedostosta
def hae_kentta_tiedot():
    with open("kentat.json", "r") as f:
        return json.load(f)


# API-piste, joka palauttaa lentokentän tiedot ICAO-koodilla
@app.route('/kenttä/<icao>', methods=['GET'])
def kentta(icao):
    kentat = hae_kentta_tiedot()

    # Etsitään kenttä annetuilla ICAO-koodilla
    kentta_data = kentat.get(icao.upper())  # Muutetaan ICAO-koodi isoksi
    if kentta_data:
        # Palautetaan kentän tiedot JSON-muodossa
        return jsonify({
            "ICAO": icao.upper(),
            "Name": kentta_data["Name"],
            "Municipality": kentta_data["Municipality"]
        })
    else:
        # Jos ICAO-koodia ei löydy, palautetaan virheilmoitus
        return jsonify({"error": "Kenttää ei löytynyt"}), 404


if __name__ == "__main__":
    # Käynnistetään Flask-sovellus
    app.run(debug=True, host="127.0.0.1", port=3000)
