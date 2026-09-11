from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = [
            "name",
            "email",
            "phone",
            "subject",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Your email address",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Your phone number",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "placeholder": "What can we help you with?",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "placeholder": "Tell us how we can help...",
                    "rows": 6,
                }
            ),
        }