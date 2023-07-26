from django.db import models
from django.contrib.auth.models import AbstractUser


class UsersModel(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name="昵称", default='')
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default='', verbose_name="性别")
    telephone = models.CharField(max_length=11, verbose_name='电话', null=True, blank=True, default='')
    is_ban = models.BooleanField(verbose_name="借书状态", null=False, default=False)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname
