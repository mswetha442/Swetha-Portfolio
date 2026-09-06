from django.contrib import admin
from .models import Profile, Project, Experience, Education


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "profession",
        "email",
        "phone",
        "location",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")
    search_fields = ("title", "technologies")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("job_title", "company", "start_date", "end_date")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "start_year", "end_year")