"""Temperature conversions."""


def convert(value: float, src: str, dst: str) -> float:
    if src == dst:
        return value
    if src == "C" and dst == "F":
        return round(value * 9 / 5 + 32, 2)
    if src == "F" and dst == "C":
        return round((value - 32) * 5 / 9, 2)
    raise ValueError("unsupported conversion")
