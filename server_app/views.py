from django.http import JsonResponse
from django.shortcuts import render

def server_app(request):
    return render(request, 'server_app/server_app.html', {})


def check(request):
    if request.method == "POST":
        with open("sensor", "w")as f:
            f.write("0")

    with open("sensor", "r")as f:
        vib = f.read() == "1"

    return JsonResponse(data={"vib": vib})
