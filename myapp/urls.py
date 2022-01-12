from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('url_end_point/', views.function_name for excute , name = " title or Raka home page")
    path('', views.hello_world, name="Raka home page"),
    path("raka", views.raka_name, name="Raka info"),
    path("test", views.test, name="Create HTML for Test"),
    path("pass_value_runtime_test", views.pass_value_dynamically, name="Pass value run timeTest"),
    path("raka_fb", views.raka_fb_link, name="Raka FB"),
    path("raka_youtube", views.youtube, name="Raka Youtube"),
    path("sample_page", views.sample_page, name="Sample Page  raka"),
    path("submit_expression", views.submit_name_anything, name="Submit test raka"),
    path("add", views.add_number, name="add test raka"),
    path("add_result", views.add_result, name=" result add raka"),
    path("login", views.add_result, name="login raka"),

]
