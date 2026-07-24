try:
    number = int(input("Enter the number to analyze: "))

    def pos_neg(n):
        if n > 0:
            print("The number is positive.")
        elif n < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")

    def even_odd(n):
        if n % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")

    def prime_or_not(n):
        if n <= 1:
            print("The number is not a prime number.")
        else:
            for i in range(2, n):
                if n % i == 0:
                    print("The number is not a prime number.")
                    break
            else:
                print("The number is a prime number.")

    def armstrong_or_not(n):
        if n < 0:
            print("Negative numbers are not Armstrong numbers.")
            return

        temp = n
        arms = n
        count = 0
        total = 0

        while temp > 0:
            count += 1
            temp //= 10

        while arms > 0:
            digit = arms % 10
            total += digit ** count
            arms //= 10

        if total == n:
            print("The number is an Armstrong number.")
        else:
            print("The number is not an Armstrong number.")

    def palindrome_or_not(n):
        n = abs(n)
        original = n
        rev = 0

        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10

        if rev == original:
            print("The number is a palindrome.")
        else:
            print("The number is not a palindrome.")

    print("\n----- Number Analysis -----")
    pos_neg(number)
    even_odd(number)
    prime_or_not(number)
    armstrong_or_not(number)
    palindrome_or_not(number)

except ValueError:
    print("Error: Please enter a valid integer.")