from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.username}'


class Bug(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

