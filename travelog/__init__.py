from .settings import *                  # settings.py(本番環境用)をimport

try:
    from .settings_dev import *      # settings_develop.py(開発環境用)をimport
except:
    pass