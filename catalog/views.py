from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    print(f"--- Тип запроса: {request.method} ---")
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение {message} получено.")
    return render(request, 'contacts.html')
