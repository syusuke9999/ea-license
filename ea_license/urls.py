"""
ea_licenseプロジェクトのURL設定。

`urlpatterns`リストはURLをビューにルーティングします。詳細は以下をご覧ください:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
例:
関数ビュー
    1. インポートを追加します:  from my_app import views
    2. urlpatternsにURLを追加します:  path('', views.home, name='home')
クラスベースのビュー
    1. インポートを追加します:  from other_app.views import Home
    2. urlpatternsにURLを追加します:  path('', Home.as_view(), name='home')
別のURLconfを含める
    1. include()関数をインポートします: from django.urls import include, path
    2. urlpatternsにURLを追加します:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  include  # include をインポート
from django.urls import path
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/admin/')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # apiアプリのurls.pyをインクルード
]
