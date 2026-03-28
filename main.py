from fastapi import FastAPI
import uvicorn
from src.models.schemas import ResearchQuery, ResearchReport
from src.fetchers.sources import gather_all_sources
from src.ai.llm import generate_summary

# Khởi tạo ứng dụng FastAPI với tiêu đề cực ngầu
app = FastAPI(
    title="Async AI Research Agent API",
    description="Hệ thống tự động thu thập tài liệu và tóm tắt bằng Gemini 2.5 Flash",
    version="1.0.0"
)

# Tạo một Endpoint (Đường dẫn) nhận yêu cầu POST
@app.post("/api/research", response_model=ResearchReport)
async def research_topic(request: ResearchQuery):
    print(f"\n[API] Nhận được yêu cầu nghiên cứu: '{request.query}'")
    
    # 1. Cào dữ liệu song song (Async)
    documents = await gather_all_sources(request.query)
    
    # 2. Gửi cho Gemini tóm tắt
    report = await generate_summary(request.query, documents)
    
    print("[API] Trả kết quả về cho người dùng thành công!")
    # FastAPI sẽ tự động chuyển đổi object ResearchReport này thành JSON cực chuẩn
    return report

if __name__ == "__main__":
    # Lệnh để chạy Server trên máy ảo Localhost, cổng 8000
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)