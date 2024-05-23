from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# 기본적인 username, firstName, lastName, email, password 등록일자 등을
# 나타내는 메서드
# settings.py -> AUTH_USER_MODEL = 'accounts.User'
# 이거 해줘야 한다.