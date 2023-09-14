from flask import Flask, request, jsonify
from web import validate_password
#python app.py


app = Flask(__name__)

@app.route('/validar-senha', methods=['POST'])
def validar_senha():
    data = request.get_json()
    password = data.get('password')
    name = data.get('name')
    lastname = data.get('lastname')
    cpf = data.get('cpf')

    if password:
        results, entropy_bits, compromised = validate_password(password, name, lastname, cpf)

        response = {
            'result': results,
            'compromised': compromised,
            'entropy_bits': entropy_bits
           
        }
    else:
        response = {
            'error': 'Por favor, forneça uma senha.'
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
