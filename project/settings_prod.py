from .settings import *


DEBUG = False

RQ_QUEUES = {
    'default': {
        'HOST': 'redis://redistogo:138ed9b216c6a6ec5a8a4782bbfa0a16@pearlfish.redistogo.com',
        'PORT': 9405,
        'DB': 0,
        'PASSWORD': '138ed9b216c6a6ec5a8a4782bbfa0a16',
    },
}
