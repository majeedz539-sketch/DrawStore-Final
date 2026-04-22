"""
اختبارات بسيطة للتطبيق
"""

import app as main_app
import os
import json

def test_app_creation():
    """اختبار: إنشاء التطبيق"""
    assert main_app.app is not None
    print("✅ تم إنشاء التطبيق بنجاح")

def test_files_folder_creation():
    """اختبار: إنشاء مجلد files"""
    if not os.path.exists('files'):
        os.makedirs('files')
    assert os.path.exists('files')
    print("✅ مجلد files موجود")

def test_stats_file():
    """اختبار: ملف الإحصائيات"""
    stats = main_app.load_stats()
    assert isinstance(stats, dict)
    print("✅ يمكن قراءة ملف الإحصائيات")

def test_format_size():
    """اختبار: تنسيق حجم الملف"""
    assert main_app.format_size(512) == "512.0 B"
    assert main_app.format_size(1024) == "1.0 KB"
    assert main_app.format_size(1024 * 1024) == "1.0 MB"
    print("✅ تنسيق أحجام الملفات يعمل بشكل صحيح")

def test_client():
    """اختبار: اختبار العميل"""
    main_app.app.config['TESTING'] = True
    client = main_app.app.test_client()
    
    # اختبار الصفحة الرئيسية
    response = client.get('/')
    assert response.status_code == 200
    print("✅ الصفحة الرئيسية تستجيب بنجاح")
    
    # اختبار صفحة الإحصائيات
    response = client.get('/stats')
    assert response.status_code == 200
    print("✅ صفحة الإحصائيات تستجيب بنجاح")
    
    # اختبار ملف غير موجود
    response = client.get('/download/nonexistent.file')
    assert response.status_code == 404
    print("✅ معالجة الملفات غير الموجودة صحيحة")

if __name__ == '__main__':
    print("🧪 تشغيل الاختبارات...\n")
    
    try:
        test_app_creation()
        test_files_folder_creation()
        test_stats_file()
        test_format_size()
        test_client()
        
        print("\n✨ جميع الاختبارات نجحت!")
    except AssertionError as e:
        print(f"\n❌ فشل الاختبار: {e}")
    except Exception as e:
        print(f"\n⚠️ خطأ: {e}")
