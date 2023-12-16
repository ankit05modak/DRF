from django.shortcuts import render
from django.http import JsonResponse
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
import io
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(["POST", "GET"])
def student_detail(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(request.body)
        python_Data = JSONParser().parse(stream)
        ser = StudentSerializer(data=python_Data)
        if ser.is_valid():
            ser.save()
            return Response({"message": "Data Created"})
        return Response(ser.errors)
    if request.method == "GET":
        request_body = request.body
        print(request_body)
        if request_body:
            stream = io.BytesIO(request_body)
            python_data = JSONParser().parse(stream)
            print(python_data, type(python_data))
            id = python_data.get('id', None)
            if id is not None:
                student_obj = Student.objects.get(id=id)
                print("object Found")
            return Response({"msg": "Hit"})
        student_object = Student.objects.all()
        student_serializer = StudentSerializer(student_object, many=True)
        return JsonResponse(student_serializer.data, safe=False)


@api_view(["POST"])
def student_update(request):
    if request.method == "POST":
        request_body = request.body
        print(request_body)
        stream = io.BytesIO(request_body)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id:
            student_obj = Student.objects.get(id=id)
            ser = StudentSerializer(student_obj, data=python_data, partial=True)
            if ser.is_valid():
                ser.save()
                res = {"msg": "success"}
                return Response(res)
            return Response(ser.errors)
        return Response({"msg": "id not present"})
    

@api_view(["POST"])
def student_delete(request):
    if request.method == "POST":
        request_body = request.body
        stream = io.BytesIO(request_body)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({"msg": "success"})









def newfunc2():
    return 1 + 2s

