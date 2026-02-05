todo = [
    " Get quarters.",
    " Do laundry.",
    " Take a walk.",
    " Get a haircut.",
    " Make some tea.",
    " Complete Lists chapter.",
    " Call mom.",
    " Watch My Hero Academia."
]

print("First item:", todo[0])
print("Second item:", todo[1])
print("\nThird, fourth, and fifth items:")
print(todo[2:5])

print("\nTrying to access index 9:")
try:
    print(todo[9])
except IndexError as e:
    print(f"IndexError: {e}")