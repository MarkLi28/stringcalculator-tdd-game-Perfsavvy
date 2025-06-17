""" Edit the function below to implement the String Calculator TDD Kata """

def add(numbers):
    if numbers == "":
        return 0
    delimiter = ","

    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter = header[2:] 

    numbers = numbers.replace("\n", delimiter).replace(delimiter, ",")

    parts = commas.split(",")
    nums = [int(p) for p in parts if p.strip() != ""]
    return sum(nums)
