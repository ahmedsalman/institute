from django.contrib import admin

from institute.models import Discipline, Institute, SubDiscipline


class DisciplineAdmin(admin.ModelAdmin):
    pass


class InstituteAdmin(admin.ModelAdmin):
    pass


class SubDisciplineAdmin(admin.ModelAdmin):
    pass


admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(SubDiscipline, SubDisciplineAdmin)
