import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd

from db.connect import get_connection

class HotelDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotel Price Dashboard")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Hotel Prices")
        self.layout.addWidget(self.label)

        # Table
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        # Button to fetch prices
        self.fetch_btn = QPushButton("Fetch Prices")
        self.fetch_btn.clicked.connect(self.fetch_prices)
        self.layout.addWidget(self.fetch_btn)

        # Chart
        self.figure = Figure(figsize=(6, 4))
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def fetch_prices(self):
        self.label.setText("Fetching prices from DB...")
        hotels = fetch_hotels_from_db("Paris")

        # Update table
        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Price", "Source"])
        for row, hotel in enumerate(hotels):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(hotel["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(str(hotel["price"])))
            self.table.setItem(row, 2, QTableWidgetItem(hotel["source"]))

        # Draw chart
        self.draw_price_chart(hotels)

        self.label.setText(f"Showing {len(hotels)} hotels")

    def draw_price_chart(self, hotels):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        df = pd.DataFrame(hotels)
        if df.empty:
            ax.text(0.5, 0.5, "No data", ha='center', va='center')
        else:
            df.groupby("name")["price"].mean().plot(kind="bar", ax=ax)
            ax.set_ylabel("Price")
            ax.set_title("Average Price per Hotel")

        self.canvas.draw()


def fetch_hotels_from_db(location="Paris"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, price, source FROM hotels WHERE location=%s ORDER BY price ASC", (location,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"name": r[0], "price": float(r[1]), "source": r[2]} for r in rows]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HotelDashboard()
    window.show()
    sys.exit(app.exec())
