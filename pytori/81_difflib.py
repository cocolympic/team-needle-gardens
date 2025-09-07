import difflib

words = ["apple", "banana", "cherry"]
target = "appel"

matches = difflib.get_close_matches(target, words)
print(matches)