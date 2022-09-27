# Generated by Django 3.2.10 on 2022-01-11 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import private_storage.fields
import private_storage.storage.files
import project.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('google_calendar_id', models.CharField(blank=True, max_length=254, null=True)),
                ('url', models.CharField(blank=True, max_length=254, null=True)),
                ('lawyer_mode', models.BooleanField(default=False)),
                ('meet_start', models.DateTimeField(null=True)),
                ('meet_end', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meet_from_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('closed_description', models.TextField(blank=True, null=True)),
                ('order_number', models.IntegerField(blank=True, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_client', to='client.client')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='TeamType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('role', models.CharField(choices=[('1', 'Reader'), ('2', 'Editor')], default='1', max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('is_removable', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('customer', models.BooleanField(default=False)),
                ('token', models.UUIDField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_project', to='project.project')),
                ('team_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_type', to='project.teamtype')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='TaskDefault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('start_date_plus_day', models.PositiveIntegerField(blank=True, null=True)),
                ('product', models.ManyToManyField(to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'In progress'), ('INCOMPLETE', 'Incomplete'), ('REVIEW', 'Review'), ('COMPLETE', 'Complete')], default='IN_PROGRESS', max_length=254)),
                ('lawyer_mode', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('archived', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_from_user', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_project', to='project.project')),
                ('responsible_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_responsible_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProjectFormDefault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('default_schema', models.JSONField(blank=True, null=True)),
                ('default_meta', models.JSONField(blank=True, null=True)),
                ('default_form', models.BooleanField(default=False)),
                ('start_date_plus_day', models.PositiveIntegerField(blank=True, null=True)),
                ('multiple', models.BooleanField(default=False)),
                ('product', models.ManyToManyField(to='shop.Product')),
                ('team_type', models.ManyToManyField(to='project.TeamType')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('form_schema', models.JSONField(blank=True, null=True)),
                ('form_meta', models.JSONField(blank=True, null=True)),
                ('form_value', models.JSONField(blank=True, null=True)),
                ('locked', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('help_link', models.CharField(blank=True, max_length=254, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_form', to='project.project')),
                ('responsible_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_form_responsible_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('private', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('TASK', 'Task'), ('MEET', 'Meet'), ('NOTE', 'Note'), ('FORM', 'Form')], default='NOTE', max_length=254)),
                ('visible', models.BooleanField(default=True)),
                ('lawyer_mode', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('meet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_meet', to='project.meet')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_project', to='project.project')),
                ('project_form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_project_form', to='project.projectform')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_task', to='project.task')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('url', models.CharField(blank=True, max_length=254, null=True)),
                ('lawyer_mode', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_project', to='project.project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_from_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='meet',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meet_project', to='project.project'),
        ),
        migrations.AddField(
            model_name='meet',
            name='to_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_display_name', models.CharField(max_length=254, null=True)),
                ('action', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('meet_start', models.DateTimeField(null=True)),
                ('meet_end', models.DateTimeField(null=True)),
                ('is_read', models.BooleanField(db_index=True, default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invite_project2', to='project.project')),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invite_recipient2', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('create_date',),
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('project_file', private_storage.fields.PrivateFileField(blank=True, null=True, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to=project.models.get_file_path_default)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_relase', models.BooleanField(default=False)),
                ('meet_record_url', models.CharField(blank=True, max_length=254, null=True)),
                ('lawyer_mode', models.BooleanField(default=False)),
                ('file_type', models.CharField(choices=[('NOTE', 'Note'), ('TASK', 'Task'), ('TASK_NOTE', 'Task note'), ('MESSAGE', 'Message'), ('MEET', 'Meet'), ('MEET_NOTE', 'Meet note'), ('FORM', 'Form'), ('FORM_NOTE', 'Form note'), ('DEFAULT', 'Default')], default='DEFAULT', max_length=254)),
                ('archived', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('meet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_meet', to='project.meet')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_message', to='project.message')),
                ('note', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_note', to='project.note')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_project', to='project.project')),
                ('project_form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_form', to='project.projectform')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_task', to='project.task')),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_from_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentDefault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_document', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_user_document', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_document', to='project.project')),
                ('to_user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('lawyer_mode', models.BooleanField(default=False)),
                ('is_read', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_project', to='project.project')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]