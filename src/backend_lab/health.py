def is_ready() -> bool:
    return True


def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


total = calculate_total(100.0, 2)
