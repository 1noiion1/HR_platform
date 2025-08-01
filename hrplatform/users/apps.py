from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from django.db.models.signals import post_save
        from django.contrib.auth import get_user_model
        from .models import Profile, Role

        User = get_user_model()

        def create_user_profile(sender, instance, created, **kwargs):
            if created and not hasattr(instance, 'profile'):
                Profile.objects.create(
                    user=instance,
                    role=Role.CANDIDATE
                )

        post_save.connect(create_user_profile, sender=User)
