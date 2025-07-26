# resume_builder/forms.py
from django import forms
from .models import (
    ResumeTemplate, Resume, ResumeSection, WorkExperience,
    TechnicalSkill, Education, Technology, Project,
    Certification, Award, Language
)

class ResumeTemplateForm(forms.ModelForm):
    class Meta:
        model = ResumeTemplate
        fields = ['name', 'description', 'format_type', 'version']

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'slug', 'summary', 'tags', 'template', 'language', 'visibility']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter resume title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL slug'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter resume summary'}),
            'template': forms.Select(attrs={'class': 'form-select'}),
            'language': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., en'}),
            'visibility': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            # Only show templates that are active
            self.fields['template'].queryset = ResumeTemplate.objects.filter(is_active=True)

class ResumeSectionForm(forms.ModelForm):
    class Meta:
        model = ResumeSection
        fields = ['section_type', 'title', 'content', 'order', 'is_visible']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['resume', 'job_title', 'company', 'location', 'start_date', 'end_date', 'is_current', 'description', 'achievements', 'technologies']
        widgets = {
            'resume': forms.Select(attrs={'class': 'form-select'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job title'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_current': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe your role and responsibilities'}),
            'technologies': forms.SelectMultiple(attrs={'class': 'form-select', 'multiple': True}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

class TechnicalSkillForm(forms.ModelForm):
    class Meta:
        model = TechnicalSkill
        fields = ['resume', 'technology', 'proficiency', 'years_experience', 'last_used', 'project_count', 'is_visible']
        widgets = {
            'resume': forms.Select(attrs={'class': 'form-select'}),
            'technology': forms.Select(attrs={'class': 'form-select'}),
            'proficiency': forms.Select(attrs={'class': 'form-select'}),
            'years_experience': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '50'}),
            'last_used': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'project_count': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['resume', 'degree', 'institution', 'location', 'start_date', 'end_date', 'gpa', 'description', 'is_visible']
        widgets = {
            'resume': forms.Select(attrs={'class': 'form-select'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Bachelor of Science in Computer Science'}),
            'institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., University of Technology'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., New York, NY'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '4', 'placeholder': 'e.g., 3.8'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Additional details, honors, relevant coursework, etc.'}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['name', 'category', 'icon']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['resume', 'title', 'role', 'start_date', 'end_date', 'description', 'technologies', 'outcomes', 'url', 'is_active']
        widgets = {
            'resume': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., E-commerce Website'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Lead Developer'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe the project, your role, and key achievements'}),
            'technologies': forms.SelectMultiple(attrs={'class': 'form-select', 'multiple': True}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/username/project'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['resume', 'name', 'issuer', 'issue_date', 'expiration_date', 'credential_id', 'verification_url', 'skills']
        widgets = {
            'resume': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., AWS Certified Solutions Architect'}),
            'issuer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Amazon Web Services'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'credential_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Certification ID or number'}),
            'verification_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://verify.example.com/cert123'}),
            'skills': forms.SelectMultiple(attrs={'class': 'form-select', 'multiple': True}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['resume', 'title', 'issuer', 'issue_date', 'category', 'description', 'impact_metrics', 'is_visible']
        widgets = {
            'resume': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Employee of the Year'}),
            'issuer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., ABC Corporation'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe the achievement'}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['resume', 'name', 'proficiency', 'certification', 'is_visible']
        widgets = {
            'resume': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Spanish'}),
            'proficiency': forms.Select(attrs={'class': 'form-select'}),
            'certification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., DELE B2'}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['resume'].queryset = Resume.objects.filter(user=self.user)