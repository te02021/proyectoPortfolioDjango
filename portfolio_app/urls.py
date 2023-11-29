from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('', views.index_view, name="index"),
    path('contact_success/', views.contact_success, name="contact_success"),
    path('studies/', views.studies, name="studies"),
    path('experience/', views.experience, name="experience"),
    path('skills/', views.skills, name="skills")    
]
