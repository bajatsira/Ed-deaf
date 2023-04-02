from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer

class ListCourse(APIView):
	def get(self, request):
		courses = Course.objects.all()
		serializer = CourseSerializer(courses, many=True)
		return Response({"courses": serializer.data})

	def post(self, request):
		course = request.data.get('courses')
		serializer = CourseSerializer(data=course)
		if serializer.is_valid(raise_exception=True):
			courseSaved = serializer.save()
		return Response({"success": "Course '{}' created successfully".format(course_saved.title)})

