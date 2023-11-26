from django.contrib import admin
from .models import EmailVerification, ResetPasswordVerication


admin.site.register([EmailVerification, ResetPasswordVerication])
