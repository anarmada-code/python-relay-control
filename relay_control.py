# Python Relay Control Simulation

print("=== Relay Control System ===")

while True:
    print("\n1. Turn Relay ON")
    print("2. Turn Relay OFF")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Relay is ON")

    elif choice == "2":
        print("Relay is OFF")

    elif choice == "3":
        print("Program stopped.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
