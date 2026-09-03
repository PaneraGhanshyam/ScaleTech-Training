import time


def timer(func):

    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print(f"Execution time: {end - start:.4f} seconds")

    return wrapper


@timer
def download_file():
    print("Downloading file...")

    time.sleep(2)

    print("Download complete")


download_file()