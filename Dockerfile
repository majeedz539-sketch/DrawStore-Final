FROM python:3.10-slim

# تعيين مجلد العمل
WORKDIR /app

# نسخ المتطلبات
COPY requirements.txt .

# تثبيت المكتبات
RUN pip install --no-cache-dir -r requirements.txt

# نسخ الملفات
COPY . .

# إنشاء مجلد files
RUN mkdir -p files

# تعيين متغيرات البيئة
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0
ENV PORT=5000

# فتح البورت
EXPOSE 5000

# تشغيل التطبيق
CMD ["python", "app.py"]
