# 🎯 DrawStore Loader - نظام التحميل الاحترافي

> 🚀 **نظام حديث وآمن لتوزيع وتحميل الملفات مع نظام ترخيص متقدم**

---

## ✨ الميزات الجديدة (2024)

### 🔐 نظام الترخيص المتقدم
- **مفاتيح ترخيص فريدة** لكل مستخدم
- **التحقق عبر Railway API** آمن وسريع
- **صفحة تسجيل دخول** جميلة واحترافية
- **جلسات آمنة** للمستخدمين

### 📦 نظام الملفات الذكي
- **كل مستخدم يرى الملفات المتاحة له فقط**
- **فلترة ذكية حسب نوع الملف**
- **إحصائيات تفصيلية** لكل ملف
- **تسجيل جميع التحميلات**

### 💬 التواصل السهل
- **رابط Discord مباشر**: https://discord.gg/Ad66M4CW8v
- **رابط TikTok مباشر**: https://www.tiktok.com/@drawstore
- **أيقونات سوشيال ميديا** في الفوتر

### 🎨 التصميم المحسّن
- **واجهة عربية جميلة** (RTL)
- **لوقو نظيف بدون تأثيرات معقدة**
- **أنيمیشنات سلسة وسريعة**
- **متوافق مع جميع الأجهزة** (Responsive)

---

## 🚀 البدء السريع

### 1️⃣ التثبيت والإعداد
```bash
# استنساخ أو تحميل المشروع
cd DrawStore-Loader

# تثبيت المكتبات المطلوبة
pip install -r requirements.txt

# تشغيل الاختبار السريع
python test_system.py
```

### 2️⃣ تشغيل التطبيق
```bash
# طريقة 1: تشغيل مباشر
python app.py

# طريقة 2: استخدام الملف الباتش
run.bat
```

### 3️⃣ الوصول للموقع
```
افتح المتصفح وادخل: http://localhost:5000
```

---

## 📖 دليل الاستخدام

### للمستخدمين النهائيين

1. **افتح الموقع** → `http://localhost:5000`
2. **أدخل مفتاح الترخيص** الخاص بك
3. **شاهد الملفات المتاحة** لحسابك
4. **اختر الملف** من القائمة
5. **استخدم الفلتر** لتصفية الملفات (اختياري)
6. **اضغط تحميل** لتنزيل الملف
7. **تسجيل الخروج** عند الانتهاء

### للمطورين

#### إضافة ملف جديد
```python
# ضع الملف في مجلد: files/
# مثال: files/Bo7.exe
```

#### إضافة مستخدم جديد
```json
{
  "license_key": "LICENSE-KEY-123456",
  "user_email": "user@example.com",
  "purchased_files": ["Bo7", "MW3V1"],
  "expiry_date": "2025-12-31"
}
```

#### التحقق من المفتاح (API)
```bash
curl -X POST http://localhost:5000/api/verify \
  -H "Content-Type: application/json" \
  -d '{"key": "YOUR-LICENSE-KEY"}'
```

---

## 🔧 الإعدادات

### ملف البيئة (.env)
```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=drawstore-secret-key-2024
HOST=0.0.0.0
PORT=5000

DISCORD_LINK=https://discord.gg/Ad66M4CW8v
TIKTOK_LINK=https://www.tiktok.com/@drawstore

RAILWAY_API_URL=https://deaw-production.up.railway.app/api
```

### ملف الإعدادات (config.py)
```python
DEBUG = True
MAX_DOWNLOADS_PER_FILE = 100
FILES_FOLDER = 'files'
```

---

## 📊 إحصائيات النظام

يعرض الموقع:
- ✅ **عدد الملفات المتاحة**
- ✅ **إجمالي التحميلات**
- ✅ **عدد ملفات EXE**
- ✅ **إجمالي حجم البيانات**

---

## 🔒 الأمان

### المميزات الأمنية
✅ **جلسات مشفرة** - كل مستخدم له جلسة فريدة
✅ **التحقق من المفتاح** - فقط المفاتيح الصحيحة تعمل
✅ **فحص الملفات** - التحقق من أن الملف موجود قبل التحميل
✅ **تسجيل الأنشطة** - تسجيل كل تحميل مع التاريخ و IP
✅ **حماية المسارات** - منع الوصول للملفات خارج مجلد files

