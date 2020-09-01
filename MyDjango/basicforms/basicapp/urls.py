from django.conf.urls import url
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    url(r'^Go/$', views.go_to, name='Go_to'),
    url(r'^formpage/$', views.form_name_view, name='form_name'),
]