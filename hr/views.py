from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def hrAuth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        context = {
            'error': None
        }

        if user is not None:
            login(request, user)
            return redirect('/employees/')
        else:
            context['error'] = 'Invalid username or password'
            return render(request, 'index.html', context)

    return render(request, 'index.html')
