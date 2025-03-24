from django.urls import path
from . import views

urlpatterns = [
    path('rooms/',views.room_list, name='room_list'),
#     path('book/<int:room_id>/', views.book_room, name='book_room'),
#     path('booking-success/', views.booking_success, name='booking_success'),
]
