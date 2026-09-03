import threading
import time


def download_file(name):
    print(f"{name} started")

    time.sleep(2)

    print(f"{name} finished")


threads = []

for i in range(3):
    thread = threading.Thread(
        target=download_file,
        args=(f"File {i + 1}",)
    )

    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print("All downloads completed")