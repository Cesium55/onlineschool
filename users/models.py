from django.db import models

class Users(models.Model):
    login = models.EmailField('Email')
    password = models.CharField('Пароль', max_length=50, default='')

    def __str__(self) -> str:
        return self.login
    
    class Meta():
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
