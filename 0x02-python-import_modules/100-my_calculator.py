#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    if len(argv) != 4:
        print("usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(argv[1])
    b = int(argv[3])
    operator = str(argv[2])

    if operator == "+":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
