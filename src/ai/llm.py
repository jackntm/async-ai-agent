import os
import asyncio
from google import genai
from dotenv import load_dotenv
from src.models.schemas import Document, ResearchReport

# Tải API Key từ file .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Khởi tạo Client theo chuẩn SDK mới nhất (google-genai)
client = genai.Client(api_key=API_KEY)

async def generate_summary(query: str, docs: list[Document]) -> ResearchReport:
    print("\n[AI Brain] Đang gửi dữ liệu lên Google Gemini để phân tích...")
    
    # Lọc bỏ các tài liệu rác (relevance_score = 0)
    valid_docs = [doc for doc in docs if doc.relevance_score and doc.relevance_score > 0]
    
    if not valid_docs:
        return ResearchReport(
            query=query, 
            summary="Xin lỗi, tôi không tìm thấy dữ liệu nào hữu ích để tóm tắt.", 
            references=[]
        )
    
    # Nhào nặn dữ liệu (Prompt Engineering)
    context_text = "\n\n".join([f"Nguồn ({doc.source_type}): {doc.content}" for doc in valid_docs])
    
    prompt = f"""
    Bạn là một trợ lý nghiên cứu AI chuyên nghiệp.
    Dựa vào các tài liệu tham khảo dưới đây, hãy viết một đoạn tóm tắt ngắn gọn (khoảng 3-4 câu) 
    giải thích về chủ đề: "{query}".
    
    TÀI LIỆU THAM KHẢO:
    {context_text}
    """
    
    try:
        # Trong SDK mới, dùng client.aio để gọi API bất đồng bộ (Async)
        response = await client.aio.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt
        )
        summary_text = response.text
    except Exception as e:
        print(f"[AI Brain] Lỗi khi gọi API: {e}")
        summary_text = "Đã xảy ra lỗi trong quá trình tổng hợp dữ liệu từ AI."
        
    print("[AI Brain] -> Đã nhận được câu trả lời từ Gemini!")
    
    return ResearchReport(
        query=query,
        summary=summary_text.strip(),
        references=valid_docs
    )