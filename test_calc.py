from calc import add


# Write your tests below.
# Use assert statements to check that calc returns the correct result.
# All test functions must start with test_ to be discovered by pytest or similar frameworks.
# We have included a single starter test.
# Add more test_* functions as you work through each new requirement.
# Example:

def test_example_string_returns_zero():
    assert add("") == 0  # uncomment to test
    pass
def test_single_number_returns_itself():
    assert add("5") == 5
def test_two_numbers_return_sum():
    assert add("1,2") == 3
def test_newline_delimiters_are_allowed():
    assert add("1\n2,3") == 6
def test_multiple_numbers_return_sum():
    assert add("1,2,3,4,5") == 15
def test_custom_delimiters():
    assert add("//;\n1;2") == 3
def test_negatives():
    assert add("1,-1,3") == "negatives not allowed: -1"
