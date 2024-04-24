from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from lung_cancer_prediction import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage,name='home_page'),   
    path('save-account',views.saveAccount, name='save_account'),
    path('login-user', views.LoginUser, name='login_user'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('save-patient', views.savePatient, name='save_patient'),
    path('upload-ctscan', views.uploadCTScan, name='upload_ctscan'),
    path('show-ctscan', views.showCTScan, name='show_ctscan')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)