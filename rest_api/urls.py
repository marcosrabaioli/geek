from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^dollar/$', views.DollarquotationList.as_view(), name='dollar-list'),
    url(r'^dollar/(?P<pk>[^/]+)/$', views.DollarQuotationDetail.as_view(), name='dollar-detail'),

    url(r'^euro/$', views.EuroQuotationList.as_view(), name='euro-list'),
    url(r'^euro/(?P<pk>[^/]+)/$', views.EuroQuotationDetail.as_view(), name='euro-detail'),

    url(r'^bitcoin/$', views.BitcoinQuotationList.as_view(), name='bitcoin-list'),
    url(r'^bitcoin/(?P<pk>[^/]+)/$', views.BitcoinQuotationDetail.as_view(), name='bitcoin-detail'),

    url(r'^example/$', views.ExampleList.as_view(), name='example-list')

]
