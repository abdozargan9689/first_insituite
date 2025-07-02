from django.contrib import admin
from .models import Admin, Student, Courses, Subjects, Quizzes, Behavior

@admin.register(Admin)
class AdminModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'created_at']
    search_fields = ['username', 'name']
    readonly_fields = ['created_at']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id_card', 'fullname', 'rank', 'total_degree', 'created_at', 'updated_at']
    list_filter = ['rank', 'created_at']
    search_fields = ['id_card', 'fullname']
    readonly_fields = ['total_degree', 'created_at', 'updated_at']

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_name', 'student', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'id_name', 'student__fullname']
    readonly_fields = ['created_at']

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'full_degree', 'pass_degree', 'owner_degree', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['name', 'course__name']
    readonly_fields = ['created_at']

@admin.register(Quizzes)
class QuizzesAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'full_degree', 'pass_degree', 'owner_degree', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['name', 'course__name']
    readonly_fields = ['created_at']

@admin.register(Behavior)
class BehaviorAdmin(admin.ModelAdmin):
    list_display = ['course', 'full_degree', 'pass_degree', 'owner_degree', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['course__name']
    readonly_fields = ['created_at']
