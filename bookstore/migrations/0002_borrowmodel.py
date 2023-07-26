# Generated by Django 4.2.3 on 2023-07-22 20:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='借书日期')),
                ('return_time', models.DateTimeField(blank=True, null=True, verbose_name='归还日期')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.bookmodel', verbose_name='书籍编码')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户信息')),
            ],
            options={
                'verbose_name': '借阅信息',
                'verbose_name_plural': '借阅信息',
            },
        ),
    ]
