from typing import Union
import json


with open("conversions.json", "r") as f:
    conversion_table = json.load(f)


def unit_type(unit: str) -> Union[str, None]:
    for i in conversion_table:
        if unit in conversion_table[i]["conversions"]:
            return i
    
    # Return None if not found
    return None


def is_same_type(a: str, b: str) -> bool:
    if unit_type(a) == unit_type(b):
        return True
    else:
        return False


def convert(a: str, b: str, value: Union[int, float]) -> Union[int, float]:
    if not is_same_type(a, b):
        raise Exception("Cannot convert different types of units")
    if a == b:
        # Same unit, so no conversion needed
        return value
    
    base_unit_ratio = conversion_table[unit_type(a)]["conversions"][a]
    target_unit_ratio = conversion_table[unit_type(b)]["conversions"][b]

    # TODO: Make Temperature conversion
    if unit_type(a) == "temperature":
        raise NotImplementedError("Temperature conversion not yet implemented")

    return value / base_unit_ratio * target_unit_ratio


if __name__ == "__main__":
    print(convert("cubic meter", "cubic mile", 100))
    print(convert("acre", "square mile", 1))
    # print(convert("liter", "kelvin", 1000))
    print(convert("liter", "cubic kilometer", 1))
    print(convert("centimeter", "kilometer", 2137))
    print(convert("kelvin", "celsius", 300))
