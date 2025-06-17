""" Edit the function below to implement the String Calculator TDD Kata """

def add(numbers):
    if numbers == "":
        return 0
    parts = numbers.split(",")
    nums = [int(p) for p in parts if p.strip() != ""]
    return sum(nums)
