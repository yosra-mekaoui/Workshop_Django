# Generated by Django 4.1.5 on 2023-02-07 09:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_alter_event_eventdate_alter_event_nbrparticipants_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together={('person', 'event')},
        ),
    ]
