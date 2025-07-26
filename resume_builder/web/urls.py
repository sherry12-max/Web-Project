# Python
from django.urls import path
from .views import (
    ResumeListView, ResumeCreateView, ResumeUpdateView, ResumeDeleteView, ResumeDetailView,
    WorkExperienceListView, WorkExperienceCreateView, WorkExperienceUpdateView,
    WorkExperienceDeleteView, WorkExperienceDetailView,
    EducationListView, EducationCreateView, EducationUpdateView, EducationDeleteView, EducationDetailView,
    ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectDetailView,
    CertificationListView, CertificationCreateView, CertificationUpdateView, CertificationDeleteView, CertificationDetailView,
    AwardListView, AwardCreateView, AwardUpdateView, AwardDeleteView, AwardDetailView,
    LanguageListView, LanguageCreateView, LanguageUpdateView, LanguageDeleteView, LanguageDetailView,
    TechnicalSkillListView, TechnicalSkillCreateView, TechnicalSkillUpdateView, TechnicalSkillDeleteView, TechnicalSkillDetailView,
    TemplateSelectionView, SelectTemplateView, ResumeDownloadView, PublicResumeDownloadView
)

urlpatterns = [
    # Resume URLs
    path('resumes/', ResumeListView.as_view(), name='resume_list'),
    path('resumes/add/', ResumeCreateView.as_view(), name='resume_create'),
    path('resumes/<int:pk>/edit/', ResumeUpdateView.as_view(), name='resume_update'),
    path('resumes/<int:pk>/delete/', ResumeDeleteView.as_view(), name='resume_delete'),
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),

    # Work Experience URLs
    path('work-experience/', WorkExperienceListView.as_view(), name='work_experience_list'),
    path('work-experience/add/', WorkExperienceCreateView.as_view(), name='work_experience_create'),
    path('work-experience/<int:pk>/edit/', WorkExperienceUpdateView.as_view(), name='work_experience_update'),
    path('work-experience/<int:pk>/delete/', WorkExperienceDeleteView.as_view(), name='work_experience_delete'),
    path('work-experience/<int:pk>/', WorkExperienceDetailView.as_view(), name='work_experience_detail'),

    # Education URLs
    path('education/', EducationListView.as_view(), name='education_list'),
    path('education/add/', EducationCreateView.as_view(), name='education_create'),
    path('education/<int:pk>/edit/', EducationUpdateView.as_view(), name='education_update'),
    path('education/<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),
    path('education/<int:pk>/', EducationDetailView.as_view(), name='education_detail'),

    # Project URLs
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

    # Certification URLs
    path('certifications/', CertificationListView.as_view(), name='certification_list'),
    path('certifications/add/', CertificationCreateView.as_view(), name='certification_create'),
    path('certifications/<int:pk>/edit/', CertificationUpdateView.as_view(), name='certification_update'),
    path('certifications/<int:pk>/delete/', CertificationDeleteView.as_view(), name='certification_delete'),
    path('certifications/<int:pk>/', CertificationDetailView.as_view(), name='certification_detail'),

    # Award URLs
    path('awards/', AwardListView.as_view(), name='award_list'),
    path('awards/add/', AwardCreateView.as_view(), name='award_create'),
    path('awards/<int:pk>/edit/', AwardUpdateView.as_view(), name='award_update'),
    path('awards/<int:pk>/delete/', AwardDeleteView.as_view(), name='award_delete'),
    path('awards/<int:pk>/', AwardDetailView.as_view(), name='award_detail'),

    # Language URLs
    path('languages/', LanguageListView.as_view(), name='language_list'),
    path('languages/add/', LanguageCreateView.as_view(), name='language_create'),
    path('languages/<int:pk>/edit/', LanguageUpdateView.as_view(), name='language_update'),
    path('languages/<int:pk>/delete/', LanguageDeleteView.as_view(), name='language_delete'),
    path('languages/<int:pk>/', LanguageDetailView.as_view(), name='language_detail'),

    # Technical Skill URLs
    path('technical-skills/', TechnicalSkillListView.as_view(), name='technical_skill_list'),
    path('technical-skills/add/', TechnicalSkillCreateView.as_view(), name='technical_skill_create'),
    path('technical-skills/<int:pk>/edit/', TechnicalSkillUpdateView.as_view(), name='technical_skill_update'),
    path('technical-skills/<int:pk>/delete/', TechnicalSkillDeleteView.as_view(), name='technical_skill_delete'),
    path('technical-skills/<int:pk>/', TechnicalSkillDetailView.as_view(), name='technical_skill_detail'),

    # Template Selection URLs
    path('templates/', TemplateSelectionView.as_view(), name='template_selection'),
    path('resumes/<int:resume_pk>/select-template/<int:template_pk>/', SelectTemplateView.as_view(), name='select_template'),

    # Resume Download URLs
    path('resumes/<int:pk>/download/', ResumeDownloadView.as_view(), name='resume_download'),
    path('resumes/<int:pk>/download/<str:format_type>/', ResumeDownloadView.as_view(), name='resume_download_format'),

    # Public Download URLs (for testing)
    path('public/resumes/<int:pk>/download/', PublicResumeDownloadView.as_view(), name='public_resume_download'),
    path('public/resumes/<int:pk>/download/<str:format_type>/', PublicResumeDownloadView.as_view(), name='public_resume_download_format'),
]