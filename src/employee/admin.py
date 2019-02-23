from django.contrib import admin
from .models import (
					Employee,
					Department,
					#Section,
					Designation,
					#Team,
					#DepartmentAndDesignation,
					#DepartmentAndSection,
					#SectionAndTeam
				)

admin.site.register(Employee)
admin.site.register(Department)
#admin.site.register(Section)
admin.site.register(Designation)
#admin.site.register(Team)
# admin.site.register(DepartmentAndSection)
# admin.site.register(SectionAndTeam)



# Listing 11-2. Django admin list_display option

# from django.contrib import admin
# from coffeehouse.stores.models import Store
# class StoreAdmin(admin.ModelAdmin):
#       list_display = ['name','address','city','state']
# admin.site.register(Store, StoreAdmin)

# admin.py
# class StoreAdmin(admin.ModelAdmin):
#     list_display = ['name','address','upper_case_city_state']
#     def upper_case_city_state(self, obj):
#         return ("%s %s" % (obj.city, obj.state)).upper()
#     upper_case_city_state.short_description = 'City/State'

# Listing 11-8. Django admin with list_editable option

# # admin.py
# from django.contrib import admin
# from coffeehouse.stores.models import Store
# class StoreAdmin(admin.ModelAdmin):
#       list_display = ['name','address','city','state']
#       list_editable = ['address','city','state']
# admin.site.register(Store, StoreAdmin)


# Listing 11-9. Django admin with list_per_page option
# # admin.py
# from django.contrib import admin
# from coffeehouse.items.models import Item
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ['menu','name','price']
#     list_per_page = 5
# admin.site.register(Item, ItemAdmin)


# Listing 11-10. Django admin search_fields option
# from django.contrib import admin
# from coffeehouse.stores.models import Store
# class StoreAdmin(admin.ModelAdmin):
#       search_fields = ['city','state']
# admin.site.register(Store, StoreAdmin)


# Listing 11-11. Django admin list_filter option
# from django.contrib import admin
# from coffeehouse.items.models import Item
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ['menu','name','price']
#     list_filter = ['menu','price']
# admin.site.register(Item, ItemAdmin)