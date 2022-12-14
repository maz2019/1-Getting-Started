from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_organizor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    SOURCE_CHOICES = (
        ('YT', 'YouTube'),
        ('G', 'Google'),
        ('NEWL', 'Newletter'),
    )
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    company = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    phone_numer = models.CharField(max_length=20)
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name}{self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name

class Category(models.Model):
    name = models.CharField(max_length=35)
    company = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)