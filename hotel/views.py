from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Booking
from .forms import BookingForm

#  Create your views here

def home(request):
    featured = Room.objects.filter(available=True)[:3]
    return render(request, 'hotel/home.html', {'featured': featured})

def rooms(request):
    all_rooms = Room.objects.filter(available=True)
    return render(request, 'hotel/rooms.html', {'rooms': all_rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'hotel/room_detail.html', {'room': room})

def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, room=room)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()
            return redirect('booking_success', booking_id=booking.id)
    else:
        form = BookingForm(room=room)
    return render(request, 'hotel/book_room.html', {'form': form, 'room': room})

def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'hotel/booking_success.html', {'booking': booking})

def about(request):
    return render(request, 'hotel/about.html')

def contact(request):
    return render(request, 'hotel/contact.html')