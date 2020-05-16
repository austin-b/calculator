'''
Started/finished 14 May 2020.

Simple calculator backend logic.
'''

# Class for first class use of math operators
class Operator:
    def __init__(self, s, f):
        self.string_to_print = s
        self.operating_function = f
    def __str__(self):
        return self.string_to_print
    def evaluate(self, a, b):
        return self.operating_function(a,b)

# Calculator logic class
class Calculator:
    def __init__(self):
        self.expression = []

    def add_number(self, number):
        try:
            assert isinstance(number, int) or isinstance(number, float)
            if len(self.expression) == 0:
                self.expression.append(number)
            elif type(self.expression[-1]) == int:
                new_number = int(str(self.expression[-1])+str(number))
                self.expression[-1] = new_number
            elif type(self.expression[-1]) == float:
                return
            else:
                self.expression.append(number)
        except AssertionError:
            raise TypeError("Input must be an integer or float.")

    def add_operator(self, operator):
        if len(self.expression) == 0 or type(self.expression[-1]) == Operator:
            return

        if operator == '+':
            self.expression.append(Operator(operator, lambda a,b : a+b))
        elif operator == '-':
            self.expression.append(Operator(operator, lambda a,b : a-b))
        elif operator == '*':
            self.expression.append(Operator(operator, lambda a,b : a*b))
        elif operator == '/':
            self.expression.append(Operator(operator, lambda a,b : a/b))
        else:
            raise ValueError("Invalid operator.")

    def __clean_expression(self):
        new_expression = []
        temp = None
        for i in self.expression:
            if len(new_expression) == 0:
                new_expression.append(i)
            elif type(i) == Operator:
                temp = i
            else:
                new_expression.append(i)
                new_expression.append(temp)
        return new_expression

    def __evaluator(self, expression):
        current = expression.pop()
        if type(current) == Operator:
            next_number = expression.pop()
            return current.evaluate(self.__evaluator(expression), next_number)
        else:
            return current

    def evaluate(self):
        if len(self.expression) == 0:
            result = 0
        else:
            expression = self.__clean_expression()
            result = self.__evaluator(expression)
        self.clear_expression()
        self.add_number(result)
        return result

    def clear_expression(self):
        self.expression = []

    def get_expression(self):
        str_expression = ""
        for i in self.expression:
            str_expression += str(i)
        return str_expression

    def __str__(self):
        return self.get_expression()

def test():
    calc = Calculator()
    calc.add_operator('+')
    calc.add_number(-4)
    calc.add_operator('+')
    calc.add_number(3)
    print("Test expression = " + calc.get_expression())
    print("Test expression = " + str(calc))
    calc.add_number(6)
    print("Test expression (adding second number) = " + calc.get_expression())
    calc.add_operator('/')
    print("Test expression = " + calc.get_expression())
    calc.add_operator('*')
    print("Test expression (second *) = " + calc.get_expression())
    calc.add_number(6)
    print("Test expression = " + calc.get_expression())
    result = calc.evaluate()
    print("Result: " + str(result))
    print("Test expression = " + calc.get_expression())

if __name__ == "__main__":
    test()
