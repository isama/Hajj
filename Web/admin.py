from django.contrib import admin
from Web.models import Activity, Action, Camp, CampUser
# Register your models here.

admin.AdminSite.site_header = "Administration"


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'supervisor', 'start', 'end')


class CampUserAdmin(admin.ModelAdmin):
    list_display = ('camp', 'user')


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Camp)
admin.site.register(CampUser, CampUserAdmin)
