
def validate_hotel(hotel):
    # Name must exist
    if not hotel.get("name"):
        return False

    # Price must be numeric
    price = hotel.get("price")
    if not price:
        return False

    try:
        hotel["price"] = float(''.join(filter(str.isdigit, str(price))))
    except ValueError:
        return False

    # Source must exist
    if not hotel.get("source"):
        return False

    return True
