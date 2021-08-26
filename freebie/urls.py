from django.urls import path, include
from .views import (
	IndexView,
	FreebieCreateView,
	FreebieDetailView,
	FreebieUpdateView,
	FreebieDeleteView,
	Orig_SharerCreateView,
	Orig_SharerView

	)

urlpatterns = [
	path('', IndexView, name="freebies"),  
	path('add-freebie/', FreebieCreateView.as_view(), name="add-freebie"),  
	path('<int:pk>/', FreebieDetailView.as_view(), name="freebie-detail"),
	path('<int:pk>/update/', FreebieUpdateView.as_view(), name="update-freebie"),  
	path('<int:pk>/delete/', FreebieDeleteView.as_view(), name="delete-freebie"),  
	path('add-sharer/', Orig_SharerCreateView.as_view(), name="add-sharer"),  

]




from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)