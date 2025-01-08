from django import forms
from .models import Song




class EditSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'starting_date', 'duration','status','notes']

        
        
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control is-valid',
                'id': 'name',
                'required': False
            }),
            'starting_date': forms.DateInput(attrs={
                'class': 'form-control',
                'data-datepicker':'',
                'id': 'date',
                'required': False,
                'placeholder':"dd/mm/yyyy",
                'type':'date',
                'disabled':'disabled'
            }),
            'duration': forms.TimeInput(attrs={
                'class': 'form-control',
                'id': 'duration',
                'required': False,
                'type':'time'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'id': 'status',
                'required': False,
                'type':'select',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'notes',
                'required': False,
                'type':'text',
                'rows':'4',
                'cols':'50'
            }),
        }
    
    


class NewSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'starting_date', 'duration','status','notes']

        
        
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control is-valid',  # Add Bootstrap classes
                'id': 'name',
                'required': True
            }),
            'starting_date': forms.DateInput(attrs={
                'class': 'form-control',
                'data-datepicker':'',
                'id': 'date',
                'required': True,
                'placeholder':"dd/mm/yyyy",
                'type':'date'
                
            }),
            'duration': forms.TimeInput(attrs={
                'class': 'form-control',
                'id': 'duration',
                'required': True,
                'type':'time'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'id': 'status',
                'required': True,
                'type':'select',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'notes',
                'required': True,
                'type':'text',
                'rows':'4',
                'cols':'50'
            }),
        }
        