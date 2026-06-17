from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date

# Dữ liệu đầu vào từ phòng hậu kỳ đã được chuẩn hóa cấu trúc
raw_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"}, # Ngày lỗi
    {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
]

def main():
    print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA =======")
    
    # Khởi tạo hạ tầng lưu trữ gốc an toàn
    safe_create_dir("media_vault")
    print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
    print("-" * 75)
    
    successful_count = 0
    total_files = len(raw_files)
    
    for file_info in raw_files:
        filename = file_info["filename"]
        size_bytes = file_info["size_bytes"]
        upload_at_str = file_info["upload_at"]
        
        print(f"[TỆP TIN: {filename}]")
        
        # Kiểm tra tính hợp lệ của ngày upload trước khi xử lý lưu trữ
        parsed_date = parse_and_inspect_date(upload_at_str)
        
        if parsed_date is None:
            print(f" + Trạng thái: 🔴 THẤT BẠI (Lỗi: Định dạng ngày upload '{upload_at_str}' không tồn tại)")
            print()
            continue
            
        # Tính toán dung lượng lưu trữ thực tế theo cấu trúc Blocks
        disk_blocks = calculate_disk_blocks(size_bytes, block_size=4096)
        
        # Phân loại thư mục lưu trữ dựa vào đuôi mở rộng của tệp tin
        file_extension = filename.split(".")[-1].lower()
        category = "video" if file_extension == "mp4" else "audio"
        
        # Tiến hành tạo thư mục phân loại thực tế giả định trên ổ đĩa production
        target_path = f"media_vault/{category}"
        safe_create_dir(target_path)
        
        print(f" + Dung lượng thực tế: {size_bytes:,} Bytes")
        print(f" + Số khối phân vùng (4KB Block): {disk_blocks} Blocks")
        print(f" + Trạng thái: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{category}')")
        print()
        
        successful_count += 1
        
    print("========================================================")
    print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {successful_count}/{total_files} tệp tin thành công. Hệ thống ổn định.")

if __name__ == "__main__":
    main()