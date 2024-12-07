from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<html><head><title>Hello World</title></head><body><h1 style='color:blue;'>Hello, World!</h1></body></html>")