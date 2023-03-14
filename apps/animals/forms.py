from django import forms

from apps.animals.models import Animal


class AnimalByOwnerForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = (
            "name",
            "age",
            "kind",
            "avatar",
            "owner",
        )
        widgets = {
            "owner": forms.HiddenInput(),
        }
