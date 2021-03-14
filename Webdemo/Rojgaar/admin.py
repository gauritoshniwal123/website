from django.contrib import admin
from .models import SRecruiter,LRecruiter,SJobseeker,LJobseeker

admin.site.register(SRecruiter)
admin.site.register(LRecruiter)
admin.site.register(SJobseeker)
admin.site.register(LJobseeker)

