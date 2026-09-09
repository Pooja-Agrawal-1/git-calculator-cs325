def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate():
    print("Welcome to the Pair Calculator!")
    print("Addition: 5 + 3 =", add(5, 3))
    print("Subtraction: 5 - 3 =", subtract(5, 3))

if __name__ == "__main__":
    calculate()