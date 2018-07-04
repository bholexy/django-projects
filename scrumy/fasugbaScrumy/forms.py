from .models import ScrumyUser, ScrumyGoals, ScrumyStatus
from django import forms


GENDER_CHOICES= [
    ('First choice', 'I am...'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ]

COUNTRY_CHOICES= [
    ('France', 'France'),
    ('Germany', 'Germany'),
    ('Italy', 'Italy'),
    ('United States', 'United States'),
    ]

YEARS= [x for x in range(1920,2017)]







class ScrumyUserForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
	birth_date= forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
	gender= forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
	location= forms.CharField(widget=forms.Select(choices=COUNTRY_CHOICES))
	class Meta:
		model = ScrumyUser
		fields= ["username","first_name", "last_name", "password1", "password2","scrumy_user_role", 
				 "birth_date", "gender", "phone_no", "email", "location"]


class ScrumyGoalsForm(forms.ModelForm):
	class Meta:
		model = ScrumyGoals
		fields = [
			'goals'
		]
			

class ScrumyStatusForm(forms.ModelForm):
	class Meta:
		model = ScrumyStatus
		fields = [
			'name'
		]





