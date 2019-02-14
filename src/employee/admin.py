from django.contrib import admin
from .models import (
					Employee,
					Department,
					Section,
					Designation,
					Team,
					DepartmentAndDesignation,
					DepartmentAndSection,
					SectionAndTeam
				)


admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Section)
admin.site.register(Designation)
admin.site.register(Team)
admin.site.register(DepartmentAndDesignation)
admin.site.register(DepartmentAndSection)
admin.site.register(SectionAndTeam)



