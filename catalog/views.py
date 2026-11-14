from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(f"Получено сообщение от {name}: {message}")

        context = {
            'success': True,
            'sender_name': name
        }
        return render(request, 'contacts.html', context)

    return render(request, 'contacts.html')
