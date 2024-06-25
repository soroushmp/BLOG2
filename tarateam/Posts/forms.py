from django import forms
from .models import Comment ,  CooperationRequest
from django.forms import TextInput, EmailField , NumberInput , DateTimeInput , EmailInput ,Textarea  ,Widget 

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text' , 'email' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control name1'}),
            'text':forms.Textarea(attrs={'class': 'text3 form-control ', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class':'form-control'} )}
        
        
class Form_CooperationRequest(forms.ModelForm):
    class Meta:
        model = CooperationRequest
        # fields = ['name', 'phone_number' , 'email_address' ,'description' ,'date_brd' ]
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control name1', 'placeholder': 'نام خود را وارد کنید'}),
            'phone_number':forms.NumberInput(attrs={'class': 'form-control num1'}),
            # 'description':forms.TextInput(attrs={'class': 'text3 form-control '}),
            'description':forms.Textarea(attrs={'class': 'text3 form-control ', 'rows': 3}),
            'date_brd': forms.TextInput(attrs={'class': 'form-control date1',  "type": "text","id": "date_of_birth", "data-jdp": "", 'placeholder': "", 'data-jdp-only-date': ""}),
            'email_address': forms.EmailInput(attrs={'class':'form-control'} )}
        widgets['date_brd'].attrs['required'] = True
        
    