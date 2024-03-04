def generate_strings(n, vowels, valid_strings, current_string):
    if n == 1:
        for vowel in vowels:
            valid_strings.add(current_string + vowel)
    else:
        for vowel in vowels:
            if len(current_string) == 0 or vowels.index(vowel) > vowels.index(current_string[-1]):
                generate_strings(n-1, vowels, valid_strings, current_string + vowel)
def count_valid_strings(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    valid_strings = set()
    generate_strings(n, vowels, valid_strings, "")
    return len(valid_strings)
print(count_valid_strings(2))
print(count_valid_strings(33))  
print(count_valid_strings(-5))  
print(count_valid_strings(102)) 
