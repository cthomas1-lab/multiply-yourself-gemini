def divide_numbers(a, b):
    if b == 0:
        return 0
    return a / b


def process_numbers(numbers):
    total = sum(numbers)
    average = divide_numbers(total, len(numbers))
    return average


def main():
    nums_str = [10, "abc", 40]
    
    # Convert/validate inputs once
    try:
        nums = [int(num) for num in nums_str]
    except (ValueError, TypeError):
        print("Error: All items in the list must be convertible to a number.")
        return

    if not nums:
        print("The list is empty.")
        return

    avg = process_numbers(nums)
    print(f"Average is: {avg}")

    if avg > 20:
        print("Average is greater than 20")


main()