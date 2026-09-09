
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    full_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=150)
    bio = models.TextField()

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    email = models.EmailField()
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    location = models.CharField(
        max_length=100,
        blank=True
    )

    github = models.URLField(
        blank=True
    )
    linkedin = models.URLField(
        blank=True
    )

    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.full_name
    
class Project(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    title = models.CharField(max_length=150)

    description = models.TextField()

    technologies = models.CharField(
        max_length=300,
        blank=True
    )

    image = models.ImageField(upload_to='projects/')
    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="projects/carousel/")
    caption = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.project.title} Image"   
class Experience(models.Model):

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="experiences"
    )

    job_title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)

    start_date = models.CharField(max_length=50)
    end_date = models.CharField(
        max_length=50,
        blank=True
    )

    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} - {self.company}"


class Education(models.Model):

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="education"
    )

    degree = models.CharField(max_length=150)

    institution = models.CharField(max_length=200)

    start_year = models.CharField(max_length=20)

    end_year = models.CharField(
        max_length=20,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.degree} - {self.institution}"
