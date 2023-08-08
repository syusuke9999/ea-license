"""
ea_licenseプロジェクトのWSGI設定。

モジュールレベルの変数``application``としてWSGIコール可能なものを公開します。

このファイルについての詳細は、以下を参照してください。
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise


application = get_wsgi_application()
application = WhiteNoise(application, root='/path/to/static/files')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ea_license.settings')
