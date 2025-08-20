from db.connect import Base, engine
from db.models import Hotel

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")
