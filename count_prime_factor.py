n = 10
count = 0
divisor = 2  # Start with the smallest prime number

while n > 1:
    if n % divisor == 0:
        # Count the factor if it's prime
        count += 1
        while n % divisor == 0:
            n //= divisor
    divisor += 1

print(count)
