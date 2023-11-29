from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo Electronico", widget=forms.TextInput(attrs={'class': 'form-control'}))
    company = forms.CharField(label="Empresa", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Descripcion", widget=forms.Textarea(attrs={'class': 'form-control'}))
