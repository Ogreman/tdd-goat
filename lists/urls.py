from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(
        regex=r'^(\d+)/$',
        view='lists.views.view_list',
        name='view_list',
    ),

    url(
        regex=r'^(\d+)/add_item$',
        view='lists.views.add_item',
        name='add_item',
    ),

    url(
        regex=r'^new$',
        view='lists.views.new_list',
        name='new_list'
    ),

)
