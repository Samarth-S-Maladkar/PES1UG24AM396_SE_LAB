import math


def parse_rental(text):
    if not isinstance(text, str):
        return "", 0.0
    parts = text.split(":")
    if len(parts) != 2:
        return "", 0.0
    unit_raw, months_raw = parts[0].strip(), parts[1].strip()
    if not unit_raw:
        return "", 0.0
    try:
        months = float(months_raw)
    except (ValueError, TypeError):
        return "", 0.0
    if not math.isfinite(months) or months < 0:
        return "", 0.0
    return unit_raw.title(), months


def duration_average(months_csv):
    if not isinstance(months_csv, str) or not months_csv.strip():
        return 0
    values = []
    for token in months_csv.split(","):
        token = token.strip()
        if not token:
            continue
        try:
            val = int(token)
            if val >= 0:
                values.append(val)
        except (ValueError, TypeError):
            continue
    if not values:
        return 0
    return sum(values) // len(values)


def payable_rent(text):
    if not isinstance(text, str):
        return 0.0
    parts = text.split("|")
    if len(parts) != 2:
        return 0.0
    try:
        rent = float(parts[0].strip())
        discount = float(parts[1].strip())
    except (ValueError, TypeError):
        return 0.0
    if not (math.isfinite(rent) and math.isfinite(discount)):
        return 0.0
    if rent < 0 or discount < 0:
        return 0.0
    total = round(rent * 1.18 - discount, 2)
    return max(total, 0.0)


def main():
    print("==== Running parse_rental ====")
    user_input = input("Enter unit:months (e.g. medium:6): ")
    result = parse_rental(user_input)
    print("Unit and Months:", result)

    print("\n==== Running duration_average ====")
    user_input = input("Enter rental months as CSV (e.g. 3,6,12): ")
    result = duration_average(user_input)
    print("Average Duration:", result)

    print("\n==== Running payable_rent ====")
    user_input = input("Enter rent|discount (e.g. 2400|200): ")
    result = payable_rent(user_input)
    print("Payable Rent:", result)


if __name__ == "__main__":
    main()
