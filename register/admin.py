from django.contrib import admin
from register.models import UserProfile
from vendor.models import tokoternak, hewan
from user.models import pembeli_confirm
admin.site.register(UserProfile)
admin.site.register(tokoternak)
admin.site.register(hewan)
admin.site.register(pembeli_confirm)
# Register yourmodels here.
