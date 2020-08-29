from django.forms import forms, Textarea, ModelForm, FileInput
from .models import ImgBank


class ImgBankForm(ModelForm):
    class Meta:
        model = ImgBank
        fields = ["title","image"]
        widgets = {
            "title": Textarea(attrs={
                "class" : "form-control",
                "placeholder" : "Напишите комментарий",
            }),
            "image": FileInput(attrs={
                "class": "custom-file-input",
                "onchange":"changelabel();",
            }),
        }