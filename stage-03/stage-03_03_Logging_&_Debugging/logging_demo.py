import logging


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def divide(a, b):
    logging.info(f"Dividing {a} by {b}")

    if b == 0:
        logging.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero")

    result = a / b

    logging.info(f"Result: {result}")

    return result


logging.info("Application started")

try:
    divide(10, 2)
    divide(10, 0)

except ValueError as error:
    logging.exception("Operation failed")