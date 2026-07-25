try:
    list_analyze = []

    # Taking 10 numbers as input
    for i in range(10):
        list_item = int(input("Enter the number: "))
        list_analyze.append(list_item)

    def largest_num(n):
        return max(n)

    def smallest_num(n):
        return min(n)

    # Find the second largest number without modifying the original list
    def second_largest(n):
        unique_numbers = list(set(n))

        if len(unique_numbers) < 2:
            return "Not Available"

        unique_numbers.remove(max(unique_numbers))
        return max(unique_numbers)

    def sum_list(n):
        return sum(n)

    def avg_list(n):
        return sum(n) / len(n)

    def even_num(n):
        even = []
        for item_even in n:
            if item_even % 2 == 0:
                even.append(item_even)
        return even

    def odd_num(n):
        odd_values = []
        for item_odd in n:
            if item_odd % 2 != 0:
                odd_values.append(item_odd)
        return odd_values

    # Calling all functions
    largest_value = largest_num(list_analyze)
    smallest_value = smallest_num(list_analyze)
    second_largest_value = second_largest(list_analyze)
    list_sum = sum_list(list_analyze)
    list_average = avg_list(list_analyze)
    even_value = even_num(list_analyze) 
    odd_value = odd_num(list_analyze)

    # Displaying the results
    print("\n----- List Analysis -----")
    print("List values are below:")

    for idx, item in enumerate(list_analyze, start=1):
        print(f"{idx}: Value ~ {item}")

    print(f"\nThe largest value in the list is: {largest_value}")
    print(f"The smallest value in the list is: {smallest_value}")
    print(f"The second largest value in the list is: {second_largest_value}")
    print(f"The sum of the list values is: {list_sum}")
    print(f"The average of the list values is: {list_average:.2f}")
    print(f"The even values in the list are: {even_value}")
    print(f"The odd values in the list are: {odd_value}")

except ValueError:
    print("Error: Please enter a valid integer.")