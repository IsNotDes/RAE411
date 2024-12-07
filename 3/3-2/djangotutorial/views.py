from django.shortcuts import render

def hello_world_mvt(request):
    return render(request, 'hello_world.html')
