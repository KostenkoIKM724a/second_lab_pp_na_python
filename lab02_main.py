import stats_module as sm

def parse_input(input_str):
    tokens = input_str.strip().split()
    numbers = []
    for token in tokens:
        try:
            val = float(token)
            numbers.append(val)
        except ValueError:
            print(f"Warning: token '{token}' skipped (not a number).")
    return numbers

def create_data_dict(temp_list, hum_list, pres_list):
    length = min(len(temp_list), len(hum_list), len(pres_list))
    
    temp_dict = {f"T{i+1}": temp_list[i] for i in range(length)}
    hum_dict = {f"T{i+1}": hum_list[i] for i in range(length)}
    press_dict = {f"T{i+1}": pres_list[i] for i in range(length)}
    
    return {
        "temperature": temp_dict,
        "humidity": hum_dict,
        "pressure": press_dict
    }

def process_measurements(title, data_dict, threshold):
    if not data_dict:
        print(f"No data for {title}.")
        return

    sm.show_table(data_dict, title)

    avg = sm.get_average(data_dict)
    minimum = sm.get_min(data_dict)
    maximum = sm.get_max(data_dict)
    median = sm.get_median(data_dict)
    jumps = sm.find_jumps(data_dict, threshold)

    print(f"Average: {avg:.2f}" if avg is not None else "Average: -")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Median: {median}")

    if jumps:
        jumps_str = ", ".join([f"between {t1} -> {t2} ({diff:.1f})" for t1, t2, diff in jumps])
        print(f"Sharp jumps: {jumps_str}")
    else:
        print("Sharp jumps: None")

def main():
    print("=== Smart Home Data Processing ===")

    temp_str = input("Enter temperatures (°C): ")
    hum_str = input("Enter humidity (%): ")
    pres_str = input("Enter pressure (Pa): ")

    temp_list = parse_input(temp_str)
    hum_list = parse_input(hum_str)
    pres_list = parse_input(pres_str)

    lengths = [len(temp_list), len(hum_list), len(pres_list)]
    if len(set(lengths)) > 1:
        print("\n[WARNING] Measurement lengths differ! Data will be trimmed.")

    if not temp_list or not hum_list or not pres_list:
        print("Error: One of the measurement lists is empty.")
        return

    data = create_data_dict(temp_list, hum_list, pres_list)

    process_measurements("Temperature", data["temperature"], threshold=7.0)
    process_measurements("Humidity", data["humidity"], threshold=20.0)
    process_measurements("Pressure", data["pressure"], threshold=5000.0)

if __name__ == "__main__":
    main()
