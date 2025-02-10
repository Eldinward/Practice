def analyze_string(input_string):
    vowels = "аеєєиіїїоуюяaeiouy"
    consonants = ""
    vowels_in_string = ""
    count_vowels = 0
    for char in input_string:
        if char.lower() in vowels:
            vowels_in_string += char.lower()
            count_vowels += 1
        elif char.isalpha():
            consonants += char.lower()
    
    vowels_in_string = ''.join(sorted(vowels_in_string))
    consonants = ''.join(sorted(consonants))
    
    return (vowels_in_string, count_vowels, consonants)

input_string = input("Введіть строку: ")
result = analyze_string(input_string)
print(result)
