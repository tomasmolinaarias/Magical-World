from django import forms
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    HOUSE_QUESTIONS = [
        ('Gryffindor', 'Prefieres la valentía y el coraje'),
        ('Slytherin', 'Valoras la ambición y la astucia'),
        ('Ravenclaw', 'Prefieres la inteligencia y la sabiduría'),
        ('Hufflepuff', 'Valoras la lealtad y el trabajo duro'),
    ]
    house_question = forms.ChoiceField(
        choices=HOUSE_QUESTIONS, 
        widget=forms.RadioSelect, 
        label="¿Qué cualidad valoras más?"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            # Crear el perfil del usuario y guardar la casa seleccionada
            Profile.objects.create(user=user, house=self.cleaned_data['house_question'])
        return user
