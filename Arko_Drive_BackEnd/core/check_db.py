import MySQLdb
import os
from django.conf import settings

# Убедитесь, что этот модуль находит ваш settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # либо ваш_пакет.settings

try:
    db_settings = settings.DATABASES['default']
    conn = MySQLdb.connect(
        host=db_settings.get('HOST', 'localhost'),
        user=db_settings.get('USER'),
        passwd=db_settings.get('PASSWORD'),
        db=db_settings.get('NAME'),
        port=int(db_settings.get('PORT', 3306))
    )
    print("✓ Подключение к базе прошло успешно")
    conn.close()
except Exception as e:
    print("✗ Ошибка при подключении к базе:", e)

