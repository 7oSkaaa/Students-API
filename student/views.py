from django.shortcuts import render
from django.http import JsonResponse
import json

# read the data from the file
def read(file):
    with open(file, 'r') as openfile:
        return json.load(openfile, strict=False)
    
    
# write the data to the file
def write(file, data):
    with open(file, 'w') as openfile:
        json.dump(data, openfile)


# for get and post request
def get_post(request):
    file = 'student/db.json'
    students = read(file)
    if request.method == 'GET':
        return JsonResponse(data=students, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body, strict=False)
        students.append(data)
        write(file, students)
        return JsonResponse(data=students, safe=False)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)


# for put and delete request
def put_delete(request, id):
    file = 'student/db.json'
    students = read(file)
    if request.method == 'PUT':
        for i in range(len(students)):
            if students[i]['id'] == id:
                students[i] = json.loads(request.body, strict=False)
                write(file, students)
                return JsonResponse(data=students, safe=False)
        return JsonResponse({"message": "Student not found"}, status=404)
    elif request.method == 'DELETE':
        for i in range(len(students)):
            if students[i]['id'] == id:
                students.pop(i)
                write(file, students)
                return JsonResponse(data=students, safe=False)
        return JsonResponse({"message": "Student not found"}, status=404)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)