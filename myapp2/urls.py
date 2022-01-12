from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("login", views.login, name="login raka"),
    # path("signin", views.signin, name="signin raka"),
]
