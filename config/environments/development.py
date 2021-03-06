from path import path
from config.settings import *




# if ALLOW_TEMPLATE_EXCEPTIONS then template throws exception on undefined
# variables instead of failing silently, which is the default behavior.
# WARNING: Parts of Django expect the template engine to silently fail
# (like admin).
# Read more at https://docs.djangoproject.com/en/dev/ref/templates/api/#how-invalid-variables-are-handled
# The official advice is that this "should only be enabled in order to debug a
# specific template problem, then cleared once debugging is complete."
ALLOW_TEMPLATE_EXCEPTIONS = True
class InvalidString(str):
    # Taken from http://stackoverflow.com/a/7854378/196678
    def __mod__(self, other):
        if ALLOW_TEMPLATE_EXCEPTIONS:
            from django.template.base import TemplateSyntaxError
            raise TemplateSyntaxError(
                """Undefined variable or unknown value for: %s.
(You're seeing this because you turned on ALLOW_TEMPLATE_EXCEPTIONS)
""" % other)
        else:
            return ""
TEMPLATE_STRING_IF_INVALID = InvalidString("%s")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '[[DATABASE_NAME]]',
        'USER': 'postgres', # this is the system usernme, not the database username
        'PASSWORD': 'postgres', # postgres server seems to require a password
        'HOST': 'localhost',
        'PORT': '5432',
    },

    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_ROOT / 'db/development.sqlite3',
    }
}

DEBUG = True

# config/environments/local.py is ignored to allow for easy settings
# overrides without affecting others environments / developers
try:
    from local import *
except ImportError:
    pass
LOGGING['loggers']['django.request']['handlers'].append('console')
LOGGING['loggers']['django.request']['level'] = 'DEBUG'
