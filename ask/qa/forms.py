from django import forms
from django.contrib.auth.models import User

from .models import Question, Answer


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text')        

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text', 'question')


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
