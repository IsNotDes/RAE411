from django.shortcuts import render
from django.http import JsonResponse
from messageapp.models import Message

def send_message(request):
    if request.method == 'POST':
        sender = request.POST['sender']
        receiver = request.POST['receiver']
        msg = request.POST['msg']
        Message.objects.create(sender=sender, receiver=receiver, message=msg)
        return render(request, 'message_sent.html', {'receiver': receiver})

    return render(request, 'send_message.html')

def get_messages(request):
    if request.method == 'GET':
        sender = request.GET.get('sender', '')
        messages = Message.objects.filter(sender=sender).order_by('-id')[:20]
        return render(request, 'view_messages.html', {'messages': messages, 'sender': sender})
