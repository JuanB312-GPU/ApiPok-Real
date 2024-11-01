from flask import Flask, jsonify, request
import requests as rq
# Librería que obtiene las últimas tasas de intercambio de divisas internacionales.
import yfinance as yf

# Realizan las consultas a la API pública elegida (pokemon e item), y devuelve la data en formato JSON.
def queri_pokemon(pokemon_name):

    pokemon_data = rq.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/')

    return pokemon_data

def queri_item(item_name):

    item_data = rq.get(f'https://pokeapi.co/api/v2/item/{item_name}/')

    return item_data

# Código que implementa la conversión del Yen a tres monedas diferentes.
def yen_conversion(yen_price, exchangeR):

    if exchangeR == "COP":
        currency_pair = "COPJPY=X"  # Peso colombiano.
    elif exchangeR == "EUR":
        currency_pair = "EURJPY=X"  # Euro. 
    elif exchangeR == "USD":
        currency_pair = "JPY=X"     # Dólar Estado Unidense.
    else:
        return "Error: Unsupported currency."

    # Obtiene la tasa de cambio
    data = yf.download(currency_pair, period="1d", interval="1d")
    if data.empty:
        print("Error: No data retrieved.")
        return None  
    print(data)
    if not data.empty:
        if exchangeR == "COP":
            rate =  data[('Close', currency_pair)][-1] 
            new_amount = (yen_price * rate)*1000
        elif exchangeR == "EUR":
            rate =  data[('Close', currency_pair)][-1] 
            new_amount = yen_price / rate
        elif exchangeR == "USD":
            rate = data[('Close', currency_pair)][-1] 
            new_amount = yen_price / rate
        return new_amount
    else:
        return "Error: Could not retrieve exchange rate."

# Función que desglosa la conversión del precio del item, (a consideración de ser ampliada).
def item_price_scaled(item_data):

    return {
            "item": item_data['name'],
            "price(Yen)": item_data['cost'],
            "price(USD)": yen_conversion(item_data['cost'],'USD'),
            "price(COP)": yen_conversion(item_data['cost'],'COP'),
            "price(Euro)": yen_conversion(item_data['cost'],'EUR')
        }


def scaled_weight(pokemon_data):

    # Los datos originales estan en decímetros para altura y en hectogramos para peso.
    # Se deben realizar las conversiones a metros y kilogramos respectivas.
    height = pokemon_data['height']/10 
    weight = pokemon_data['weight']/10

    # Se aplica la fórmula del índice de masa corporal.
    bmi = weight/(height**2)

    # Evalúa la condición de acuerdo al valor del BMI.
    if bmi < 18.5:
        condition = "Underweight"
    elif 18.5 <= bmi < 24.9:
        condition = "Normal weight"
    elif 25.0 <= bmi < 29.9:
        condition = "Overweight"
    elif 30.0 <= bmi < 34.9:
        condition = "Obesity Class I (Moderate)"
    elif 35.0 <= bmi < 39.9:
        condition = "Obesity Class II (Severe)"
    else:
        condition = "Obesity Class III (Morbid)"

    return {
            "pokemon": pokemon_data['name'],
            "height(m)": height,
            "wieght(kg)": weight,
            "Body mass index": bmi,
            "Condition": condition
        }

# Función encargada de estandarizar la verificación de datos, y errores comunes.
def queri_validation(mode, element):

    # Verificar si la entrada está vacía
    if not str(element).strip():  # Verifica que no esté vacío o lleno de espacios
        return jsonify({"error": "The item element is empty."}), 400

    try:
        if mode == 0 or mode == 2:
            response = queri_pokemon(element)
        elif mode == 1 or mode == 3:
            response = queri_item(element)
        
        # Verificar que la solicitud fue exitosa
        if response.status_code == 200:

            if mode == 0:
                return jsonify(response.json())
            elif mode == 1:
                return jsonify(response.json())
            elif mode == 2:
                return jsonify(scaled_weight(response.json()))
            elif mode == 3:
                return jsonify(item_price_scaled(response.json()))
            
        else:
            # Responder con un mensaje de error y el código de estado de la API externa
            return jsonify({
                "error": f"External API return {response.status_code}, element not found."
            }), response.status_code
    except rq.exceptions.JSONDecodeError:
        # Responder en caso de que el JSON no sea válido
        return jsonify({
            "error": "External API response, it is not in JSON format."
        }), 500

# EndPoints, se crearon dos para operaciones Get, otros dos para operaciones Post.
app = Flask(__name__)

@app.route('/pokemon/<string:pokemon_name>', methods = ['GET'])
def getPokemon(pokemon_name):

    return queri_validation(0, pokemon_name)

@app.route('/item/<string:item_name>', methods = ['GET'])
def getItem(item_name):

    return queri_validation(1, item_name)

@app.route('/weight_pokemon', methods = ['POST'])
def weightIbm():

    return queri_validation(2, request.json['name'])

@app.route('/price_item', methods = ['POST'])
def priceConversion():

    return queri_validation(3, request.json['name'])


    





