from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from main.forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'main/house_result.html', {'house': user.profile.house})
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def validate_username(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        if not username:
            return JsonResponse({'error': 'Este campo es obligatorio.'})
        if len(username) > 50:
            return JsonResponse({'error': 'Debe tener 50 caracteres o menos.'})
        if not username.isalnum() and not all(c in "@./+/-/_" for c in username):
            return JsonResponse({'error': 'Solo se permiten letras, números y los caracteres @/./+/-/_.'})
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'El nombre de usuario ya existe.'})
        return JsonResponse({'valid': True})
    return JsonResponse({'error': 'Método inválido.'}, status=400)

def validate_password(request):
    if request.method == "POST":
        password = request.POST.get('password', '')
        if not password:
            return JsonResponse({'error': 'Este campo es obligatorio.'})
        if len(password) < 5:
            return JsonResponse({'error': 'La contraseña debe tener al menos 5 caracteres.'})
        return JsonResponse({'valid': True})
    return JsonResponse({'error': 'Método inválido.'}, status=400)

def validate_email(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        if not email:
            return JsonResponse({'error': 'Este campo es obligatorio.'})
        if len(email) > 50:
            return JsonResponse({'error': 'Debe tener 50 caracteres o menos.'})
        if not email.endswith('@gmail.com') and not email.endswith('@hotmail.com'):
            return JsonResponse({'error': 'Por favor, ingresa un correo válido.'})
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'El correo electrónico ya está registrado.'})
        return JsonResponse({'valid': True})
    return JsonResponse({'error': 'Método inválido.'}, status=400)