"""
ea_licenseプロジェクトのASGI設定。

モジュールレベルの変数``application``としてASGIコール可能なものを公開します。

このファイルについての詳細は、以下を参照してください。
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ea_license.settings')

application = get_asgi_application()
