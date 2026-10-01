from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


class StudentListView(APIView):

    def get(self, request):
        students = Student.objects.all()
        print(students)
        serializer = StudentSerializer(students, many=True)
        print(serializer.data)

        return Response(data={"data": serializer.data}, status=200)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data": serializer.data}, status=201)
        else:
            return Response(data={"errors": serializer.errors}, status=400)