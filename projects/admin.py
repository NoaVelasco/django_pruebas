from django.contrib import admin
from projects.models import Experience, Persona, Project


# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    pass

class PersonaAdmin(admin.ModelAdmin):
    pass
class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Project, ProjectAdmin)
