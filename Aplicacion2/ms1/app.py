#!/usr/bin/python3.10

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Hola mundo desde el micro servicio'

@app.route('/enviar', methods = ['POST'])
def datos():
    a = request.data
    print(a)
    return "datos recibidos"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5555)