# Generated by Django 4.1.6 on 2023-02-18 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=200)),
                ('pet_name', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('animal_type', models.CharField(choices=[('DO', 'Dog'), ('CA', 'Cat'), ('BI', 'Bird'), ('RE', 'Reptile'), ('OT', 'Other')], default='OT', max_length=2)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.owner')),
            ],
            options={
                'ordering': ['pet_name'],
            },
        ),
    ]
