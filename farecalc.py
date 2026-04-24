# The "FareCalc" Travel Optimizer

def compute_fare(distance, service_type, hour):
    # per km pricing for each type of service 
    fare_rates = {
        "economy": 10,
        "premium": 18,
        "suv": 25
    }

    # check if service type is valid
    if service_type not in fare_rates:
        return None

    # calculate base cost
    base_cost = distance * fare_rates[service_type]

    # peak hour pricing (5 PM to 8 PM)
    if hour >= 17 and hour <= 20:
        surge_multiplier = 1.5
    else:
        surge_multiplier = 1

    surge_cost = base_cost * surge_multiplier

    # add tax (5%)
    tax = surge_cost * 0.05
    total_cost = surge_cost + tax

    #  discount for long rides
    if distance > 20:
        total_cost = total_cost * 0.95   # 5% discount

    return round(total_cost, 2)


def take_input():
    # mapping for flexible input (numbers or names)
    service_map = {
        "1": "economy",
        "2": "premium",
        "3": "suv",
        "economy": "economy",
        "premium": "premium",
        "suv": "suv"
    }

    try:
        distance = float(input("Enter distance (in km): "))

        print("\nSelect Service Type:")
        print("1. Economy")
        print("2. Premium")
        print("3. SUV")

        choice = input("Enter option (1/2/3 or name): ").lower().strip()
        service_type = service_map.get(choice)

        hour = int(input("Enter travel hour (0–23): "))

        # validations
        if distance <= 0:
            print("Distance must be greater than 0")
            return None

        if hour < 0 or hour > 23:
            print("Invalid hour entered")
            return None

        if service_type is None:
            print("Invalid service type selected")
            return None

        return distance, service_type, hour

    except ValueError:
        print("Invalid input! Please enter correct values")
        return None


def show_receipt(distance, service, hour, amount):
    print("\n---------- Ride Summary ----------")
    print(f"Distance       : {distance} km")
    print(f"Service Type   : {service.capitalize()}")
    print(f"Travel Time    : {hour}:00")

    if hour >= 17 and hour <= 20:
        print("Peak Pricing   : Applied")
    else:
        print("Peak Pricing   : Not Applied")

    print(f"Total Fare     : ₹{amount}")
    print("------------------------------------\n")


# main program
user_data = take_input()

if user_data:
    distance, service, hour = user_data

    final_fare = compute_fare(distance, service, hour)

    if final_fare is None:
        print("Service Not Available")
    else:
        show_receipt(distance, service, hour, final_fare)