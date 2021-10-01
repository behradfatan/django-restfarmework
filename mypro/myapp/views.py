from rest_framework.response import Response
from rest_framework.decorators import api_view

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