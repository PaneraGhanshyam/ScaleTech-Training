from multiprocessing import Process
import time


def calculate(name):
    print(f"{name} started")

    total = 0

    for i in range(10_000_000):
        total += i

    print(f"{name} finished")


processes = []

for i in range(3):
    process = Process(
        target=calculate,
        args=(f"Process {i + 1}",)
    )

    processes.append(process)
    process.start()


for process in processes:
    process.join()

print("All calculations completed")