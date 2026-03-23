import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

def setup_social():
    # 1. Setup Site
    site, created = Site.objects.get_or_create(id=1, defaults={'domain': '127.0.0.1:8000', 'name': '127.0.0.1'})
    if not created:
        site.domain = '127.0.0.1:8000'
        site.name = '127.0.0.1'
        site.save()
    print(f"Site configured: {site.domain}")

    # 2. Setup Google App Placeholder
    google_app, created = SocialApp.objects.get_or_create(
        provider='google',
        name='Google Login',
        defaults={
            'client_id': 'YOUR_GOOGLE_CLIENT_ID',
            'secret': 'YOUR_GOOGLE_SECRET',
        }
    )
    google_app.sites.add(site)
    print(f"Google App {'created' if created else 'already exists'}.")

    # 3. Setup GitHub App Placeholder
    github_app, created = SocialApp.objects.get_or_create(
        provider='github',
        name='GitHub Login',
        defaults={
            'client_id': 'YOUR_GITHUB_CLIENT_ID',
            'secret': 'YOUR_GITHUB_SECRET',
        }
    )
    github_app.sites.add(site)
    print(f"GitHub App {'created' if created else 'already exists'}.")

if __name__ == "__main__":
    setup_social()
    print("\nSocial Login placeholders created! You can now access the login page.")
    print("Remember to update the Client ID and Secret in the Admin Panel.")
