# Generated by Django 4.2.2 on 2023-06-13 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0005_auto_20160629_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepoShareInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_id', models.CharField(db_index=True, max_length=36)),
                ('path', models.TextField()),
                ('permission', models.CharField(choices=[('r', 'read only'), ('rw', 'read and write')], default='r', max_length=50)),
                ('invitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repo_share', to='invitations.invitation')),
            ],
            options={
                'db_table': 'repo_share_invitation',
            },
        ),
    ]