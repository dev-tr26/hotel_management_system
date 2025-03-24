from django.contrib import admin
from .models import Employee, Attendance, LeaveRequest

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'department', 'designation', 'salary', 'email_id', 'phone')
    list_filter = ('department', 'designation')
    search_fields = ('employee_name', 'email_id', 'phone')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('attendance_id', 'employee', 'attendance_date', 'attendance_status')
    list_filter = ('attendance_status',)
    search_fields = ('employee__employee_name',)

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'employee', 'leave_type', 'from_date', 'to_date', 'status')
    list_filter = ('leave_type', 'status')
    search_fields = ('employee__employee_name', 'reason')