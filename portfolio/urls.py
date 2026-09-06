from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from main import views as main_views


urlpatterns = [

    # =========================
    # ADMIN
    # =========================

    path(
        "admin/",
        admin.site.urls
    ),

    # =========================
    # HOME
    # =========================

    path(
        "",
        main_views.home,
        name="home"
    ),

    # =========================
    # USER PORTFOLIO
    # =========================

    path(
        "portfolio/<str:username>/",
        main_views.portfolio,
        name="portfolio"
    ),

    # =========================
    # ACCOUNTS
    # =========================

    path(
        "accounts/",
        include("accounts.urls")
    ),
]


# =========================
# MEDIA FILES
# Profile images / Resumes
# =========================

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )