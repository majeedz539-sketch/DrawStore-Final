#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
اختبار سريع لتطبيق DrawStore
"""

import os
import sys

def test_imports():
    """اختبار استيراد المكتبات"""
    print("🔍 اختبار المكتبات...")
    try:
        import flask
        print("  ✅ Flask مثبت")
    except ImportError:
        print("  ❌ Flask غير مثبت - شغّل: pip install flask")
        return False
    
    try:
        import requests
        print("  ✅ Requests مثبت")
    except ImportError:
        print("  ⚠️  Requests غير مثبت - شغّل: pip install requests")
        return False
    
    return True

def test_file_structure():
    """اختبار وجود الملفات الأساسية"""
    print("\n📁 اختبار هيكل الملفات...")
    
    required_files = {
        'app.py': 'ملف التطبيق الرئيسي',
        'config.py': 'ملف الإعدادات',
        'requirements.txt': 'ملف المكتبات',
        'templates/index.html': 'صفحة الرئيسية',
        'templates/login.html': 'صفحة التسجيل',
        'files': 'مجلد الملفات'
    }
    
    all_exist = True
    for file_path, description in required_files.items():
        if os.path.exists(file_path):
            print(f"  ✅ {file_path} ({description})")
        else:
            print(f"  ❌ {file_path} ({description}) - غير موجود")
            all_exist = False
    
    return all_exist

def test_python_syntax():
    """اختبار صحة الـ Python Syntax"""
    print("\n✔️  اختبار صيغة Python...")
    
    try:
        with open('app.py', 'r', encoding='utf-8') as f:
            code = f.read()
        compile(code, 'app.py', 'exec')
        print("  ✅ app.py - بدون أخطاء صيغة")
        return True
    except SyntaxError as e:
        print(f"  ❌ خطأ في صيغة Python: {e}")
        return False

def main():
    print("=" * 60)
    print("🧪 اختبار DrawStore Loader System")
    print("=" * 60)
    
    results = {
        'المكتبات': test_imports(),
        'الملفات': test_file_structure(),
        'الصيغة': test_python_syntax()
    }
    
    print("\n" + "=" * 60)
    print("📊 نتائج الاختبار:")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "✅ نجح" if result else "❌ فشل"
        print(f"{test_name}: {status}")
    
    print("=" * 60)
    
    if all(results.values()):
        print("\n✨ جميع الاختبارات نجحت! النظام جاهز.")
        print("\n▶️  لتشغيل التطبيق:")
        print("   python app.py")
        print("\n🌐 ثم افتح: http://localhost:5000")
        return 0
    else:
        print("\n⚠️  بعض الاختبارات فشلت. تحقق من الأخطاء أعلاه.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
