from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status
from rest_framework.permissions import IsAdminUser
@api_view()
def hello(request):
    return Response({"message": "welcome"})


@api_view(["post", "GET"])
def welcome(request):
    if request.method == "POST":
        name = request.data["name"]
        return Response({"message": f' welcome {name}'})
    else:
        return Response({"message": "welcome"})


@api_view()
def show_person(request):
    person = Person.objects.all()
    ser = PersonSerializer(person, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)

@api_view()
def person(request, id):
    try:
        person = Person.objects.get(id=id)
    except person.DoesNotExist():
        return Response({"error": "person does not exist"}, status=status.HTTP_400_NOT_FOUND)
    ser = PersonSerializer(person)
    return Response(ser.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes(['IsAdminUser'])
def create_person(request):
    create = PersonSerializer(data=request.data)
    if create.is_valid():
        create.save()
    else:
        return Response(create.errors, status=status.HTTP_404_NOT_FOUND)