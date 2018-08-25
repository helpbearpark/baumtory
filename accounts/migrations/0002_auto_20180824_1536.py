# Generated by Django 2.0.7 on 2018-08-24 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='clubs/%Y/%m/%d/')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Club_Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=''),
        ),
        migrations.AddField(
            model_name='club_relation',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_user', to='accounts.Profile'),
        ),
        migrations.AddField(
            model_name='club_relation',
            name='to_club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joiner_user', to='accounts.Club'),
        ),
        migrations.AlterUniqueTogether(
            name='club_relation',
            unique_together={('from_user', 'to_club')},
        ),
    ]