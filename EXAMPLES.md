"""
أمثلة الاستخدام والـ API
"""

# مثال 1: الوصول للصفحة الرئيسية
# GET http://localhost:5000/
# يعرض قائمة الملفات المتاحة للتحميل


# مثال 2: تحميل ملف معين
# GET http://localhost:5000/download/DrawStore_v1.0.ahk
# يحمّل الملف ويسجل الإحصائيات


# مثال 3: عرض الإحصائيات
# GET http://localhost:5000/stats
# يعرض جميع إحصائيات التحميلات


# مثال 4: استخدام Python
"""
import requests

# تحميل ملف
response = requests.get('http://localhost:5000/download/file.ahk')
if response.status_code == 200:
    with open('file.ahk', 'wb') as f:
        f.write(response.content)
"""


# مثال 5: استخدام JavaScript/Fetch API
"""
// تحميل قائمة الملفات
fetch('http://localhost:5000/')
  .then(response => response.text())
  .then(html => {
    // معالجة الـ HTML
    console.log(html);
  });

// تحميل ملف
async function downloadFile(filename) {
  const response = await fetch(`/download/${filename}`);
  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.click();
}
"""


# مثال 6: تخصيص الإعدادات
"""
# في ملف .env
FLASK_ENV=production
FLASK_DEBUG=0
PORT=8000
HOST=0.0.0.0
SECRET_KEY=your-secret-key-here
"""


# مثال 7: إضافة Authentication (اختياري)
"""
from functools import wraps
from flask import request, abort

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.password != 'admin-password':
            abort(403)
        return f(*args, **kwargs)
    return decorated

@app.route('/admin/<path>')
@require_auth
def admin_panel(path):
    # كود الأدمن
    pass
"""


# مثال 8: استخدام قاعدة بيانات (اختياري)
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///drawstore.db')
Session = sessionmaker(bind=engine)

# ثم يمكنك حفظ الإحصائيات في قاعدة البيانات بدلاً من JSON
"""


# مثال 9: تشغيل مع Gunicorn (للإنتاج)
"""
gunicorn -w 4 -b 0.0.0.0:5000 app:app
"""


# مثال 10: تشغيل مع Nginx (reverse proxy)
"""
server {
    listen 80;
    server_name drawstore.example.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
"""
