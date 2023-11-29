from django.db import models

# Create your models here.

class SaveContactMessage(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Save Contact Message'
        verbose_name_plural = 'Save Contact Messages'

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
class Studies(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    start_date = models.DateField()
    #permitir valores nulos en la base de datos y también que permita que el campo esté en blanco en los formularios
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        if self.end_date:
            return f"{self.title} ({self.start_date} - {self.end_date})"
        else:
            return f"{self.title} ({self.start_date} - En curso)"
        
    class Meta:
        verbose_name = 'Studie'
        verbose_name_plural = 'Studies'
    
class Courses(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    start_date = models.DateField()
    #permitir valores nulos en la base de datos y también que permita que el campo esté en blanco en los formularios
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    certificate = models.ImageField(upload_to='certificates/', null=True, blank=True)
    
    def __str__(self):
        if self.end_date:
            return f"{self.name} ({self.start_date} - {self.end_date})"
        else:
            return f"{self.name} ({self.start_date} - En curso)"
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        
class Works(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='works/', null=True, blank=True)
    
    def __str__(self):
        if self.end_date:
            return f"{self.title} ({self.start_date} - {self.end_date})"
        else:
            return f"{self.title} ({self.start_date} - En curso)"
        
    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'
        
class Skills(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='skills/')  # El directorio 'skills/' debe existir en tu directorio de medios
    url = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'