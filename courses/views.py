from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Course, Task, Unit
from .serializers import CourseSerializer, UnitSerializer

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
		return Response({"success": "Course '{}' created successfully".format(courseSaved.title)})

	def put(self, request, pk):
		savedCourse = get_object_or_404(Course.objects.all(), pk=pk)
		data = request.data.get('courses')
		serializer = CourseSerializer(instance=savedCourse, data=data, partial=True)

		if serializer.is_valid(raise_exception=True):
			courseSaved = serializer.save()

		return Response({"success": "Course '{}' created successfully".format(courseSaved.title)})
		
	def delete(self, request, pk):
		course = get_object_or_404(Course.objects.all(), pk=pk)
		course.delete()
		return Response({"message": "Course with id '{}' deleted successfully".format(pk)}, status=204)

	def CheckAnswer(AnswerStudent):
		if AnswerStudent==1:
			return Response({"success": "Okey"})

class ListUnit(APIView):
	def get(self, request):
		units = Unit.objects.all()
		serializer = UnitSerializer(units, many=True)
		return Response({"units": serializer.data})
