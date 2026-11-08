# Grand Hotel Booking Site

A hotel website built with Django and Bootstrap where guests can browse rooms and book a stay online.

**Live demo:** coming soon

## Features

- Home page with featured rooms
- Rooms list and room detail pages with photos
- Booking form with validation (no past dates, no overlapping bookings for the same room)
- Automatic calculation of nights and total price
- Admin dashboard to manage rooms and bookings
- Responsive layout that works on phones

## Built with

- Python and Django
- HTML and Bootstrap 5
- SQLite

## Screenshots

![Home](screenshots/home.png)
![Rooms](screenshots/rooms.png)
![Booking form](screenshots/booking.png)
![Booking confirmation](screenshots/success.png)

## Run it locally

```
git clone https://github.com/victornnajifor333/hotel-booking-site.git
cd hotel-booking-site
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
```

Create a file named `.env` in the project folder with this line:

```
SECRET_KEY=any-long-random-text
```

Then run:

```
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Open http://127.0.0.1:8000/admin/, log in and add a few rooms, then visit http://127.0.0.1:8000/.

## What I learned

- Building models, views, templates and forms in Django
- Validating user input and preventing double bookings
- Using Git and GitHub, and keeping secrets out of the repository

## Author

NNAJIOFOR VICTOR