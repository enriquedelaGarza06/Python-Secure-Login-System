# Define the maximum limit we want to simulate (like the max value of a byte)
MAX_VALUE = 255

# The starting number is the maximum value
num = MAX_VALUE

print(f"Initial value (maximum allowed): {num}")

# We attempt to add 1 twenty times
print("\nStarting addition loop:")
for i in range(1, 20):
    # Add 1
    num += 1
    
    # Apply the modulo operator to simulate "overflow"
    # The value "wraps around" to 0 if it exceeds 255
    num = num % (MAX_VALUE + 1)
    
    print(f"Iteration {i:2}: {num}")

# Print the final value
print(f"\nFinal value after overflow: {num}")