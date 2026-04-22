# DrawStore Loader 📦

منصة تحميل السكربتات والإضافات - A powerful script & addon distribution platform

## المميزات ✨

- 🚀 واجهة تحميل حديثة وسهلة الاستخدام
- 📊 إحصائيات تفصيلية للتحميلات
- 🌍 دعم اللغة العربية كاملاً
- 📁 إدارة سهلة للملفات
- 🔄 تحديث تلقائي للإحصائيات
- 📱 متوافق مع جميع الأجهزة

## المتطلبات 🛠️

- Python 3.7+
- Flask 2.3.0+

## التثبيت 📥

### 1. استنساخ المستودع

```bash
git clone https://github.com/your-username/DrawStore-Loader.git
cd DrawStore-Loader
```

### 2. تثبيت المكتبات

```bash
pip install -r requirements.txt
```

### 3. تشغيل التطبيق

```bash
python app.py
```

التطبيق سيعمل على `http://localhost:5000`

## الهيكل 📂

```
DrawStore-Loader/
├── app.py              # السيرفر الرئيسي
├── requirements.txt    # المكتبات المطلوبة
├── download_stats.json # ملف الإحصائيات (يُنشأ تلقائياً)
├── files/              # مجلد السكربتات والملفات
│   ├── DrawStore_v1.0.ahk
│   ├── DrawStore_v1.1.ahk
│   └── DrawStore_v2.0.exe
└── templates/          # قوالب HTML
    ├── index.html      # الصفحة الرئيسية
    └── stats.html      # صفحة الإحصائيات
```

## كيفية الاستخدام 🚀

### إضافة ملفات للتحميل

1. ضع الملفات في مجلد `files/`
2. قم بتحديث الصفحة - ستظهر الملفات تلقائياً

### عرض الإحصائيات

- اذهب إلى `/stats` لرؤية إحصائيات التحميلات

## الرفع على Railway 🚀

### الخطوة 1: إنشاء حساب على Railway

- اذهب إلى [railway.app](https://railway.app)
- سجل دخول بحساب GitHub

### الخطوة 2: رفع المشروع

```bash
# أنشئ مستودع git محلي
git init
git add .
git commit -m "Initial commit"

# أضف المستودع البعيد
git remote add origin https://github.com/your-username/DrawStore-Loader.git
git branch -M main
git push -u origin main
```

### الخطوة 3: الربط مع Railway

1. اذهب إلى https://railway.app
2. اختر "New Project"
3. اختر "Deploy from GitHub"
4. اختر المستودع
5. Railway سيكشف `requirements.txt` ويثبت الملفات تلقائياً

### الخطوة 4: تكوين المتغيرات

في لوحة التحكم أضف:
- `FLASK_ENV`: production
- `FLASK_DEBUG`: 0

## البيئات المدعومة 🌐

- Windows ✅
- Linux ✅
- macOS ✅

## الملفات المدعومة 📄

| الامتداد | الأيقونة |
|---------|---------|
| .exe | 🚀 |
| .ahk | 🔧 |
| .zip | 📦 |
| بقية الملفات | 📄 |

## المساهمة 🤝

نرحب بالمساهمات! يرجى فتح issue أو pull request

## الترخيص 📜

هذا المشروع مرخص تحت MIT License

## التواصل 📞

- Discord: d.qq
- TikTok: @Draw.Store1

---

تم إنشاء هذا المشروع بحب ❤️ لمساعدة المطورين
