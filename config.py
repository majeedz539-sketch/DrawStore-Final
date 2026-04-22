import os

class Config:
    """إعدادات التطبيق الأساسية"""
    
    # إعدادات Flask
    DEBUG = os.environ.get('FLASK_DEBUG', True)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # إعدادات الملفات
    FILES_FOLDER = 'files'
    STATS_FILE = 'download_stats.json'
    MAX_DOWNLOADS_PER_FILE = 100
    
    # إعدادات السيرفر
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))

class DevelopmentConfig(Config):
    """إعدادات التطوير"""
    DEBUG = True

class ProductionConfig(Config):
    """إعدادات الإنتاج"""
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
