from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests

# Función para cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('home')

# Frases de referencia para cada casa
HOUSE_REFERENCES = {
    'Gryffindor': '¡Los valientes y audaces siempre prosperan!',
    'Slytherin': 'Ambición y astucia, el camino al poder.',
    'Ravenclaw': 'La inteligencia y el conocimiento nos guían.',
    'Hufflepuff': 'Lealtad y trabajo duro son nuestro sello.',
}

# Dashboard principal
@login_required
def dashboard(request):
    house = request.user.profile.house  # La casa del usuario
    context = {
        'house': house,
        'reference': HOUSE_REFERENCES.get(house, 'Bienvenido al Mundo Mágico'),
    }
    return render(request, 'main/dashboard.html', context)

# Vista de personajes con filtro vivos/muertos
@login_required
def characters(request):
    house = request.user.profile.house
    alive_filter = request.GET.get('alive', 'true') == 'true'

    response = requests.get(f'https://hp-api.onrender.com/api/characters/house/{house.lower()}')
    characters = response.json()
    filtered_characters = [char for char in characters if char['alive'] == alive_filter]

    context = {
        'characters': filtered_characters,
        'house': house,
        'alive': alive_filter,
    }
    return render(request, 'main/characters.html', context)

# Vista de hechizos
@login_required
def spells(request):
    response = requests.get('https://hp-api.onrender.com/api/spells')
    spells = response.json()
    return render(request, 'main/spells.html', {'spells': spells})
