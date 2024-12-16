from django.shortcuts import render, redirect
from main.forms import RegistrationForm
from main.models import Profile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el usuario y el perfil
            profile = Profile.objects.get(user=user)  # Obtenemos el perfil del usuario
            return render(request, 'main/house_result.html', {'house': profile.house})
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})
