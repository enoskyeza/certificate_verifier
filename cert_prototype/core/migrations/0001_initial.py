# Generated by Django 4.2.11 on 2024-03-06 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=10, unique=True)),
                ('pay_status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending')], max_length=20)),
                ('course_status', models.CharField(choices=[('complete', 'Complete'), ('enrolling', 'Enrolling')], max_length=20)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issuance', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
        ),
    ]