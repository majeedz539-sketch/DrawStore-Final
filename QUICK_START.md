# البدء السريع 🚀

## على Windows

### 1. فتح Command Prompt أو PowerShell
- اضغط `Win + R` وأكتب `cmd`
- أو ابحث عن PowerShell

### 2. توجه إلى مجلد المشروع
```powershell
cd C:\Users\Ray\Desktop\Draw Mw3\DrawStore-Loader
```

### 3. تثبيت المكتبات
```powershell
pip install -r requirements.txt
```

### 4. تشغيل التطبيق
```powershell
python app.py
```

أو ببساطة انقر على:
```
run.bat
```

### 5. الوصول للتطبيق
اذهب إلى: http://localhost:5000

---

## على Linux/Mac

```bash
cd ~/DrawStore-Loader
pip install -r requirements.txt
./run.sh
```

---

## إضافة الملفات للتحميل

1. افتح مجلد `files`
2. ضع ملفاتك فيه (أي ملفات: .exe, .ahk, .zip, إلخ)
3. حدّث الصفحة في المتصفح - ستظهر الملفات تلقائياً!

---

## مراجعة الإحصائيات

بعد أن يقوم شخص ما بتحميل ملف، ستجد:
- عدد التحميلات الإجمالي
- الـ IP الخاص بالشخص الذي قام بالتحميل
- الوقت الدقيق للتحميل

اذهب إلى: http://localhost:5000/stats

---

## المشاكل الشائعة

### المشكلة: `pip command not found`
**الحل:** تأكد من تثبيت Python بشكل صحيح
```powershell
python --version
```

### المشكلة: `Port 5000 is already in use`
**الحل:** غيّر البورت في البيئة:
```powershell
$env:PORT=5001
python app.py
```

### المشكلة: الملفات لا تظهر
**الحل:** 
1. تأكد من وضع الملفات في مجلد `files`
2. أعد تحديث الصفحة (F5)
3. تأكد من أن الملفات قابلة للقراءة

---

## الرفع على Railway

1. أنشئ حساب على https://railway.app
2. سجّل دخول باستخدام GitHub
3. اضغط "New Project"
4. اختر "Deploy from GitHub"
5. اختر مستودعك
6. Railway سيقوم بالباقي تلقائياً! ✨

---

## تحتاج مساعدة؟

- 📖 اقرأ README.md للتفاصيل الكاملة
- 🐛 تحقق من أخطاء في console output
- 💬 تواصل على Discord: d.qq

هل تحتاج إلى أي مساعدة؟ 💡
