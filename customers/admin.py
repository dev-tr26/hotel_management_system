from django.contrib import admin
from .models import Booking, Guest, Feedback , CustomUser 
from django.contrib.auth.admin import UserAdmin


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'room', 'check_in', 'check_out', 'booking_type', 'adults', 'children')
    list_filter = ('booking_type',)
    search_fields = ('room__room_no',)



@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_id', 'full_name', 'booking', 'aadhar_no', 'mobile_no', 'nationality')
    list_filter = ('gender', 'nationality')
    search_fields = ('first_name', 'last_name', 'aadhar_no', 'mobile_no')

    def full_name(self, obj):
        return f"{obj.title} {obj.first_name} {obj.last_name or ''}"
    full_name.short_description = 'Name'


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_id', 'booking', 'feedback_date', 'rating', 'comments_preview')
    list_filter = ('rating',)
    search_fields = ('comments',)

    def comments_preview(self, obj):
        return obj.comments[:50] + '...' if obj.comments and len(obj.comments) > 50 else obj.comments
    comments_preview.short_description = 'Comments'
    

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Personal info', {'fields': ('full_name',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

admin.site.register(CustomUser, CustomUserAdmin)