import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def characters(request):
    # Obtiene la casa desde el perfil del usuario autenticado
    user_profile = request.user.profile  # Asume que Profile está relacionado con User
    house = user_profile.house  # La casa del usuario actual

    alive = request.GET.get('alive')  # Obtiene el estado del toggle (vivo/muerto)

    # URL de la API dinámica según la casa del usuario
    api_url = f"https://hp-api.onrender.com/api/characters/house/{house.lower()}"

    response = requests.get(api_url)
    characters = []

    if response.status_code == 200:
        all_characters = response.json()
        # Filtra personajes según el estado del toggle switch
        if alive == "true":
            characters = [char for char in all_characters if char.get('alive') is True]
        elif alive == "false":
            characters = [char for char in all_characters if char.get('alive') is False]
        else:
            characters = all_characters

    context = {
        'characters': characters,
        'house': house,  # La casa del usuario actual
        'alive': alive,  # Estado del filtro
    }
    return render(request, 'main/characters.html', context)
