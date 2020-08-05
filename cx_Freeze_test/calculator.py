import argparse

parser = argparse.ArgumentParser(description="calculator with 4 operations & 2 numbers")
parser.add_argument("--operation", "-op", default="plus", dest="operation", type=str)
parser.add_argument("num1", type=float)
parser.add_argument("num2", type=float)

args = parser.parse_args()
print(args)

calculator_options = {
    "plus" : lambda a, b: a + b,
    "minus" : lambda a, b: a - b,
    "multiply" : lambda a, b: a * b,
    "divide" : lambda a, b: a / b
}

print(args.operation)
print(args.operation in calculator_options.keys())

if args.operation in calculator_options.keys():
    print(calculator_options[args.operation](args.num1, args.num2))
else:
    raise ValueError("The operations that you can give to the '--operation'/'-op' variable are | plus | minus | multiply | divide |")
