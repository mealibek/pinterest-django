from django.db import models


class EmailVerification(models.Model):
    token = models.CharField('Email Verification Token')
    email = models.EmailField("Email Address", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table = 'email_verification_requests'
        verbose_name_plural = 'Email Verification Requests'


class ResetPasswordVerication(models.Model):
    token = models.CharField('Reset Password Token')
    email = models.EmailField('Email Address', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table = 'reset_password_requests'
        verbose_name_plural = 'Reset Password Requests'
