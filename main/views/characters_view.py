import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def characters(request):
    user_profile = request.user.profile 
    house = user_profile.house  

    alive = request.GET.get('alive')  

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
        'house': house,  
        'alive': alive,  
    }
    return render(request, 'main/characters.html', context)
