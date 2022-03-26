from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username')
        parser.add_argument('password')
    def handle(self, *args, **options):
        if len(args) != 2:
            raise CommandError('need exactly two arguments for username and password')
        username, password = args

        u, created = User.objects.get_or_create(username=username)
        if created:
            u.is_superuser = True
            u.is_staff = True
            u.set_password(password)
            u.save()
        else:
            raise CommandError("user '%s' already exist" % username)

        return "Password changed successfully for user '%s'" % u.username
# def createSuperUser(username, password, email = "", firstName = "", lastName = ""):
#     invalidInputs = ["", None]
#
#     if username.strip() in invalidInputs or password.strip() in invalidInputs:
#         return None
#
#     user = User(
#         username = username,
#         email = email,
#         first_name = firstName,
#         last_name = lastName,
#     )
#     user.set_password(password)
#     user.is_superuser = True
#     user.is_staff = True
#     user.save()