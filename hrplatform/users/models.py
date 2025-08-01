from django.db import models
from django.conf import settings


class Role(models.TextChoices):
    CANDIDATE = 'candidate', 'Кандидат'
    HR = 'hr', 'HR-менеджер'
    ADMIN = 'admin', 'Администратор'

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CANDIDATE
    )

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"