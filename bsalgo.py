def bin_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# --- Get user input ---
try:
    user_input = input("Enter a sorted list of numbers (comma-separated): ")
    arr = list(map(int, user_input.split(",")))
    arr.sort()  # Make sure it's sorted

    target = int(input("Enter the number to search: "))

    result = bin_search(arr, target)

    if result != -1:
        print(f"✅ {target} found at index {result}")
    else:
        print(f"❌ {target} not found in the list")

except ValueError:
    print("⚠️ Please enter valid numeric input only.")
