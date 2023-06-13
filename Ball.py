def calculate_max_height(v0, g):
    time_to_peak = v0 / g  # Time taken to reach the peak
    max_height = (v0 * time_to_peak) - (0.5 * g * time_to_peak ** 2)  # Formula for maximum height
    return max_height


# Input values from the console
v0 = float(input("Enter the initial velocity of the ball (ft/sec): "))
g = 32.8  # Force of gravity (ft/sec^2)

# Calculate and print the maximum height
max_height = calculate_max_height(v0, g)
print("The maximum height reached by the ball is:", max_height, "ft")
