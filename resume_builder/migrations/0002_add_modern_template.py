# Generated migration to add the modern resume template

from django.db import migrations

def create_modern_template(apps, schema_editor):
    ResumeTemplate = apps.get_model('resume_builder', 'ResumeTemplate')
    
    # Create the modern template from Assignment 4
    modern_template = ResumeTemplate.objects.create(
        name='Modern Professional',
        description='A modern, professional resume template with gradient header and asymmetric layout. Features clean typography, color-coded sections, and excellent print compatibility.',
        format_type='MODERN',
        is_active=True,
        version=1
    )

def reverse_modern_template(apps, schema_editor):
    ResumeTemplate = apps.get_model('resume_builder', 'ResumeTemplate')
    ResumeTemplate.objects.filter(name='Modern Professional').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_modern_template, reverse_modern_template),
    ]
