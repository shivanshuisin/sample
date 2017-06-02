from django.conf.urls import include,url

from . import views

urlpatterns = [
url(r'^checklogin/$', views.Authenticate, name='main'),
url(r'^admn/$',views.AdminView,name='admnl'),
url(r'^emp/$',views.ManageEmp,name='employee'),
url(r'^salary/$',views.ManageSalary,name='salary'),
url(r'^registeruser/$',views.CreateUser,name='reguser'),
url(r'^register/$',views.UserStore,name='store'),
url(r'^logout/$',views.Logout,name='logout'),
url(r'^editempm/$',views.IndexViewUM.as_view(),name='editempm'),
url(r'^editemp/$',views.EditEmp,name='editemp'),
url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
url(r'^update/$',views.UpdateUser,name='update'),
url(r'^payslipd/$',views.EditPayslip,name='payslipm'),
url(r'^editpayslipm/$',views.IndexViewPM.as_view(),name='payslipm'),
url(r'^payslip/(?P<pk>[0-9]+)/$',views.DetailViewPM.as_view(),name='payslipm'),
url(r'^admn/salary/$',views.SalaryMain,name='salarymain'),
url(r'^updatepayslip/$',views.UpdatePayslip,name='updatepayslip'),
url(r'^editempt/$',views.IndexViewUT.as_view(),name='editempt'),
url(r'^editempc/$',views.IndexViewUC.as_view(),name='editempc'),
url(r'^editpayslipc/$',views.IndexViewPC.as_view(),name='payslipc'),
url(r'^editpayslipt/$',views.IndexViewPT.as_view(),name='payslipt'),
url(r'^deleteuser/$',views.UserDeleteM,name='deleteuserm'),
url(r'^usermessageview/$',views.MessageUser,name='messageuserview'),
url(r'^usermessagesave/$',views.SendMessage,name='messagesend'),
url(r'^messagedelete/$',views.DeleteMessage,name='messagedelete'),
url(r'^adminmessageview/$',views.AdminMessageView,name='messageviewadmin'),
url(r'^userview/$',views.UserView,name='userview'),
url(r'^homeview/$',views.HomeView,name='homeview'),










        ]
