from django import forms
from django.forms import ModelForm
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('activity', 'description', 'image_url', 'image')

        labels = {
            'activity': '',
            'description': '',
            'image_url': 'Add image',
            'image': ''

        }

        widgets = {
            'activity': forms.TextInput(
                attrs={
                'class': 'form-control', 
                'placeholder': 'To do'}
                ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Description'}
                    ),
            'image_url': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'url'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'No file Chosen'
                }
            )

        }