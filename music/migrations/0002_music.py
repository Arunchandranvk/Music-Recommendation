# Generated by Django 5.0.3 on 2024-03-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='music')),
                ('img', models.ImageField(upload_to='thumbnail')),
                ('type', models.CharField(choices=[('Angry', 'Angry'), ('Disgust', 'Disgust'), ('Fear', 'Fear'), ('Happy', 'Happy'), ('Neutral', 'Neutral'), ('Sad', 'Sad'), ('Surprise', 'Surprise')], max_length=100)),
            ],
        ),
    ]
