#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv
    length = len(argv)
    operator = "+-*/"
    op = False

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    for i in operator:
        if argv[2] == i:
            op = True
            break

    if op is False:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    operation = argv[2]
    b = int(argv[3])

    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = sub(a, b)
    elif operation == "*":
        result = mul(a, b)
    elif operation == "/":
        result = div(a, b)

    print("{} {} {} = {}".format(a, operation, b, result))
