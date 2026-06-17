import os

def safe_create_dir(path: str) -> None:
    """
    Khởi tạo thư mục một cách an toàn (hỗ trợ đường dẫn lồng nhau).
    Nếu thư mục đã tồn tại thì tự động bỏ qua, tránh crash hệ thống.
    """
    os.makedirs(path, exist_ok=True)