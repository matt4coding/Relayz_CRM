from django.conf.urls import patterns, url

account_urls = patterns('',

    url(r'^$',
        'relayzapp.accounts.views.account_detail', name='account_detail'
    ),
    url(r'^edit/$',
        'relayzapp.accounts.views.account_cru', name='account_update'
    ),
)
