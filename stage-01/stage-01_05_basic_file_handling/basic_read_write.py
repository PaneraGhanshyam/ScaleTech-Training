
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Python File Handling\n")
    file.write("Reading and Writing Files\n")
    file.write("ScaleTech Training\n")


with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("File Content:")
print(content)


with open("data.txt", "a", encoding="utf-8") as file:
    file.write("New line added using append mode.\n")