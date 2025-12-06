'''A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file. '''

word = "donkey"
path = r"Chapter 9 Practice set/donkey.txt"

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    data = f.read()

dataNew = data.replace(word.lower(), "#####").replace(word.capitalize(), "#####")

with open(path, "w", encoding="utf-8") as f:
    f.write(dataNew)

print("✔ Replacement done!")
