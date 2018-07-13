from django import forms

class reservaForm(forms.Form):
    fecha = forms.DateField(widget=forms.SelectDateWidget())
    horaInicio = forms.TimeField()
    horaFinal = forms.TimeField()