# الرفع على الإنترنت 🌐

دليل شامل لرفع DrawStore-Loader على خوادم مختلفة

---

## 1️⃣ Railway (الخيار الأسهل والمجاني) ⭐

### المميزات:
- ✅ مجاني 100%
- ✅ بدء سريع جداً
- ✅ دعم تلقائي للـ Git
- ✅ SSL مجاني
- ✅ لوحة تحكم سهلة

### الخطوات:

#### أ) تحضير المستودع على GitHub
```bash
# انسخ المشروع أو أنشئ مستودع جديد
git init
git add .
git commit -m "Initial DrawStore-Loader commit"
git remote add origin https://github.com/YOUR_USERNAME/DrawStore-Loader.git
git push -u origin main
```

#### ب) الرفع على Railway
1. اذهب إلى https://railway.app
2. اضغط "Login" وسجل دخول بـ GitHub
3. اضغط "New Project"
4. اختر "Deploy from GitHub"
5. اختر مستودعك
6. Railway سيكتشف `requirements.txt` و `Procfile` تلقائياً
7. اضغط "Deploy"

#### ج) الحصول على الرابط
```
رابطك سيكون مثل:
https://drawstore-loader-production.up.railway.app
```

---

## 2️⃣ Heroku (مجاني مع تحديود)

### المميزات:
- ✅ سهل جداً
- ✅ دعم طويل الأجل
- ✅ SSL مجاني
- ⚠️ قد يكون بطيء قليلاً

### الخطوات:

```bash
# تثبيت Heroku CLI
# Windows: https://devcenter.heroku.com/articles/heroku-cli

# تسجيل الدخول
heroku login

# إنشاء التطبيق
heroku create drawstore-loader

# رفع المشروع
git push heroku main

# عرض السجلات
heroku logs --tail
```

---

## 3️⃣ PythonAnywhere (سهل جداً)

### المميزات:
- ✅ تصميم بسيط جداً
- ✅ دعم عربي جيد
- ✅ سهل للمبتدئين
- ✅ SSL متوفر

### الخطوات:

1. اذهب إلى https://www.pythonanywhere.com
2. سجل حساب جديد
3. اضغط "Files" وارفع الملفات
4. اذهب إلى "Web" وأنشئ تطبيق Flask جديد
5. اختر Python 3.10
6. أشر إلى ملف `app.py`

---

## 4️⃣ Render (ممتاز)

### المميزات:
- ✅ أداء عالي
- ✅ مجاني مع حد أدنى
- ✅ SSL مجاني
- ✅ سهل جداً

### الخطوات:

1. اذهب إلى https://render.com
2. سجل دخول بـ GitHub
3. اضغط "New +" ثم "Web Service"
4. اختر مستودع GitHub
5. استخدم الإعدادات التالية:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`

---

## 5️⃣ Docker (للسيرفرات الشخصية)

### التشغيل المحلي:

```bash
# بناء الصورة
docker build -t drawstore-loader .

# تشغيل الحاوية
docker run -p 5000:5000 -v $(pwd)/files:/app/files drawstore-loader
```

### أو باستخدام Docker Compose:

```bash
docker-compose up -d
```

---

## 6️⃣ VPS شخصي (Linode, DigitalOcean, etc.)

### التثبيت على Ubuntu/Debian:

```bash
# تحديث النظام
sudo apt update && sudo apt upgrade -y

# تثبيت Python وPip
sudo apt install python3 python3-pip -y

# استنساخ المشروع
git clone https://github.com/YOUR_USERNAME/DrawStore-Loader.git
cd DrawStore-Loader

# تثبيت المكتبات
pip3 install -r requirements.txt

# تشغيل مع Gunicorn (للإنتاج)
pip3 install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### تشغيل في الخلفية مع systemd:

```bash
sudo nano /etc/systemd/system/drawstore.service
```

ضع هذا المحتوى:
```ini
[Unit]
Description=DrawStore Loader
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/DrawStore-Loader
ExecStart=/usr/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

ثم:
```bash
sudo systemctl daemon-reload
sudo systemctl enable drawstore
sudo systemctl start drawstore
```

---

## مقارنة سريعة 📊

| المنصة | المجاني | السهولة | الأداء | الدعم |
|-------|--------|--------|--------|------|
| Railway | ✅ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Render | ✅ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Heroku | ✅ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| PythonAnywhere | ✅ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Docker | ❌ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| VPS | ❌ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## نصائح مهمة 💡

1. **استخدم HTTPS دائماً** - تأكد من أن المنصة توفر شهادة SSL
2. **قم بعمل Backup** - احفظ ملف `download_stats.json` بانتظام
3. **راقب الموارد** - تحقق من استهلاك الـ Memory والـ CPU
4. **حدث البيانات** - اتبع آخر الإصدارات من Flask
5. **استخدم متغيرات البيئة** - لا تضع المفاتيح في الكود مباشرة

---

## استكشاف الأخطاء 🔧

### المشكلة: "ModuleNotFoundError: No module named 'flask'"
**الحل:**
```bash
pip install -r requirements.txt
```

### المشكلة: الملفات لا تبقى بعد إعادة التشغيل
**الحل:** استخدم `volumes` في Docker أو قاعدة بيانات

### المشكلة: البورت مشغول
**الحل:** غيّر البورت من خلال متغيرات البيئة

---

## تحتاج مساعدة إضافية؟

- 📖 اقرأ README.md
- 🚀 اقرأ QUICK_START.md
- 💬 تواصل على Discord: d.qq
- 🐛 أنشئ issue على GitHub

**نتمنى لك أوقاتاً موفقة! 🎉**
