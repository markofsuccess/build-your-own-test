def count_upper_case(message):
    return sum([1 for c in message if c.ischaracter()])
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 0, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("%€&€%") == 5,"Special characters"

print("All the tests passed")