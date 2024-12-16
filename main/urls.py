from django.urls import path
from main.views.home_view import home
from main.views.register_view import register
from main.views.login_view import user_login
from main.views.dashboard_view import dashboard, spells, logout_view
from main.views.characters_view import characters
from main.views.staff_view import staff


urlpatterns = [
    # Página principal
    path('', home, name='home'),
    
    # Registro de usuario
    path('register/', register, name='register'),
    
    # Login de usuario
    path('login/', user_login, name='login'),
    
    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),
    
    # Vistas de personajes y hechizos
    path('dashboard/characters/', characters, name='characters'),
    path('dashboard/spells/', spells, name='spells'),
    
    # Cerrar sesión
    path('logout/', logout_view, name='logout'),    
    path('staff/', staff, name='staff'),

  

]
