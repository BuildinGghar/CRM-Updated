from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name="home"),
#     path('work', views.work, name="work"),
#     path('request', views.request, name="request"),
#     path('notice', views.notice, name="notice"),
#     path('attendance', views.attendance, name="attendance"),
# ]   
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('attendance',views.attendance,name="attendance"),
    # path('salary',views.salary,name="salary"),
    path('salary', views.salary, name='salary'),
    path('notice',views.notice,name="notice"),
    path('noticedetail/?P<id>/',views.noticedetail,name="noticedetail"),
   
]