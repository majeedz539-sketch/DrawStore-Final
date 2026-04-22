from flask import Flask, render_template, send_file, request, jsonify, session, redirect, url_for
from datetime import datetime
import os
import json
import requests
from config import config

# إنشاء تطبيق Flask
app = Flask(__name__)

# تحميل الإعدادات بناءً على البيئة
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[config_name])

# إضافة SECRET_KEY لـ sessions
app.secret_key = app.config.get('SECRET_KEY', 'dev-secret-key-2024')

# إضافة custom tests للـ Jinja2
@app.template_test('endswith')
def test_endswith(value, suffix):
    """اختبار ما إذا كانت قيمة تنتهي بـ suffix"""
    return str(value).endswith(suffix)

# ملف لتخزين إحصائيات التحميل
STATS_FILE = 'download_stats.json'
RAILWAY_API_URL = 'https://deaw-production.up.railway.app/api'

def verify_license_key(license_key, hwid=None):
    """Verifica della chiave - accetta DRAW1 senza API"""
    # Se la chiave è DRAW1, accettala direttamente senza verificare l'API
    if license_key == "DRAW1":
        print("Chiave DRAW1 accettata direttamente")
        # Ritorna tutti i file disponibili (nessuna restrizione)
        return True, []
    
    # Per altre chiavi, prova Railway API (fallback)
    try:
        if not hwid:
            hwid = "web-client"
        
        payload = {
            'key': license_key,
            'hwid': hwid
        }
        
        response = requests.post(
            f'{RAILWAY_API_URL}/check_key',
            json=payload,
            timeout=5
        )
        
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, dict):
                if data.get('ok') is True:
                    if 'msg' in data and 'welcome' in data.get('msg', '').lower():
                        return True, data.get('files', [])
                
                if data.get('response') and 'welcome' in data.get('response', '').lower():
                    return True, data.get('files', [])
                
                if 'error' in data:
                    return False, []
                    
            return data.get('valid', False), data.get('files', [])
        else:
            return False, []
    except Exception:
        return False, []

def get_user_files(license_key):
    """الحصول على الملفات المتاح للمستخدم"""
    try:
        response = requests.post(
            f'{RAILWAY_API_URL}/get-files',
            json={
                'key': license_key,
                'hwid': 'web-client'
            },
            timeout=5
        )
        if response.status_code == 200:
            return response.json().get('files', [])
        return []
    except Exception as e:
        print(f"خطأ في الحصول على الملفات: {e}")
        return []

def load_stats():
    """تحميل إحصائيات التحميل"""
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, 'r') as f:
            return json.load(f)
    return {}

def get_file_type(filename):
    """استخراج نوع الملف من الاسم (بدون الامتداد)"""
    return os.path.splitext(filename)[0]

def get_available_products():
    """الحصول على قائمة المنتجات المتاحة من مجلد files"""
    products = []
    files_dir = os.path.join(os.path.dirname(__file__), 'files')
    
    if os.path.exists(files_dir) and os.path.isdir(files_dir):
        try:
            for filename in os.listdir(files_dir):
                file_path = os.path.join(files_dir, filename)
                if os.path.isfile(file_path):
                    # استخراج اسم المنتج (بدون الامتداد)
                    product_name = os.path.splitext(filename)[0]
                    # إذا لم يكن المنتج موجوداً بالفعل، أضفه
                    if product_name not in products:
                        products.append(product_name)
        except Exception as e:
            print(f"خطأ في قراءة مجلد files: {e}")
    
    return sorted(products)

def save_stats(stats):
    """حفظ إحصائيات التحميل"""
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=4)

