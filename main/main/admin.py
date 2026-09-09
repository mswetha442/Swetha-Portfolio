from django.contrib import admin
from .models import Profile, Project, ProjectImage, Experience, Education

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3  # Provides 3 upload fields by default

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)