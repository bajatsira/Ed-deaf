from django.urls import path
from .views import ListCourse, ListUnit, ListTitle, BarChart

app_name = "courses"
urlpatterns = [
	path('courses/', ListCourse.as_view()),
	path('courses/<int:pk>', ListCourse.as_view()),
	path('units/', ListUnit.as_view()),
	path('title/', ListTitle.as_view()),
	path('level/', BarChart.as_view())
]