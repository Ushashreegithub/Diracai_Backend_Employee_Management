import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from django.conf import settings

db = settings.DATABASES["default"]

print("Django database configuration:")
print("ENGINE :", db.get("ENGINE"))
print("NAME   :", db.get("NAME"))
print("USER   :", db.get("USER"))
print("HOST   :", db.get("HOST"))
print("PORT   :", db.get("PORT"))
