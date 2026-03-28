import httpx
import asyncio
from src.models.schemas import Document

# 1. Hàm cào Wikipedia thật (Async)
async def fetch_wikipedia(query: str) -> Document:
    print(f"[Wiki] Bắt đầu tìm kiếm từ khóa: {query}...")
    
    # API chuẩn của Wikipedia
    url = f"https://vi.wikipedia.org/api/rest_v1/page/summary/{query}"
    
    # Mở một "trình duyệt ảo" bằng httpx
    async with httpx.AsyncClient() as client:
        try:
            # await: "Treo" hàm này ở đây để đi làm việc khác, chờ khi nào Wiki trả lời thì quay lại lấy
            response = await client.get(url, timeout=5.0)
            
            if response.status_code == 200:
                data = response.json()
                print("[Wiki] -> Đã lấy xong dữ liệu!")
                # Ép dữ liệu vào khuôn Document (Pydantic)
                return Document(
                    title=data.get("title", query),
                    url=data.get("content_urls", {}).get("desktop", {}).get("page", url),
                    content=data.get("extract", "Không có tóm tắt."),
                    source_type="wiki",
                    relevance_score=0.9
                )
        except Exception as e:
            print(f"[Wiki] Lỗi kết nối: {e}")
            
    # Trả về Document rỗng nếu không tìm thấy để hệ thống không bị crash
    return Document(title=query, url=url, content="Không tìm thấy dữ liệu.", source_type="wiki", relevance_score=0.0)

# 2. Hàm giả lập đọc file PDF nội bộ (Async)
async def fetch_local_pdf(query: str) -> Document:
    print(f"[PDF] Đang quét ổ cứng tìm tài liệu về: {query}...")
    # Giả lập máy tính mất 2 giây để đọc file PDF (await sleep)
    await asyncio.sleep(2.0) 
    print("[PDF] -> Đã đọc xong file!")
    
    return Document(
        title=f"Tài liệu nội bộ: {query}",
        url="file://data/ai_slide.pdf",
        content="Đây là nội dung giả lập đọc từ slide bài giảng.",
        source_type="pdf",
        relevance_score=0.85
    )

# 3. HÀM CHÍNH: Gom tất cả lại và chạy song song
async def gather_all_sources(query: str) -> list[Document]:
    print(f"\n--- KHỞI ĐỘNG AI AGENT ĐI TÌM: '{query}' ---")
    
    # Tuyệt chiêu asyncio.gather: Bắn cả 2 request đi CÙNG MỘT LÚC
    results = await asyncio.gather(
        fetch_wikipedia(query),
        fetch_local_pdf(query)
    )
    return list(results)