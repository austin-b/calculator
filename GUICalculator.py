import Calculator
from tkinter import *

def press_number(num):
    calc.add_number(num)
    equation.set(calc.get_expression())

def press_operator(oper):
    calc.add_operator(oper)
    equation.set(calc.get_expression())

def clear():
    calc.clear_expression()
    equation.set('0')

def enter():
    try:
        result = calc.evaluate()
    except ZeroDivisionError:
        calc.clear_expression()
        result="Undefined"
    equation.set(result)

calc = Calculator.Calculator()

root = Tk()
root.configure(background="light blue")
root.title("Calculator")
root.geometry("350x150")

equation = StringVar()
expression_field = Entry(root,textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)

equation.set("0")

# for some reason, lambda makes them wait to be pressed before calling function
button1 = Button(root, text=' 1 ', fg='black', bg='red', height=1, width=7, command=lambda: press_number(1))
button1.grid(row=2, column=0)

button2 = Button(root, text=' 2 ', fg='black', bg='red', height=1, width=7, command=lambda: press_number(2))
button2.grid(row=2, column=1)

button3 = Button(root, text=' 3 ', fg='black', bg='red', height=1, width=7, command=lambda: press_number(3))
button3.grid(row=2, column=2)

button4 = Button(root, text=' 4 ', fg='black', bg='red', height=1, width=7, command=lambda: press_number(4))
button4.grid(row=3, column=0)

button5 = Button(root, text=' 5 ', fg='black', bg='red', height=1, width=7, command=lambda: press_number(5))
button5.grid(row=3, column=1)

button6 = Button(root, text=' 6 ', fg='black', bg='red', height=1, width=7, command=lambda: press_number(6))
button6.grid(row=3, column=2)

button7 = Button(root, text=' 7 ', fg='black', bg='red', height=1, width=7, command=lambda: press_number(7))
button7.grid(row=4, column=0)

button8 = Button(root, text=' 8 ', fg='black', bg='red', height=1, width=7, command=lambda: press_number(8))
button8.grid(row=4, column=1)

button9 = Button(root, text=' 9 ', fg='black', bg='red', height=1, width=7, command=lambda: press_number(9))
button9.grid(row=4, column=2)

button0 = Button(root, text=' 0 ', fg='black', bg='red', height=1, width=7, command=lambda: press_number(0))
button0.grid(row=5, column=0)

buttonEnter = Button(root, text=' = ', fg='black', bg='red', height=1, width=7, command=lambda: enter())
buttonEnter.grid(row=5, column=1)

buttonClear = Button(root, text=' C ', fg='black', bg='red', height=1, width=7, command=lambda: clear())
buttonClear.grid(row=5, column=2)

buttonPlus = Button(root, text=' + ', fg='black', bg='red', height=1, width=7, command=lambda: press_operator('+'))
buttonPlus.grid(row=2, column=3)

buttonMinus = Button(root, text=' - ', fg='black', bg='red', height=1, width=7, command=lambda: press_operator('-'))
buttonMinus.grid(row=3, column=3)

buttonMultiply = Button(root, text=' * ', fg='black', bg='red', height=1, width=7, command=lambda: press_operator('*'))
buttonMultiply.grid(row=4, column=3)

buttonDivide = Button(root, text=' / ', fg='black', bg='red', height=1, width=7, command=lambda: press_operator('/'))
buttonDivide.grid(row=5, column=3)

root.mainloop()
