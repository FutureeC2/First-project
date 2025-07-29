from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.Charfield(max_lenght=50, unique=True)
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
     
    def __str__(self):
        return self.name
    

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, black=True)
    
    def has_premission(self, action):
        if not self.role:
            return False
        return {
            'add': self.role.can_add,
            'edit': self.role.can_edit,
            'delete': self.role.can_delete,
        }.get(action, False)