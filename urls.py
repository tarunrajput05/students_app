from django.urls import path

from . import views

app_name = "students_app"

urlpatterns = [
    path("", views.home, name="home"),
    path("about-us/", views.about_us, name="about_us"),
    path("content/", views.content, name="content"),
    path("contact-us/", views.contact_us, name="contact_us"),
    path("faq/", views.faq, name="faq"),
]
