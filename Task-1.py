def analyze_string(input_string):
    vowels = "аеєиіїоуюяaeiouy"
    vowels_in_string = []
    consonants = []
    count_vowels = 0

    for char in input_string:
        if char.lower() in vowels:
            vowels_in_string.append(char.lower())
            count_vowels += 1
        elif char.isalpha():
            consonants.append(char.lower())

    return (''.join(sorted(vowels_in_string)), count_vowels, ''.join(sorted(consonants)))

input_string = input("Введіть строку: ")
result = analyze_string(input_string)
print(result)
