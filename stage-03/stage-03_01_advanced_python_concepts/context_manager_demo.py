class MyContext:

    def __enter__(self):
        print("Resource opened")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource closed")


with MyContext():
    print("Using resource")