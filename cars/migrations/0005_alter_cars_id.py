# Generated by Django 3.2.8 on 2021-12-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_delete_storeclosingstock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
