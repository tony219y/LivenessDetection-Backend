# ใช้ Python 3.11 เป็น base image
FROM python:3.11

# ตั้ง working directory
WORKDIR /app

# คัดลอกไฟล์ทั้งหมดเข้า container
COPY . /app

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# เปิด port 8000 (ค่า default ของ FastAPI)
EXPOSE 8000

# รัน FastAPI ด้วย Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
 