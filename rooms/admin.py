from django.contrib import admin
from .models import Department, Room


from django.contrib import admin
from .models import (
    Department, Room, Service, HousekeepingService, LuxurySpaService,
    MultiCuisineRestaurantService, FitnessCenterService, TheaterService,
    FreeWifiService
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'department_name', 'department_head_id', 'employee_underwork')
    search_fields = ('department_name',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_no', 'room_type', 'no_of_beds', 'status')
    list_filter = ('status', 'room_type')
    search_fields = ('room_no',)



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'description')
    search_fields = ('description',)



@admin.register(HousekeepingService)
class HousekeepingServiceAdmin(admin.ModelAdmin):
    list_display = ('housekeeping_id', 'room', 'service', 'status', 'staff_assigned', 'service_date')
    list_filter = ('status',)
    search_fields = ('room_no__room_no',)

@admin.register(LuxurySpaService)
class LuxurySpaServiceAdmin(admin.ModelAdmin):
    list_display = ('spa_id', 'treatment_type', 'duration', 'service_date')
    search_fields = ('treatment_type',)

@admin.register(MultiCuisineRestaurantService)
class MultiCuisineRestaurantServiceAdmin(admin.ModelAdmin):
    list_display = ('restaurant_id', 'cuisine_type', 'seating_capacity', 'service_date')
    search_fields = ('cuisine_type',)


@admin.register(FitnessCenterService)
class FitnessCenterServiceAdmin(admin.ModelAdmin):
    list_display = ('fitness_center_id', 'equipment_count', 'service_date')


@admin.register(TheaterService)
class TheaterServiceAdmin(admin.ModelAdmin):
    list_display = ('theater_id', 'event_type', 'seating_capacity', 'service_date')
    search_fields = ('event_type',)


@admin.register(FreeWifiService)
class FreeWifiServiceAdmin(admin.ModelAdmin):
    list_display = ('wifi_id', 'wifi_name', 'booking', 'service_date')
    search_fields = ('wifi_name',)