from django.contrib import admin
from django.urls import path
from myProject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singupPage',singupPage,name="singupPage"),
    path('',singinPage,name="singinPage"),
    path('deshboardPage/',deshboardPage,name="deshboardPage"),
    path('logoutPage/',logoutPage,name="logoutPage"),
    path('forgotPasswordPage/',forgotPasswordPage,name="forgotPasswordPage"),
    path('addjobPage/',addjobPage,name="addjobPage"),
    path('deletePage/<str:myid>',deletePage,name="deletePage"),
    path('editPage/<str:myid>',editPage,name="editPage"),
    path('updatePage/',updatePage,name="updatePage"),
    path('applyPage/<str:myid>',applyPage,name="applyPage"),    
    path('viewjobPage',viewjobPage,name="viewjobPage"),    
    path('profilePage',profilePage,name="profilePage"), 
    path('EditprofilePage/',EditprofilePage,name="EditprofilePage"),
    path('changepassPage/',changepassPage,name="changepassPage"),
    path('createdjobbyrecruiter/',createdjobbyrecruiter,name="createdjobbyrecruiter"),
    path('createdresumebyjobseeker/',createdresumebyjobseeker,name="createdresumebyjobseeker"),
    path('viewresumepage/',viewresumepage,name="viewresumepage"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
