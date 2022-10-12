# Generated by Django 4.1.1 on 2022-10-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linitapp', '0002_rename_employeeaddress_employee_employeeaddress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=255)),
                ('contact_no', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]