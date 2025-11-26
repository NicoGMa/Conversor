from flask import Flask, request, jsonify
import requests #permite llamar APIs externas (GET, POST, etc.).


app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    return {"message": "pong"}, 200

@app.route("/status", methods=["GET"])
def status():
    return {"status": "ok"}, 200

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()   # recibís el JSON del cliente
    return {"echo": data["message"]}, 200


@app.route("/convertir", methods=["GET", "POST"])
def convertir():
        # ---------------------------
    # MODO GET (desde navegador)
    # ---------------------------
    if request.method == "GET":
        amount = request.args.get("amount", type=float)
        from_currency = request.args.get("from")
        to_currency = request.args.get("to")

    # ---------------------------
    # MODO POST (JSON)
    # ---------------------------
    else:
        data = request.get_json()
        amount = data["amount"]
        from_currency = data["from"]
        to_currency = data["to"]

     # Busca API cotizacion externa
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "No se pudo obtener la cotización"}), 500

    rates = response.json()["rates"]

    if to_currency not in rates:
        return jsonify({"error": "Moneda destino no encontrada"}), 400
    
    # 2. Calcular conversión real
    converted = amount * rates[to_currency]

    #pruebo con curl -X POST http://127.0.0.1:5000/convertir -H "Content-Type: application/json" -d "{\"amount\": 10, \"from\": \"USD\", \"to\": \"ARS\"}"

    return jsonify({
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted": converted,
        "rate": rates[to_currency]
    }),200
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

