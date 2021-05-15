from django.urls import path, include
from .views import (
	IndexView,
	ShareableCreateView,
	ShareableUpdateView,
	ShareableDeleteView,
	Orig_SharerCreateView,
	Orig_SharerView

	)

urlpatterns = [
	path('', IndexView, name="shareables-home"),  
	path('add-shareable', ShareableCreateView.as_view(), name="add-shareable"),  
	path('detail/<int:pk>/update/', ShareableUpdateView.as_view(), name="update-shareable"),  
	path('delete-shareable', ShareableDeleteView.as_view(), name="delete-shareable"),  
	path('add-sharer', Orig_SharerCreateView.as_view(), name="add-sharer"),  

]




from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)