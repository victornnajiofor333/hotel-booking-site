from django.contrib import admin
from .models import Room, Booking

# Register your admin here

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'capacity', 'available')
    list_filter = ('available',)
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):        
        list_display = ('guest_name', 'room', 'check_in', 'check_out', 'nights', 'total_price', 'phone')
        search_fields = ('guest_name', 'email', 'phone')