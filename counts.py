def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
"""    
Note: Code above is same as this code below

def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
"""

# assert count_upper_case("") == 1, "Failed test: Empty string should return 0"
assert count_upper_case("") == 0, "Empty string should return 0"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case("12345") == 0, "Numbers"
assert count_upper_case("      ") == 0, "Spaces"
assert count_upper_case("ABCDEF") == 6, "6 upper case"
assert count_upper_case("abcdef") == 0, "6 lowercase"
assert count_upper_case("a c8*f") == 0, "Mixed characters no uppercase"
assert count_upper_case("A c8*Gf") == 2, "Mixed characters with 2 uppercase"

print("All the tests passed")