from django import forms

from .models import Persona, Experience


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ("name", "bio", "email", "rrss_1", "rrss_2", "web", "image")


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ("title", "company", "experience", "init_date", "end_date")
