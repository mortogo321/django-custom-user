from django.contrib.auth.models import BaseUserManager
from django.db.models.query import QuerySet


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        results = super().get_queryset(*args, **kwargs)

        return results.filter(role=self.Role.STUDENT)


class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        results = super().get_queryset(*args, **kwargs)

        return results.filter(role=self.Role.TEACHER)
