from db.mixins import validate_hotel

def test_valid_hotel():
    hotel = {"name": "Hotel A", "price": "120", "source": "Booking.com"}
    assert validate_hotel(hotel) == True

def test_invalid_hotel():
    hotel = {"name": "", "price": "120", "source": "Booking.com"}
    assert validate_hotel(hotel) == False
    hotel = {"name": "Hotel B", "price": "abc", "source": "Booking.com"}
    assert validate_hotel(hotel) == False
    hotel = {"name": "Hotel C", "price": "120", "source": ""}
    assert validate_hotel(hotel) == False
