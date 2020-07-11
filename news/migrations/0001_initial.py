# Generated by Django 3.0.5 on 2020-07-09 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='news.Category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]