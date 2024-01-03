# Taking input from the user
arr = list(map(int, input("Enter space-separated elements of the array: ").split()))

# Initializing start and end variables
start = arr[0]
end = arr[0]

# Iterate over the array
N = len(arr)
for i in range(1, N):
    # Update end
    end = max(arr[i], end + arr[i])
    # Update start
    start = max(start, end)

# Print the result
print("The maximum subarray sum is:", start)
