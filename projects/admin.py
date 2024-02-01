from django.contrib import admin
from projects.models import Experience, Persona, Project


# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    pass

class PersonaAdmin(admin.ModelAdmin):
    # list_display = ('name', 'bio', 'web', 'rrss_1', 'rrss_2', 'email')
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Project, ProjectAdmin)
