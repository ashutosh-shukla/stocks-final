from django.contrib import admin
from django.urls import path
from final import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login and signup
    path('signup/', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
# Dynamic routes
path('', views.home, name='home'),
path('homepage/', views.homepage, name='homepage'),
path('foreign/', views.foreign, name='foreign'),
path('mutualfunds/', views.mf, name='mutualfunds'),
path('bonds/', views.bonds, name='bonds'),
path('etfs/', views.etfs, name='etfs'),  # Corrected the name to 'etfs'
path('stocks/', views.stocks, name='stocks'),


    # Analysis
    path('funds/', views.funds, name='funds'),
    path('importing/', views.importing, name='importing'),
    path('gdp/', views.gdp, name='gdp'),
    path('inflation/', views.inflation, name='inflation'),
    path('intrest/', views.intrest, name='intrest'),
    path('manu/', views.manu, name='manu'),

    # Fundamental Analysis
    path('fiscalpolicy/', views.fis, name='fiscalpolicy'),
    path('governmentpolicy/', views.gov, name='governmentpolicy'),
    path('monetrypolicy/', views.mon, name='monetrypolicy'),

    # Personal Finance
    path('literacy/', views.literacy, name='literacy'),
    path('retirement/', views.ret, name='retirement'),
    path('budget/', views.per, name='budget'),
    path('savings/', views.sav, name='savings'),
    path('taxes/', views.tax, name='taxes'),
    path('loan/', views.loan, name='loan'),

    # News
    path('market/', views.mar, name='market'),
    path('companies/', views.comp, name='companies'),
    path('economy/', views.eco, name='economy'),
    path('political/', views.poli, name='political'),
    path('government/', views.gov, name='government'),
    path('worldwide/', views.world, name='worldwide'),

    # Learning
    path('beginners/', views.f, name='beginners'),
    path('fanalysis/', views.ic, name='fanalysis'),
    path('trading/', views.inc, name='trading'),
    path('investing/', views.tc, name='investing'),
    path('signup/', views.signuppage, name='signuppage'),
]
