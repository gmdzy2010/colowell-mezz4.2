from django.conf.urls import url
from sms import views

urlpatterns = [
    # url(r'image/(?P<key>\w+)/$', views.captcha_image, name='captcha-image', kwargs={'scale': 1}),
    # url(r'image/(?P<key>\w+)@2/$', views.captcha_image, name='captcha-image-2x', kwargs={'scale': 2}),
    # url(r'audio/(?P<key>\w+)/$', views.captcha_audio, name='captcha-audio'),
    url(r'refresh/(?P<phone_num>\d{11})/$', views.captcha_refresh, name='captcha-refresh'),
]
