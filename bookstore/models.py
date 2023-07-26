from django.db import models
from users.models import UsersModel
from datetime import datetime


class BookModel(models.Model):
    ids = models.CharField(max_length=50, verbose_name='书籍编码', primary_key=True)
    isbn = models.CharField(max_length=30, verbose_name='ISBN编码', unique=True)
    name = models.CharField(max_length=100, verbose_name='书名', default='', null=False, blank=False)
    press = models.CharField(max_length=100, verbose_name='出版社', default='', null=True, blank=True)
    type = models.CharField(max_length=50, verbose_name='分类', default='', null=False, blank=False)
    price = models.FloatField(verbose_name='定价', default='0.0', null=True, blank=True)
    count = models.IntegerField(verbose_name='数量', default='0', null=False, blank=False)

    class Meta:
        verbose_name = '图书信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s %s" % (self.type, self.name)


class BorrowModel(models.Model):
    book_id = models.ForeignKey(BookModel, verbose_name='书籍编码', on_delete=models.CASCADE)
    user_id = models.ForeignKey(UsersModel, verbose_name='用户信息', on_delete=models.CASCADE)
    borrow_time = models.DateTimeField(verbose_name="借书日期", default=datetime.now)
    return_time = models.DateTimeField(verbose_name="归还日期", null=True, blank=True)

    class Meta:
        verbose_name = '借阅信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s %s" % (self.user_id, self.book_id.name)
