from django.db import models
from .validators import(validate_firstname_length, validate_lastname_length,validate_username_length, validate_username_alphadigits,validate_password_length, validate_password_digit, validate_password_uppercase, validate_phonenumber)




class ScrumyUser(models.Model):
	username = models.CharField(max_length=25, verbose_name= 'User name', validators= [validate_username_length, validate_username_alphadigits])
	first_name = models.CharField(max_length=100, verbose_name='Last name', validators= [validate_lastname_length])
	last_name = models.CharField(max_length=100, verbose_name='First name', validators= [validate_firstname_length])
	password1 = models.CharField(max_length=30, validators=[validate_password_length, validate_password_digit, validate_password_uppercase])
	password2 = models.CharField(max_length=30)
	email = models.EmailField()
	phone_no = models.CharField(max_length= 15, validators= [validate_phonenumber])
	birth_date= models.DateField(verbose_name='What is your birth date?')
	gender= models.CharField(max_length=6)
	location= models.CharField(max_length=100, default = 'Nigeria' )
	roles = (
		(1, 'Developer'),
		(2, 'Admin'),
		(3, 'QA - Quality Analyst'),
		(4, 'Owner'),
	)
	
	scrumy_user_role = models.PositiveSmallIntegerField(choices = roles)


	def __str__(self):
		return '{} {} {}'.format(self.username,self.last_name,self.scrumy_user_role)
	class Meta:
		verbose_name_plural = "Scrumy Users"
		permissions = (
			("anywhere_to_anywhere", "Can move from anywhere to anywhere"),
			 ("DT_to_verify", "Can move from DT to Verify"),
			  ("verify_t0_done", "Can move from verify to Done"),
			   ("WG_to_DT", "Can move from WG to DT"))
		

		


class ScrumyStatus(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Scrumy Status"


class ScrumyGoals(models.Model):
	goals = models.TextField()
	scrumy_user = models.ForeignKey(ScrumyUser, on_delete = models.CASCADE)
	scrumy_status = models.ForeignKey(ScrumyStatus, on_delete = models.CASCADE)	
	def __str__(self):
		return self.goals
	class Meta:
		verbose_name_plural = "Scrumy Goals"		
      	#permissions = (('give_refund','Can move from anywhere to anywhere'),('can_hire','Can move from DT to Verify'),('give_refundss','Can move from verify to Done'),('can_hiredd','Can move from WG to DT')) 
      	#permissions=(('give_refund','Can refund customers'),('can_hire','Can hire employees'))


		

class ScrumyUserJS(models.Model):
	username = models.CharField(max_length=25, verbose_name= 'User name', validators= [validate_username_length, validate_username_alphadigits])
	def __str__(self):
		return self.username
	class Meta:
		verbose_name_plural = "Scrumy Users JS"


class ScrumyStatusJS(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Scrumy Status JS"

class ScrumyGoalsJS(models.Model):
	goals = models.TextField()
	scrumy_user = models.ForeignKey(ScrumyUserJS, on_delete = models.CASCADE, related_name='scrumygoalsjs')
	scrumy_status = models.ForeignKey(ScrumyStatusJS, on_delete = models.CASCADE, related_name='scrumystatusjs')	
	def __str__(self):
		return self.goals
	class Meta:
		verbose_name_plural = "Scrumy Goals JS"	
		