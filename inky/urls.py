from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django.contrib.auth.urls")),
    path("", include("users.urls")),
    path("pens", include("pens.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Inky Admin"
admin.site.site_title = "Inky"
admin.site.index_title = "Welcome to the Inky Admin"
