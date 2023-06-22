from django import forms
from speakers.models import Speaker

class SpeakerForm (forms.ModelForm):
    class Meta:
        model = Speaker
        fields = "__all__"
