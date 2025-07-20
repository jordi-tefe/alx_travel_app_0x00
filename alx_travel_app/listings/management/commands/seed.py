from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.text(),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 300), 2),
                is_available=random.choice([True, False])
            )
        self.stdout.write(self.style.SUCCESS("Database seeded successfully with Listings"))
