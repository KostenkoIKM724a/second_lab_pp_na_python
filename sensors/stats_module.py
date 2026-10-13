import statistics

def get_average(data_dict):
    if not data_dict:
        return None
    values = list(data_dict.values())
    return sum(values) / len(values)

def get_min(data_dict):
    if not data_dict:
        return None
    return min(data_dict.values())

def get_max(data_dict):
    if not data_dict:
        return None
    return max(data_dict.values())

def get_median(data_dict):
    if not data_dict:
        return None
    values = list(data_dict.values())
    return statistics.median(values)

def find_jumps(data_dict, threshold):
    jumps = []
    items = list(data_dict.items())
    for i in range(len(items) - 1):
        t1, val1 = items[i]
        t2, val2 = items[i + 1]
        diff = abs(val2 - val1)
        if diff > threshold:
            jumps.append((t1, t2, diff))
    return jumps

def show_table(data_dict, title):
    print(f"\n=== Table: {title} ===")
    print(f"{'Time Label':<12} | {'Value'}")
    print("-" * 28)
    for time_key, val in data_dict.items():
        print(f"{time_key:<12} | {val}")
