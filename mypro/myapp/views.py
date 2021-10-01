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