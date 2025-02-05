def process_string(s: str) -> tuple:
    vowels = "аеёиоуыэюяaeiou"
    consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
    
    vowels_in_s = sorted([ch for ch in s.lower() if ch in vowels])
    consonants_in_s = sorted([ch for ch in s.lower() if ch in consonants])
    
    return ("".join(vowels_in_s), len(vowels_in_s), "".join(consonants_in_s))

input_str = "Привіт, як справи?"
result = process_string(input_str)
print(result)
