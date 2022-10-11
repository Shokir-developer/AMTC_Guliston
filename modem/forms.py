from django import forms
from .models import AmtcModel, AmtcModel_Eski

class AmtcForm(forms.ModelForm):
	class Meta:
		model = AmtcModel
		fields = '__all__'

		widgets = {
		'fio': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter FIO'}),
		'sn': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter SN'}),
		'p1': forms.Select(attrs={'class':'form-control'}),
		'p2': forms.Select(attrs={'class':'form-control'}),
		'p3': forms.Select(attrs={'class':'form-control'}),
		'vlan': forms.Select(attrs={'class':'form-control'})
		}

class AmtcModel_EskiForm(forms.ModelForm):
	class Meta:
		model = AmtcModel_Eski
		fields = '__all__'

		widgets = {
		'fio': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter FIO'}),
		'sn': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter SN'}),
		'p1': forms.Select(attrs={'class':'form-control'}),
		'p2': forms.Select(attrs={'class':'form-control'}),
		'p3': forms.Select(attrs={'class':'form-control'}),
		}
