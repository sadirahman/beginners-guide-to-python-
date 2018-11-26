number = [1, 2, 6, 7]

print("here are numbers that are still available")

for n in range(1, 20):
    if n in number:
        continue
    print(n)