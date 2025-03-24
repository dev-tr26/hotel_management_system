# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Room, Booking
# from .forms import BookingForm


# @login_required
# def room_list(request):
#     rooms = Room.objects.filter(is_available=True)
#     return render(request, 'rooms/room_list.html', {'rooms': rooms})


# @login_required
# def book_room(request, room_id):
#     room = get_object_or_404(Room, id=room_id)

#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.guest = request.user  # Assign the logged-in user
#             booking.room = room
#             booking.status = 'pending'
#             booking.save()
#             return redirect('booking_success')

#     else:
#         form = BookingForm()

#     return render(request, 'rooms/book_room.html', {'form': form, 'room': room})

def room_list(request):
    return HttpResponse(request, 'room list is here')




