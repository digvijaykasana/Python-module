class CalculatorError(Exception):
    """Custom exception class for Calculator errors."""
    pass

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise CalculatorError("Cannot divide by zero.")
        return x / y

    def power(self, x, y):
        return x ** y
