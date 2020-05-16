import Calculator
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

calc = Calculator.Calculator()

@app.route('/calculator')
def calculator():
    return render_template('main.html')

def press_operator(button_pressed):
    try:
        if button_pressed == "plus":
            operator = "+"
        elif button_pressed == "minus":
            operator = "-"
        elif button_pressed == "multiply":
            operator = "*"
        elif button_pressed == "divide":
            operator = "/"
        calc.add_operator(operator)
        return calc.get_expression()
    except:
        return "error"

def press_enter():
    try:
        return calc.evaluate()
    except Exception as e:
        calc.clear_expression()
        return "undefined"

@app.route('/background_process')
def background_process():
    try:
        type = request.args.get('type', 'null')
        button_pressed = request.args.get('button','null')
        if type == "digit":
            calc.add_number(int(button_pressed))
            return jsonify(result=calc.get_expression())
        elif type == "enter":
            evaluated = press_enter()
            return jsonify(result=evaluated)
        elif type == "clear":
            calc.clear_expression()
            return jsonify(result=calc.get_expression())
        elif type == "operator":
            expression = press_operator(button_pressed)
            return jsonify(result=expression)
    except Exception as e:
        return str(e)
