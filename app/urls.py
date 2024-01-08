from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
urlpatterns = [
    path('', views.Home.as_view(),name='home'),
    path('product_detail/<int:pk>/',views.ProductView.as_view(),name='product'),
    path('addcart/', views.add_to_cart, name='add-to-cart'),
    path('showcart/',views.showcart,name='showcart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.AddressView.as_view(), name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=PasswordChangeForm,success_url='/passwordchangedone/'), name='changepassword'),
    path('passwordchangedone/',views.passdone,name='passwordchangedone'),
    path('resetpassword/',auth_views.PasswordResetView.as_view(template_name='app/resetpassword.html',form_class=PasswordResetForm,success_url='/resetpassworddone/'),name='password_reset'),
    path('resetpasswordconfirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/resetpasswordconfirm.html',form_class=SetPasswordForm,success_url='/resetpasswordcomplete/'),name='password_reset_confirm'),
    path('resetpassworddone/',auth_views.PasswordResetDoneView.as_view(template_name='app/resetpassworddone.html'),name='password_reset_done'),
    path('resetpasswordcomplete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/resetpasswordcomplete.html'),name='password_reset_confirm'),
    path('mobile/', views.MobileView.as_view(), name='mobile'),
    path('mobile/<slug:data>/',views.MobileView.as_view(),name='mobiledata'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='home'),name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('checkout/', views.checkout, name='checkout'),
]+ static(settings.MEDIA_URL,
          document_root=settings.MEDIA_ROOT)
