from django.contrib import admin
from .models import UserProfile
from .models import Course, CourseMaterial


admin.site.register(UserProfile)


class CourseMaterialInline(admin.TabularInline):
    model = CourseMaterial
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseMaterialInline]

admin.site.register(Course, CourseAdmin)
