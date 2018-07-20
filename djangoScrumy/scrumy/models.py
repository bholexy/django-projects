from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255) 
    first_name = models.CharField(('First Name of User'), blank = True, max_length = 20)
    last_name = models.CharField(('Last Name of User'), blank = True, max_length = 20) 		

    def __str__(self):
        return self.username

    class meta:
    	permissions = (
				("anywhere_to_anywhere", "Can move from anywhere to anywhere"),
				 ("DT_to_verify", "Can move from DT to Verify"),
				  ("verify_t0_done", "Can move from verify to Done"),
				   ("WG_to_DT", "Can move from WG to DT"),)



class ScrumyStory(models.Model):
	story = models.CharField(max_length=25, verbose_name= 'User name')
	def __str__(self):
		return self.story
	class Meta:
		verbose_name_plural = "Scrumy Story"




class ScrumyStatus(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Scrumy Status"


class ScrumyGoals(models.Model):
	goals = models.TextField()
	scrumy_status = models.ForeignKey(ScrumyStatus, related_name='scrumy_goals',  on_delete = models.CASCADE)	
	scrumy_user = models.ForeignKey(CustomUser, related_name='scrumy_goals', on_delete = models.CASCADE)	
	def __str__(self):
		return self.goals
	class Meta:
		verbose_name_plural = "Scrumy Goals"	