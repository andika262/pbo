from django.forms import ModelForm
from django import forms
from app_utspbo.models import *

class formJurnal(ModelForm):
    class Meta:
        model = home
        fields = '__all__'

        widgets = {
            'nama_wisata' : forms.TextInput({'class': 'form-control','placeholder': 'Nama Wisata', 'required' : 'required' }),
            'deskripsi' : forms.TextInput({'class': 'form-control','placeholder': 'Deskripsi', 'required' : 'required' }),
            'nama_daerah' : forms.TextInput({'class': 'form-control','placeholder': 'Nama Daerah', 'required' : 'required' }),
            'foto' : forms.FileInput({'class':'form-control', 'placeholder':'Foto Kost', 'required' : 'required'}),
            'coord' : forms.Select({'class':'form-control', 'placeholder':'Kordinat X', 'required' : 'required'}),
        }

class formpeta(ModelForm):
    class Meta:
        model = koor
        fields = '__all__'
        widgets = {
            'nama' : forms.TextInput({'class':'form-control', 'placeholder':'Nama Daerah', 'required' : 'required'}),
            'coordX' : forms.TextInput({'class':'form-control', 'placeholder':'Kordinat X', 'required' : 'required'}),
            'coordY' : forms.TextInput({'class':'form-control', 'placeholder':'Kordinat Y', 'required' : 'required'}),
        }
