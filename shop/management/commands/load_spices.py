from django.core.management.base import BaseCommand
from your_app.models import Product  # Replace with your app name

class Command(BaseCommand):
    help = "Load dummy spice data into Product model"

    def handle(self, *args, **kwargs):
        data = [
            {"name": "Turmeric Powder", "price": 89, "image_url": "https://images.unsplash.com/photo-1615484477217-736ab9c8f9a5"},
            {"name": "Coriander Seeds", "price": 75, "image_url": "https://images.unsplash.com/photo-1631515243347-3e2206f31c35"},
            # Add all data here
        ]
        for item in data:
            Product.objects.create(**item)
        self.stdout.write(self.style.SUCCESS("✅ Dummy spice data loaded!"))
