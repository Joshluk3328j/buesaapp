from django.urls import path
from . import views


urlpatterns = [
    # path('rounte name, views(the file_name).function_created')
    path('', views.myview),
    path('getotp/', views.getotp, name="getotp"),
    path('getotp/votingpage/', views.votingpage),
    path('getotp/votingpage/submit', views.submit),
    path('getotp/votingpage/submit/vote-tracker', views.pollresult),

]
