import sys
import argparse
from pkg.calculator import Calculator
from pkg.render import render

def main():
    parser = argparse.ArgumentParser(description="A simple calculator application.")
    parser.add_argument("expression", nargs="*", help="The expression to evaluate (e.g., '3 + 5')")
    args = parser.parse_args()

    calculator = Calculator()

    if not args.expression:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('example: python main.py "3 + 5"')
        return

    expression = " ".join(args.expression)
    try:
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        print(to_print)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
