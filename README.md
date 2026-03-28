# 🚀 Async AI Research Agent - OOknafy

## Build-to-Intern Project | Python 3.10+ | FastAPI | AsyncIO | Gemini API | Docker

### 🛠️ Tech Stack

* Python 3.10+
* [google-genai](https://github.com/google-gemini/deprecations)
* FastAPI
* Pydantic
* httpx
* Docker

### 🚀 Features

* **OOknafy Architecture:** Một pipeline cào dữ liệu song song (AsyncIO), làm sạch (Pydantic), và chuẩn hóa (Type Hinting) dữ liệu từ nhiều nguồn khác nhau như Wikipedia, PDF, và Local files.
* **Tích hợp Gemini API:** Sử dụng model Gemini 2.5 Flash mạnh mẽ để tóm tắt kiến thức đa nguồn một cách thông minh.
* **FastAPI Backend:** Một API chuyên nghiệp với tài liệu Swagger UI tự động (`/docs`).
* **Containerization với Docker:** Dễ dàng triển khai và tái tạo môi trường bằng file `Dockerfile`.

### 📦 Quick Start with Docker

```bash
# Clone repository về máy
git clone [https://github.com/jackntm/async-ai-agent.git](https://github.com/jackntm/async-ai-agent.git)

# Di chuyển vào thư mục dự án
cd async-ai-agent

# Tạo file biến môi trường và điền API Key của bạn
echo "GEMINI_API_KEY=your_actual_key" > .env

# Khởi chạy hệ thống bằng Docker
docker compose up -d --build
