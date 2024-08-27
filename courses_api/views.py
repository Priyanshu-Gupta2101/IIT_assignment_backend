from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseInstanceViewSet(viewsets.ModelViewSet):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    @action(detail=False, methods=['get'])
    def by_year_semester(self, request, year=None, semester=None):
        instances = CourseInstance.objects.filter(year=year, semester=semester)
        serializer = self.get_serializer(instances, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def instance_detail(self, request, year=None, semester=None, pk=None):
        instance = CourseInstance.objects.get(year=year, semester=semester, course__id=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)