#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'


@app.route("/count/<int:number>")
def count(number):
    i = 0
    print = ""
    for i in range(number):
        print += str(i) + "\n"
    return print

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, num2, operation):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1-num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            return "Error: Cant divide by 0"
        else:
            return str(num1/num2)
    elif operation == 'div':
        if num2 == 0:
            return "Error: Cant divide by 0"
        else:
            return str(num1/num2)
    elif operation == '%':
        if num2 == 0:
            return "Error: Cant divide by 0"
        else:
            return str(num1%num2)
    else:
        print('enter valid operation')
        


if __name__ == '__main__':
    app.run(port=5555, debug=True)
