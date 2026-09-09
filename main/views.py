from django.shortcuts import render, get_object_or_404

from .models import Profile, Project, Experience, Education


# =========================================================
# HOME / DEFAULT PORTFOLIO
# =========================================================

def home(request):

    profile = Profile.objects.first()

    projects = []
    experiences = []
    educations = []

    if profile:

        projects = Project.objects.filter(
            user=profile.user
        ).order_by("-created_at")

        experiences = Experience.objects.filter(
            profile=profile
        )

        educations = Education.objects.filter(
            profile=profile
        )

    return render(
        request,
        "main/home.html",
        {
            "profile": profile,
            "projects": projects,
            "experiences": experiences,
            "educations": educations,
        }
    )


# =========================================================
# USER PORTFOLIO
# =========================================================

def portfolio(request, username):

    profile = Profile.objects.filter(
        user__username=username
    ).first()

    if not profile:
        return render(
            request,
            "main/home.html",
            {
                "profile": None,
                "projects": [],
                "experiences": [],
                "educations": [],
            }
        )

    projects = Project.objects.filter(
        user=profile.user
    ).order_by("-created_at")

    experiences = Experience.objects.filter(
        profile=profile
    )

    educations = Education.objects.filter(
        profile=profile
    )

    return render(
        request,
        "main/home.html",
        {
            "profile": profile,
            "projects": projects,
            "experiences": experiences,
            "educations": educations,
        }
    )