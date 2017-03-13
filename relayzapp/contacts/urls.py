from django.conf.urls import patterns, url

contact_urls = patterns('',

    url(r'^$', 'relayzapp.contacts.views.contact_detail', name="contact_detail"),
    url(r'^edit/$',
        'relayzapp.contacts.views.contact_cru', name='contact_update'
    ),

)
