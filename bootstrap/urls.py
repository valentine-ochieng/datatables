#urls.py
from django.urls import path  
from .import views  
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [  
    path('', views.index),  
    path('addnew',views.addnew),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('deleted', views.deleted),

    path('flowbite', views.flowbite),  
    path('tailwind', views.tailwind),  


    path('responsive', views.responsive),  
    path('modal_datatable', views.modal_datatable), 


    # path('file_upload/', views.file_upload_view),  


     path('upload/', views.upload_files, name='file_upload'),



]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)