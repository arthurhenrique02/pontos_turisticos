import os

from django.core.wsgi import get_wsgi_application

# dj static para o django conseguir enviar as imagens para o server no heroku
# from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "turismo.settings")

application = get_wsgi_application()

# application = Cling(get_wsgi_application())