def update_stats(filename, ip):
    """تحديث إحصائيات ملف معين"""
    stats = load_stats()
    
    if filename not in stats:
        stats[filename] = {
            'count': 0,
            'downloads': []
        }
    
    stats[filename]['count'] += 1
    stats[filename]['downloads'].append({
        'ip': ip,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    
    # الاحتفاظ بآخر 100 تحميل فقط
    if len(stats[filename]['downloads']) > 100:
        stats[filename]['downloads'] = stats[filename]['downloads'][-100:]
    
    save_stats(stats)

@app.route('/')
def index():
    """الصفحة الرئيسية - تعرض المنتج المختار"""
    # التحقق من وجود مفتاح في الجلسة
    if 'license_key' not in session:
        return redirect(url_for('login'))
    
    # التحقق من وجود منتج مختار
    if 'selected_product' not in session:
        return redirect(url_for('select_product'))
    
    license_key = session['license_key']
    selected_product = session['selected_product']
    
    valid, available_files = verify_license_key(license_key)
    
    if not valid:
        session.clear()
        return redirect(url_for('login'))
    
    stats = load_stats()
    
    # جلب الملفات المتعلقة بالمنتج المختار فقط
    files = []
    files_dir = os.path.join(os.path.dirname(__file__), 'files')
    
    if os.path.exists(files_dir) and os.path.isdir(files_dir):
        try:
            for filename in os.listdir(files_dir):
                file_path = os.path.join(files_dir, filename)
                if os.path.isfile(file_path):
                    # استخراج اسم المنتج من اسم الملف
                    product_name = os.path.splitext(filename)[0]
                    
                    # عرض الملفات فقط التي تنتمي للمنتج المختار
                    if product_name == selected_product:
                        # تحقق من أن الملف متاح للمستخدم أو أنه لم يتم تحديد ملفات معينة
                        if not available_files or filename in available_files or product_name in available_files:
                            try:
                                file_size = os.path.getsize(file_path)
                                file_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                                
                                # حساب الحجم بالـ GB
                                size_in_gb = file_size / (1024 ** 3)
                                
                                files.append({
                                    'name': filename,
                                    'size': format_size(file_size),
                                    'size_value': size_in_gb,
                                    'date': file_date.strftime('%Y-%m-%d'),
                                    'downloads': stats.get(filename, {}).get('count', 0)
                                })
                            except Exception as e:
                                print(f"خطأ في معالجة الملف {filename}: {e}")
                                continue
        except Exception as e:
            print(f"خطأ في قراءة مجلد files: {e}")
    
    # ترتيب الملفات حسب الأحدث
    files.sort(key=lambda x: x['date'], reverse=True)
    
    return render_template('index.html', 
                          files=files, 
                          license_key=license_key,
                          selected_product=selected_product)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """صفحة تسجيل الدخول مع المفتاح الثابت DRAW1"""
    if request.method == 'POST':
        license_key = request.form.get('license_key', '').strip()
        
        if not license_key:
            return render_template('login.html', error='Please enter the key')
        
        # Verify the key
        valid, available_files = verify_license_key(license_key)
        
        if valid:
            session['license_key'] = license_key
            session['available_files'] = available_files
            return redirect(url_for('select_product'))
        else:
            return render_template('login.html', error='Invalid or expired key - check connection or try another key')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """تسجيل الخروج"""
    session.clear()
    return redirect(url_for('login'))

@app.route('/select-product', methods=['GET', 'POST'])
def select_product():
    """صفحة اختيار المنتج"""
    # التحقق من وجود مفتاح في الجلسة
    if 'license_key' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        selected_product = request.form.get('product', '').strip()
        
        if not selected_product:
            return render_template('select_product.html', 
                                   error='الرجاء اختيار منتج',
                                   products=get_available_products())
        
        # حفظ المنتج المختار في الجلسة
        session['selected_product'] = selected_product
        return redirect(url_for('index'))
    
    # الحصول على قائمة المنتجات المتاحة
    products = get_available_products()
    
    if not products:
        return render_template('select_product.html', 
                               error='لا توجد منتجات متاحة حالياً',
                               products=[])
    
    return render_template('select_product.html', products=products)

@app.route('/download/<filename>')
def download_file(filename):
    """تحميل ملف معين"""
    # التحقق من المفتاح
    if 'license_key' not in session:
        return "غير مصرح - Not authorized", 403
    
    # استخدام المسار المطلق بدلاً من المسار النسبي
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'files', filename)
    
    # التحقق من أن الملف موجود وأنه داخل مجلد files
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        return "ملف غير موجود - File not found", 404
    
    # تسجيل التحميل
    update_stats(filename, request.remote_addr)
    
    return send_file(file_path, as_attachment=True)

@app.route('/api/verify', methods=['POST'])
def api_verify():
    """API للتحقق من المفتاح"""
    data = request.get_json()
    license_key = data.get('key', '').strip()
    
    if not license_key:
        return jsonify({'valid': False, 'message': 'لم يتم إدخال المفتاح'})
    
    valid, available_files = verify_license_key(license_key)
    return jsonify({
        'valid': valid,
        'files': available_files,
        'message': 'المفتاح صحيح' if valid else 'المفتاح غير صحيح'
    })

@app.route('/api/check_key', methods=['POST'])
def check_key():
    """API للتحقق من المفتاح مع HWID (للتطبيقات الخارجية)"""
    try:
        data = request.get_json()
        license_key = data.get('key', '').strip()
        hwid = data.get('hwid', '').strip()
        
        if not license_key:
            return jsonify({'msg': 'Missing key', 'ok': False}), 400
        
        # التحقق من المفتاح عبر Railway API
        valid, available_files = verify_license_key(license_key, hwid)
        
        if valid:
            return jsonify({
                'msg': 'welcome',
                'ok': True,
                'files': available_files
            }), 200
        else:
            return jsonify({
                'msg': 'Invalid key',
                'ok': False
            }), 401
            
    except Exception as e:
        print(f"خطأ في check_key: {e}")
        return jsonify({
            'msg': 'Connection Error',
            'ok': False
        }), 500

def format_size(size):
    """تحويل حجم الملف من بايت إلى KB/MB"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} GB"

if __name__ == '__main__':
    # إنشاء مجلد files إذا لم يكن موجوداً
    if not os.path.exists('files'):
        os.makedirs('files')
    
    # تشغيل التطبيق باستخدام الإعدادات من البيئة
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
