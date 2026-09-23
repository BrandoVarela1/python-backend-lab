def calculate_total(price: float, quantity: int) -> float:
    total = price * quantity
    return total


def main() -> None:
    price = 25.50
    quantity = 4

    total = calculate_total(price, quantity)

    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
