# 1. Kéo hệ điều hành Linux siêu nhẹ (chỉ khoảng 114MB) có cài sẵn Python 3.10
FROM python:3.10-slim

# 2. Tạo một thư mục ảo tên là /app bên trong container để làm việc
WORKDIR /app

# 3. Copy file thực đơn vào trước
COPY requirements.txt .

# 4. Cài đặt các thư viện AI, FastAPI (dùng --no-cache-dir để container nhẹ hơn)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy toàn bộ code của bạn (thư mục src, file main.py) vào thư mục /app
COPY . .

# 6. Mở cửa số 8000 để container có thể nhận yêu cầu từ web
EXPOSE 8000

# 7. Lệnh khởi chạy Server. Chú ý host là 0.0.0.0 để nó nhận mọi kết nối
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]