# Generated migration to add all resume templates

from django.db import migrations

def create_all_templates(apps, schema_editor):
    ResumeTemplate = apps.get_model('resume_builder', 'ResumeTemplate')
    
    # Create Classic template
    classic_template = ResumeTemplate.objects.create(
        name='Classic Professional',
        description='A traditional, clean resume template with classic typography and formal layout. Perfect for conservative industries and traditional roles.',
        format_type='CLASSIC',
        is_active=True,
        version=1
    )
    
    # Create Creative template
    creative_template = ResumeTemplate.objects.create(
        name='Creative Designer',
        description='A vibrant, modern template with sidebar layout and visual elements. Ideal for creative professionals, designers, and marketing roles.',
        format_type='CREATIVE',
        is_active=True,
        version=1
    )
    
    # Create Technical template
    technical_template = ResumeTemplate.objects.create(
        name='Technical Engineer',
        description='A code-inspired template with monospace fonts and technical styling. Perfect for software engineers, developers, and IT professionals.',
        format_type='TECHNICAL',
        is_active=True,
        version=1
    )

def reverse_all_templates(apps, schema_editor):
    ResumeTemplate = apps.get_model('resume_builder', 'ResumeTemplate')
    ResumeTemplate.objects.filter(
        name__in=['Classic Professional', 'Creative Designer', 'Technical Engineer']
    ).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0002_add_modern_template'),
    ]

    operations = [
        migrations.RunPython(create_all_templates, reverse_all_templates),
    ]
