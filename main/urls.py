from django.urls import path
from main.views.home_view import home
from main.views.register_view import register, validate_username, validate_password,validate_email
from main.views.login_view import user_login,check_username,check_password
from main.views.dashboard_view import dashboard, spells, logout_view
from main.views.characters_view import characters
from main.views.staff_view import staff


urlpatterns = [
    # Página principal
    path('', home, name='home'),
    
    # Registro de usuario
    path('register/', register, name='register'),
    path('check-username/', check_username, name='check_username'),
    path('validate-username/', validate_username, name='validate_username'),
    path('validate-password/', validate_password, name='validate_password'),
    path('validate_email/', validate_email, name='validate_email'),
    # Login de usuario
    path('login/', user_login, name='login'),
    path('check-username/', check_username, name='check_username'),  
    path('check-password/', check_password, name='check_password'),

    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),
    
    # Vistas de personajes y hechizos
    path('dashboard/characters/', characters, name='characters'),
    path('dashboard/spells/', spells, name='spells'),
    
    # Cerrar sesión
    path('logout/', logout_view, name='logout'),    
    path('staff/', staff, name='staff'),

  

]
