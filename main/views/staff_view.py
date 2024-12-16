import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def staff(request):
    alive = request.GET.get('alive')  # Filtro de vivos/muertos
    api_url = "https://hp-api.onrender.com/api/characters/staff"

    response = requests.get(api_url)
    staff_members = []

    if response.status_code == 200:
        all_staff = response.json()
        if alive == "true":
            staff_members = [staff for staff in all_staff if staff.get('alive') is True]
        elif alive == "false":
            staff_members = [staff for staff in all_staff if staff.get('alive') is False]
        else:
            staff_members = all_staff

    context = {
        'staff_members': staff_members,
        'alive': alive
    }
    return render(request, 'main/staff.html', context)
