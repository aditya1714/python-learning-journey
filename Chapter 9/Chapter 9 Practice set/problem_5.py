'''Repeat program 4 for a list of such words to be censored.'''

words = ["donkey", "the", "other"]
path = r"Chapter 9 Practice set/donkey.txt"

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    data = f.read()
for word in words:
    data = data.replace(word.lower(), "#" *len(word)).replace(word.capitalize(), "#####")

with open(path, "w", encoding="utf-8") as f:
    f.write(data)

print("✔ Replacement done!")