def sort(width: int, height: int, length: int, mass: int) -> str:
    volume = width * height * length

    is_bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
