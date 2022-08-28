from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    OWNER = 0
    CAMERA = 1
    GUEST = 2

    NOTE = (
        (OWNER, 'owner'),
        (CAMERA, 'camera'),
        (GUEST, 'guest'),
    )

    role = models.IntegerField(choices=NOTE, verbose_name='role')


class Meeting(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='meeting owner')
    url = models.CharField(max_length=300, verbose_name='meeting link')
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='meeting start time')
    end_time = models.DateTimeField(blank=True, null=True)


class MeetingImages(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, verbose_name='meeting')
    image = models.ImageField(upload_to='meeting_images', verbose_name='meeting image', blank=True)


class UsersInMeeting(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
