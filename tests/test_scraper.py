from app.scraper import scrape_booking, scrape_hotels
from ui.main import fetch_hotels_from_db

def test_scrape_booking():
    hotels = scrape_booking("Paris")
    assert isinstance(hotels, list)
    assert len(hotels) > 0
    for h in hotels:
        assert "name" in h
        assert "price" in h
        assert "source" in h

def test_scrape_hotels():
    hotels = scrape_hotels("Paris")
    assert isinstance(hotels, list)
    for h in hotels:
        assert "name" in h
        assert "price" in h
        assert "source" in h

def test_fetch_hotels():
    hotels = fetch_hotels_from_db("Paris")
    assert isinstance(hotels, list)
