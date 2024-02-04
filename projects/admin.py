from django.contrib import admin
from projects.models import Experience, Persona, Project


# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "init_date", "end_date",
        "experience",
        "persona",
    )


class PersonaAdmin(admin.ModelAdmin):
    # list_display = ('name', 'bio', 'web', 'rrss_1', 'rrss_2', 'email')
    pass


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "image",
        "persona_id",
        "tags",
    )


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Project, ProjectAdmin)
