def unit_converter():
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "inch": 0.0254,
        "ft": 0.3048,
        "mile": 1609.34
    }

    print("\n--- Unit Converter ---")
    print("Available units: mm, cm, m, km, inch, ft, mile")

    try:
        value = float(input("Enter value: "))
        convert_from = input("Enter from: ").lower().strip()
        convert_to = input("Enter to: ").lower().strip()

        if convert_from in units and convert_to in units:
            result = value * (units[convert_from] / units[convert_to])
            print(
                f"Result: {value} {convert_from} = {result:.4f} {convert_to}")
        else:
            print("Invalid units!")
    except ValueError:
        pass


unit_converter()
