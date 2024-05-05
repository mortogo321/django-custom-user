from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Student, StudentProfile, Teacher, TeacherProfile


@receiver(post_save, sender=Student)
def create_user_profile(sender, instant, created, **kwargs):
    if created and instant.role == "STUDENT":
        StudentProfile.objects.create(user=instant)


@receiver(post_save, sender=Teacher)
def create_user_profile(sender, instant, created, **kwargs):
    if created and instant.role == "TEACHER":
        TeacherProfile.objects.create(user=instant)
