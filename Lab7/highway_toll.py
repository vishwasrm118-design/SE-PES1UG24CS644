def parse_plate(plate):
    if not isinstance(plate, str):
        return None
    parts = plate.split('-')
    if len(parts) != 4:
        return None
    state, district, series, number = parts
    try:
        district_num = int(district)
        plate_num = int(number)
        if district_num < 0 or plate_num < 0:
            return None
        return state.strip().upper(), district_num, plate_num
    except (ValueError, TypeError):
        return None

def trip_cost(text):
    if not isinstance(text, str):
        return None
    parts = text.lower().split('x')
    if len(parts) != 2:
        return None
    try:
        count = int(parts[0].strip())
        rate = int(parts[1].strip())
        if count < 0 or rate < 0:
            return None
        return count * rate
    except (ValueError, TypeError):
        return None

def axle_class(axles):
    if axles is None:
        return None
    try:
        n = int(axles)
    except (ValueError, TypeError):
        return None
    if n < 2:
        return None
    if n == 2:
        return 'car'
    if n <= 4:
        return 'truck'
    return 'heavy'

def main():
    print("==== Running parse_plate ====")
    user_input = input("Enter a plate (e.g. KA-05-AB-1234): ")
    result = parse_plate(user_input)
    print("State, District and Number:", result)

    print("\n==== Running trip_cost ====")
    user_input = input("Enter trips x rate (e.g. 3x150): ")
    result = trip_cost(user_input)
    print("Trip Cost:", result)

    print("\n==== Running axle_class ====")
    user_input = input("Enter an axle count (e.g. 3): ")
    result = axle_class(user_input)
    print("Vehicle Class:", result)

if __name__ == "__main__":
    main()