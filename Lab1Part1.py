# Group C, Problem 1 Solution (Python): PC Component Compatibility Checker
# This system uses nested if-elif-else statements to check component compatibility.

def check_compatibility(socket_type, ram_type):
    socket = socket_type.upper()
    ram = ram_type.upper()


    print("\n--- PC Component Compatibility Check ---")
    print(f"Components: Socket={socket}, RAM={ram}")

    # Outer branch: Check the CPU Socket Type
    if socket == "LGA1700":
        # Inner branch: Check the required RAM Type
        if ram == "DDR5":
            result = "COMPATIBLE"
        else:
            result = "INCOMPATIBLE (LGA1700 requires DDR5)"

    elif socket == "AM4":
        # Inner branch: Check the required RAM Type
        if ram == "DDR4":
            result = "COMPATIBLE"
        else:
            result = "INCOMPATIBLE (AM4 requires DDR4)"

    else:
        # Unknown or unsupported socket type
        result = "INCOMPATIBLE (Unknown/Unsupported Socket Type)"

    print(f"Compatibility Status: {result}")
    print("--------------------------------------")


# Example 1: Compatible components
check_compatibility("LGA1700", "DDR5")

# Example 2: Incompatible RAM
check_compatibility("AM4", "DDR5")

# Example 3: Compatible components (lowercase input)
check_compatibility("am4", "ddr4")

# Example 4: LGA1700/DDR4 (missed compatibility)
check_compatibility("LGA1700", "DDR4")

# Example 5: Unknown socket type
check_compatibility("LGA1200", "DDR4")