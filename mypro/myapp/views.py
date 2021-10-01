from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PersonSerializer

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
    return Response(ser.data)

@api_view()
def person(request, id):
    try:
        person = Person.objects.get(id=id)
    except person.DoesNotExist():
        return Response({"error": "person does not exist"})
    ser = PersonSerializer(person)
    return Response(ser.data)
