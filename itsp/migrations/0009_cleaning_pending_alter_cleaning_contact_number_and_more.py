# Generated by Django 4.0.5 on 2022-07-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsp', '0008_alter_cleaning_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleaning',
            name='Pending',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='Contact_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='date',
            field=models.DateField(null=True, verbose_name='Date of cleaning'),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='hostel',
            field=models.CharField(choices=[('Hostel 1', 'Hostel 1'), ('Hostel 2', 'Hostel 2'), ('Hostel 3', 'Hostel 3'), ('Hostel 4', 'Hostel 4'), ('Hostel 5', 'Hostel 5'), ('Hostel 6', 'Hostel 6'), ('Hostel 7', 'Hostel 7'), ('Hostel 8', 'Hostel 8'), ('Hostel 9', 'Hostel 9'), ('Hostel 10', 'Hostel 10'), ('Hostel 11', 'Hostel 11'), ('Hostel 12', 'Hostel 12'), ('Hostel 13', 'Hostel 13'), ('Hostel 14', 'Hostel 14'), ('Hostel 15', 'Hostel 15'), ('Hostel 16', 'Hostel 16'), ('Hostel 17', 'Hostel 17'), ('Hostel 18', 'Hostel 18')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='room',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='time',
            field=models.TimeField(null=True, verbose_name='Time of cleaning'),
        ),
        migrations.AlterField(
            model_name='wingcleaning',
            name='hostel',
            field=models.CharField(choices=[('Hostel 1', 'Hostel 1'), ('Hostel 2', 'Hostel 2'), ('Hostel 3', 'Hostel 3'), ('Hostel 4', 'Hostel 4'), ('Hostel 5', 'Hostel 5'), ('Hostel 6', 'Hostel 6'), ('Hostel 7', 'Hostel 7'), ('Hostel 8', 'Hostel 8'), ('Hostel 9', 'Hostel 9'), ('Hostel 10', 'Hostel 10'), ('Hostel 11', 'Hostel 11'), ('Hostel 12', 'Hostel 12'), ('Hostel 13', 'Hostel 13'), ('Hostel 14', 'Hostel 14'), ('Hostel 15', 'Hostel 15'), ('Hostel 16', 'Hostel 16'), ('Hostel 17', 'Hostel 17'), ('Hostel 18', 'Hostel 18')], max_length=50),
        ),
        migrations.AlterField(
            model_name='wingcleaning',
            name='shift',
            field=models.CharField(choices=[('Morning', 'morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='cleaning',
            unique_together={('hostel', 'date', 'time')},
        ),
    ]