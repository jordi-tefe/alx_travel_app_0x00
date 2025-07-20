# ALX Travel App - Milestone 2

## Project Overview

This project is a Django-based travel app that allows users to view listings, make bookings, and post reviews. This milestone focuses on creating database models, serializers for API representation, and a seeder to populate the database with sample data.

---

## Features Implemented

- **Models**  
  Defined the following models in `listings/models.py`:
  - `Listing` — represents travel listings with title, description, location, price per night, and availability status.
  - `Booking` — represents user bookings for listings, with check-in/out dates and total price.
  - `Review` — represents user reviews with ratings and comments linked to listings.

- **Serializers**  
  Created serializers in `listings/serializers.py` for:
  - `ListingSerializer`
  - `BookingSerializer`

- **Seeder**  
  Implemented a custom Django management command `seed` in  
  `listings/management/commands/seed.py` that populates the database with sample `Listing` data.

---

## How to Run Seeder

1. Make sure you have installed all required dependencies (including `Faker` library):

   ```bash
   pip install Faker
