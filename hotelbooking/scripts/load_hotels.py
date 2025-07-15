import os
import django
import sys
import requests
from django.core.files.base import ContentFile
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelease.settings")


django.setup()


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelease.settings")
django.setup()

from booking.models import Hotel
from django.core.files.base import ContentFile
import requests


hotels = [
    {
        "name": "Sea Breeze Resort",
        "location": "Goa",
        "description": "A beachside resort with sunset views.",
        "price": 3299,
        "image_url": "https://picsum.photos/seed/hotel1/600/400"
    },
    {
        "name": "Mountain View Lodge",
        "location": "Manali",
        "description": "Peaceful lodge surrounded by mountains.",
        "price": 2799,
        "image_url": "https://picsum.photos/seed/hotel2/600/400"
    },
    {
        "name": "City Central Hotel",
        "location": "Bangalore",
        "description": "Modern rooms in the heart of the city.",
        "price": 1999,
        "image_url": "https://picsum.photos/seed/hotel3/600/400"
    },
]


for data in hotels:
    hotel = Hotel(
        name=data["name"],
        location=data["location"],
        description=data["description"],
        price_per_night=data["price"]
    )
    
    
    response = requests.get(data["image_url"])
    if response.status_code == 200:
        image_name = f"{data['name'].replace(' ', '_')}.jpg"
        hotel.image.save(image_name, ContentFile(response.content), save=False)
    
    hotel.save()
    print(f"Added: {hotel.name}")
