string = input("Digite uma string: ")

count = 0

for char in string:
    if char.lower() == 'a':
        count += 1

if count > 0:
    print(f"A letra 'a' aparece {count} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")