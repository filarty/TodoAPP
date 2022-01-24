from django import forms


class FormList(forms.Form):
    form_task = forms.CharField(widget=forms.TextInput(attrs={'size': '40', 'class': 'form'}))
