# Student Corner Django app

A standalone Django app for a student information site. It provides five URL patterns, five separate page templates, and a contact form with Name, Email, Subject, Query, and Mobile fields.

## Add it to a Django project

1. Copy the `students_app` folder into the Django project.
2. Add `students_app` to `INSTALLED_APPS` in settings.py.
3. Include the app URLs in the project urls.py:

```python
from django.urls import include, path

urlpatterns = [path("", include("students_app.urls"))]
```

4. Keep Django templates, static files, messages, and CSRF middleware enabled.
5. Run `python manage.py runserver`.

## Pages

| Page | URL | View |
| --- | --- | --- |
| Home | `/` | `home` |
| About Us | `/about-us/` | `about_us` |
| Content | `/content/` | `content` |
| Contact Us | `/contact-us/` | `contact_us` |
| FAQ | `/faq/` | `faq` |

The contact form currently validates that all five fields are present and displays a confirmation. Connect it to email or a model to retain submissions.
