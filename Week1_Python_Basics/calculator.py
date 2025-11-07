# Simple Calculator using class

class Calculator:
    def square(self, n): return n ** 2
    def cube(self, n): return n ** 3
    def sqrt(self, n): return n ** 0.5

calc = Calculator()
num = float(input("Enter a number: "))

print(f"Square: {calc.square(num)}")
print(f"Cube: {calc.cube(num)}")
print(f"Square Root: {calc.sqrt(num):.2f}")
