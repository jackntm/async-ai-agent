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
# Clone và setup
git clone [https://github.com/HCMUT-student/OOknafy-Agent.git](https://github.com/HCMUT-student/OOknafy-Agent.git)
cd OOknafy-Agent
echo "GEMINI_API_KEY=your_actual_key" > .env

# Run với Docker
docker-compose up -d --build