### نصائح الأمان
⚠️ **غيّر SECRET_KEY** في الإنتاج
⚠️ **استخدم HTTPS** في الإنتاج (مهم!)
⚠️ **قوية كلمات المرور** للمفاتيح
⚠️ **نسخ احتياطية منتظمة** لقاعدة البيانات

---

## 📡 تكامل Railway API

النظام يتطلب Railway API بهذا الشكل:

### Endpoint 1: التحقق من الترخيص
```
POST /api/verify-license
Body: {"key": "license-key"}
Response: {
  "valid": true,
  "files": ["Bo7.exe", "MW3V1.exe"]
}
```

### Endpoint 2: الحصول على الملفات
```
POST /api/get-files
Body: {"key": "license-key"}
Response: {
  "files": ["Bo7.exe", "MW3V1.exe"]
}
```

📄 انظر `RAILWAY_API_EXAMPLE.json` لأمثلة مفصلة

---

## 📁 هيكل المشروع

```
DrawStore-Loader/
├── app.py                    # التطبيق الرئيسي
├── config.py                 # إعدادات التطبيق
├── requirements.txt          # المكتبات المطلوبة
├── .env                      # متغيرات البيئة
├── test_system.py            # اختبار النظام
│
├── files/                    # مجلد الملفات
│   ├── Bo7.exe
│   ├── MW3V1.exe
│   └── OW2.exe
│
├── templates/                # قوالب HTML
│   ├── index.html           # الصفحة الرئيسية
│   └── login.html           # صفحة التسجيل
│
└── docs/                     # التوثيق
    ├── SYSTEM_UPDATES.md
    ├── CHANGES_SUMMARY.md
    └── RAILWAY_API_EXAMPLE.json
```

---

## 🐛 استكشاف الأخطاء

### المشكلة: "File not found"
```
✅ الحل: تأكد من وجود الملف في مجلد files/
```

### المشكلة: "خطأ في الاتصال بـ Railway API"
```
✅ الحل: تحقق من:
   - URL صحيح في .env
   - الإنترنت متصل
   - Railway API يعمل
```

### المشكلة: "المفتاح غير صحيح"
```
✅ الحل:
   - تحقق من المفتاح (capital/small)
   - تحقق من صلاحية المفتاح
   - استعد المفتاح من الأدمن
```

### المشكلة: "ملفات موقع بطيئة"
```
✅ الحل:
   - استخدم CDN للأصول الثابتة
   - ضغط الملفات
   - نسخ احتياطية من الخادم
```

---

## 🚀 النشر والإطلاق

### النشر على Railway
```bash
# 1. تثبيت Railway CLI
npm install -g railway

# 2. تسجيل الدخول
railway login

# 3. إنشاء مشروع جديد
railway init

# 4. رفع المشروع
git push railway main
```

### النشر على Heroku
```bash
# 1. تثبيت Heroku CLI
# 2. تسجيل الدخول
heroku login

# 3. إنشاء تطبيق
heroku create drawstore

# 4. رفع المشروع
git push heroku main
```

---

## 📞 الدعم والتواصل

### قنوات التواصل
- 💬 **Discord**: https://discord.gg/Ad66M4CW8v
- 🎵 **TikTok**: https://www.tiktok.com/@drawstore
- 📧 **البريد**: support@drawstore.com

### الملفات المساعدة
- 📖 [SYSTEM_UPDATES.md](SYSTEM_UPDATES.md) - التحديثات
- 📋 [CHANGES_SUMMARY.md](CHANGES_SUMMARY.md) - ملخص التغييرات
- 📡 [RAILWAY_API_EXAMPLE.json](RAILWAY_API_EXAMPLE.json) - أمثلة API

---

## 📜 الترخيص والحقوق

© 2024-2026 DrawStore - جميع الحقوق محفوظة

---

## 🙏 شكر خاص

شكراً لاستخدامك DrawStore!

---

**آخر تحديث**: 22 أبريل 2024
**الإصدار**: 2.0 (نظام الترخيص)
**الحالة**: ✅ جاهز للإنتاج
