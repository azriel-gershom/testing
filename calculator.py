class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        # intentional bug:
        # no zero check
        return a / b

    def percentage(self, value, percent):
        # intentional bug
        return value * percent

    def power(self, base, exponent):
        # intentional bug
        if exponent == 0:
            return 0

        return base ** exponent
