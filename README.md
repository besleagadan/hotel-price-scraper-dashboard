# Hotel Price Scraper Dashboard

A desktop application that automates the collection of hotel pricing data from multiple sources, stores the results in a PostgreSQL database, and visualizes them through an interactive PySide6 dashboard.

## Overview

This project demonstrates the integration of web scraping, data storage, and desktop application development. It fetches hotel pricing data from platforms like Booking.com and Hotels.com, stores the information in a PostgreSQL database, and presents it through a user-friendly desktop dashboard built with PySide6.

## Features

- **Automated Data Collection:** Scrapes hotel prices and details from multiple online sources.
- **Data Storage:** Stores collected data in a PostgreSQL database.
- **Interactive Dashboard:** Visualizes data through an intuitive PySide6 desktop application.
- **Data Visualization:** Displays bar charts comparing hotel prices.
- **Data Validation:** Ensures data integrity with validation checks.

## Technologies Used

- **Python:** Programming language for backend logic.
- **Selenium:** Web scraping tool for data extraction.
- **PySide6:** Framework for building the desktop application.
- **PostgreSQL:** Database for storing scraped data.
- **pandas:** Data manipulation and analysis.
- **matplotlib:** Data visualization.

## Installation

### Clone the Repository
```bash
git clone https://github.com/besleagadan/hotel-price-scraper-dashboard.git
cd hotel-price-scraper-dashboard
```

### Set Up Virtual Environment
```bash
# Create a new environment
uv init
# Install packages
uv add requests selenium sqlalchemy
# Install from lockfile (reproducible installs)
uv install
# List installed packages
uv list
# Remove a package
uv remove package_name
```

### Set Up PostgreSQL Database
```bash
docker run --name hotel-price-scraper-dashboard-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=hotel_prices -p 5432:5432 -d postgres
```

### Access the database
```bash
docker exec -it hotel-price-scraper-dashboard-db psql -U postgres -d hotel_prices -c "\dt"
```

## Usage

### Run the Scraper
```bash
uv run -m app.main
```

### Launch the Dashboard
```bash
uv run -m ui.main
```
The dashboard will display hotel data and visualizations.

### Run All Tests
```bash
uv run pytest tests/ --maxfail=1 --disable-warnings -q
```

## Screenshots

![PySide6 Result](https://github.com/besleagadan/hotel-price-scraper-dashboard/blob/main/src/images/puside6.png)

![PgAdmin Result](https://github.com/besleagadan/hotel-price-scraper-dashboard/blob/main/src/images/pgadmin.png)

![Terminal Result](https://github.com/besleagadan/hotel-price-scraper-dashboard/blob/main/src/images/terminal.png)

## Author

**Dan** — Python Developer & Creator

📧 Contact: [danu1besleaga@gmail.com]
🌐 GitHub: github.com/besleagadan
