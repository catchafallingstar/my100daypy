while True:
    try:
        f = float(input("Enter Fahrenheit: "))
        # If the line above works, we break the loop
        break 
    except ValueError:
        # If float() fails, it jumps here instead of crashing
        print(" Warning: Please enter a valid number (e.g., 98.6).")

c = (f - 32) * 5/9
print(f"Celsius: {c:.2f}")