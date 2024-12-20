# Define the list of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Function to print all allowed vehicles
def print_allowed_vehicles():
    print(" ")
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(f"- {vehicle}")
        print(" ")

# Function to search for a specific vehicle
def search_vehicle():
    print("********************************")
    print("Please Enter the full Vehicle name:")
    vehicle_name = input("           ").strip()
    # Case-insensitive search logic
    if vehicle_name.lower() in [vehicle.lower() for vehicle in AllowedVehiclesList]:
        print(f"{vehicle_name} is an authorized vehicle.")
    else:
        print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again.")
    print("********************************")

# Main menu function
def menu():
    while True:
        print(" ")
        print("********************************")
        print("AutoCountry Vehicle Finder v0.2")
        print("********************************")
        print(" ")
        print("Please Enter the following number below from the following menu:")
        print(" ")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. Exit")

        choice = input("           ").strip()

        if choice == '1':
            print_allowed_vehicles()
        elif choice == '2':
            search_vehicle()
        elif choice == '3':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
menu()
