import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

def set_credentials():
    username = 'Admin'
    password = 'Admin'
    
    user, created = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    
    if created:
        print(f"Superuser '{username}' created successfully.")
    else:
        print(f"Password for superuser '{username}' updated successfully.")

if __name__ == "__main__":
    set_credentials()
