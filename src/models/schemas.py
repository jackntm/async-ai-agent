from pydantic import BaseModel, Field #Kiểm tra và Ép kiểu dữ liệu (Data Validation).
from typing import Optional #Type Hinting

# 1. Khuôn mẫu cho một tài liệu thu thập được
class Document(BaseModel):
    title: str
    url: str
    content: str
    source_type: str = Field(..., description="Loại nguồn: 'web', 'wiki', hoặc 'pdf'")
    relevance_score: Optional[float] = Field(None, ge=0.0, le=1.0, description="Điểm liên quan từ 0->1")

# 2. Khuôn mẫu cho báo cáo tóm tắt cuối cùng trả về cho người dùng
class ResearchReport(BaseModel):
    query: str
    summary: str
    references: list[Document]

class ResearchQuery(BaseModel):
    query: str = Field(..., description="Từ khóa hoặc câu hỏi bạn muốn AI nghiên cứu", example="Trí tuệ nhân tạo")