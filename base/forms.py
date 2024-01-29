from django import forms

from base.models import ContactForm


class ContactCreateForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", }), required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "cols": "30", "rows": "7"}),
                              required=True)

    class Meta:
        model = ContactForm
        fields = [
            "first_name",
            "last_name",
            "email",
            "subject",
            "message",
        ]
