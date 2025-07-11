def add(a, b):
    return a + b

def user_input():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a, b

def main():
    a,b= user_input()
    result = add(a, b)
    print(f"The sum of {a} and {b} is {result}")

if __name__ == "__main__":
    main()
