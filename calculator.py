def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate():
    print("=== Team Calculator 1.0 ===")
    print("Addition: 5 + 3 =", add(5, 3))
    print("Subtraction: 5 - 3 =", subtract(5, 3))
    print("Multiplication: 5 * 3 =", multiply(5,3))

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0: return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    calculate()

