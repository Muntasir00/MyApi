# Generated by Django 3.2.8 on 2021-12-02 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostsRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.BigIntegerField(default=0)),
                ('dislikes', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_body', models.TextField(max_length=1000)),
                ('rates', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.postsrates')),
            ],
        ),
    ]
