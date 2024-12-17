from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Vista principal de login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

# Nueva vista para validar si el usuario existe
def check_username(request):
    if request.method == "POST":
        username = request.POST.get('username')
        exists = User.objects.filter(username=username).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'error': 'Método inválido'}, status=400)

# Nueva vista para validar la contraseña
def check_password(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({'valid': True})
        return JsonResponse({'valid': False})
    return JsonResponse({'error': 'Método inválido'}, status=400)
