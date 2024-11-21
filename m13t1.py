from flask import Flask, jsonify

app = Flask(__name__)

# Funktio, joka tarkistaa, onko luku alkuluku
def on_alkuluku(luku):
    if luku <= 1:
        return False
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            return False
    return True

# API-piste, joka tarkistaa, onko luku alkuluku
@app.route('/alkuluku/<int:luku>', methods=['GET'])
def tarkista_alkuluku(luku):
    alkuluku_tulos = on_alkuluku(luku)
    return jsonify({"Number": luku, "isPrime": alkuluku_tulos})

if __name__ == "__main__":
    # Ajetaan Flask-sovellus paikallisessa kehityspalvelimessa
    app.run(debug=True, host="127.0.0.1", port=3000)
