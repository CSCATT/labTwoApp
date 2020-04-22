from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from .models import *

# def get_booking(request):
# 	bookking_seat = Booking.objects.get(name = '')
# 	return HttpResponse(f'{bookking_seat}')

def get_booking(request, booking_id):
	bookking_seat = Booking.objects.get(id = booking_id)
	return HttpResponse(f'{bookking_seat}')

urlpatterns = [
    path('admin/', admin.site.urls),
]
