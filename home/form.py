from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

from django import forms

from django.core.validators import validate_slug
from django.forms import ModelForm, TextInput, CharField, ImageField, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from .models import Request, Namecompany, Namecl, User, viewblogs, Mohmed, Comment, Startup
from static import edit


# Create your forms here.

class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('edit/css.css',)
        }


class CommentForm(ModelForm):
    class Meta:
        model = Request
        fields = '__all__'


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class MohmedForm(ModelForm):
    class Meta:
        model = Mohmed
        fields = ['name', 'email', 'img', 'phone', 'brith']
        widgets = {

            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),
            'email': TextInput(attrs={
                'class': "form-control",

                'placeholder': 'Email',
                'style': 'height: 30px; width: 300px; border: 2px solid grey; padding: 7px; margin-top: 20px; margin-bottom: 10px; font-size: 20px;',
            }),
            'phone': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'pohon',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),
            'brith': DatePickerInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'pohon',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),

        }

class StartupForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = ['name', 'industry', 'year_founded', 'about', 'website', 'logo', 'address', 'employee_count', 'founder', 'founder_email', 'founder_phone', 'video_pitch']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'max-width: 300px; height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;'
            })
class numcilnt(ModelForm):
    class Meta:
        model = Namecl
        fields = ['name', 'email', 'img', 'pohon', 'born']
        widgets = {

            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),
            'email': TextInput(attrs={
                'class': "form-control",

                'placeholder': 'Email',
                'style': 'height: 30px; width: 300px; border: 2px solid grey; padding: 7px; margin-top: 20px; margin-bottom: 10px; font-size: 20px;',
            }),
            'pohon': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'pohon',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),
            'born': DatePickerInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'pohon',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),

        }


class postmeta(ModelForm):
    class Meta:
        model = viewblogs
        fields = ("title", "img", "body", "catag", "active")
        widgets = {

            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),
            'body ': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),

            'pohon': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'pohon',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),
            'born': DatePickerInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'pohon',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),

        }


class numcom(ModelForm):
    class Meta:
        model = Namecompany
        fields = '__all__'


class NewUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'style': 'max-width: 300px;',
        'placeholder': 'Password1',
        'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password2',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }))
    class Meta:
        model = User
        fields = ("username","email",)
        widgets = {

            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'name',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Egmail',
                'style': 'height: 30px; width: 250px; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px;',
            }),



        }


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
