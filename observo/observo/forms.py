from django import forms
from .models import Animal, Observ
from django.contrib.auth.models import User

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nom_commun', 'nom_savant', 'embranchement', 'classe', 'ordre', 'sous_ordre', 'famille', 'genre', 'statut_iucn', 'description']
        labels = {'nom_commun': 'Nom commun', 
                  'nom_savant' : 'Nom savant', 
                  'embranchement':'Embranchement', 
                  'classe' : 'Classe', 
                  'ordre': 'Ordre', 
                  'sous_ordre': 'sous-ordre', 
                  'famille': 'Famille', 
                  'genre': 'Genre', 
                  'statut_iucn': 'Satut IUCN',
                  'description' : 'Description'
            
        }

class ObservForm(forms.ModelForm):
    class Meta:
         model = Observ
         fields = [
             'animal',
             'date_heure',
             'latitude',
             'description'
         ]
         labels = {
             'animal':'animal observé',
             'date_heure': 'date et heure',
             'latitude': 'latitude',
             'description':'description',
         }
class SignUpForm(forms.ModelForm):
    ROLE_CHOICES = (
        ("user", "Utilisateur"),
        ("admin", "Administrateur"),
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        label="Rôle",
        widget=forms.RadioSelect
    )

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "email")

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            raise forms.ValidationError("Les mots de passe ne correspondent pas")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
