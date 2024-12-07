from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse
from django.shortcuts import render
import json

# HttpResponse example
def http_response_example(request):
    return HttpResponse("<h1>Hello, World! This is HttpResponse</h1>")

# JsonResponse example
def json_response_example(request):
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return JsonResponse(data)

# StreamingHttpResponse example (streaming content as response)
def streaming_response_example(request):
    def generate_large_data():
        for i in range(100):
            yield f"Line {i}\n"
    
    response = StreamingHttpResponse(generate_large_data(), content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename="large_data.txt"'
    return response

# FileResponse example (serving a file)
def file_response_example(request):
    # Assuming you have a file called 'example.txt' in your project folder.
    file_path = 'example4app/static/example.txt'
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='example.txt')
