from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("social/login/", include("account.urls")),

    path('api/', include('app.urls')),
]
