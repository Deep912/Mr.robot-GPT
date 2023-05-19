
class Config(object):
    DEBUG = True
    TESTING = False

class Development(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_KEY = 'YOUR-API-KEY'

config = {
    'development': Development,
    'testing': Development,
    'production': Development
}
