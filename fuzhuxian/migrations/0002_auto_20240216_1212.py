# Generated by Django 3.2.24 on 2024-02-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuzhuxian', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('n', '未开始'), ('a', '已解决'), ('i', '正在进行')], default='n', help_text='状态', max_length=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text='标签名称', max_length=200, verbose_name='标签名称'),
        ),
    ]
