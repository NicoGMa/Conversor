import requests

def obtener_tasa(moneda_origen):
    url = f"https://api.exchangerate-api.com/v4/latest/{moneda_origen}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error obteniendo la cotización.")
        return None
    
    return response.json()["rates"]

def convertir_moneda():
    print("=== Conversor CLI ===")

    from_currency = input("Ingrese la moneda origen (ej: USD, ARS, EUR): ").upper()
    to_currency = input("Ingrese la moneda destino (ej: USD, ARS, EUR): ").upper()
    amount = float(input("Ingrese el monto a convertir: "))

    rates = obtener_tasa(from_currency)
    if rates is None:
        return
    
    if to_currency not in rates:
        print("La moneda destino no existe en las tasas obtenidas.")
        return
    
    converted = amount * rates[to_currency]

    print("\n--- Resultado ---")
    print(f"{amount} {from_currency} = {converted} {to_currency}")
    print(f"Tasa utilizada: 1 {from_currency} = {rates[to_currency]} {to_currency}")

if __name__ == "__main__":
    convertir_moneda()