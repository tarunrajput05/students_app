from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):
    return render(request, "students_app/home.html")


def about_us(request):
    return render(request, "students_app/about_us.html")


def content(request):
    return render(request, "students_app/content.html")


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        query = request.POST.get("query", "").strip()
        mobile = request.POST.get("mobile", "").strip()

        if all((name, email, subject, query, mobile)):
            # This starter app acknowledges submissions. Connect this view to
            # email or a model to persist messages in a real deployment.
            messages.success(request, "Thanks! Your query has been received.")
            return redirect("students_app:contact_us")
        messages.error(request, "Please complete every field before submitting.")

    return render(request, "students_app/contact_us.html")


def faq(request):
    return render(request, "students_app/faq.html")
