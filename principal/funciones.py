from django.contrib.auth.models import User

def generarPin():
    random_number = User.objects.make_random_password(length=4, allowed_chars='123456789')
    return random_number