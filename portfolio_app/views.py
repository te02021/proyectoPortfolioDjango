from django.shortcuts import render, redirect
from .models import Project, SaveContactMessage, Studies, Courses, Works, Skills
from .forms import ContactForm

# Create your views here.

def projects(request):
    context = Project.objects.all()
    return render(request, 'project/projects.html', {
        'projects': context
        })
    
def index_view(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'index.html', {'form': form})
    else:
        SaveContactMessage.objects.create(name=request.POST['name'],
                                          last_name=request.POST['last_name'],
                                          email=request.POST['email'],
                                          company=request.POST['company'],
                                          description=request.POST['description'])
        return redirect('contact_success')  # Redirige a una página de éxito o la página que prefieras.
    
            
def contact_success(request):
    return render(request, 'contact_success.html')

def studies(request):
    studies_list = Studies.objects.all()
    courses_list = Courses.objects.all()
    return render(request, 'studies.html', {
        'studies': studies_list,
        'courses': courses_list
        })

def experience(request):
    works_list = Works.objects.all() 
    return render(request, 'experience.html', {
        'works':works_list})

def skills(request):
    skills_list = Skills.objects.all()
    return render(request, 'skills.html', {
        'skills': skills_list
        })