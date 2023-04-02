from django.urls import path
from .views import ListCourse

app_name = "courses"
urlpatterns = [
	path('courses/', ListCourse.as_view()),
]