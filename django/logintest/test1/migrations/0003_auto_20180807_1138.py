# Generated by Django 2.0.3 on 2018-08-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_test_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='testname',
            field=models.CharField(choices=[('a', 'aaa'), ('b', 'bbb')], max_length=1),
        ),
    ]