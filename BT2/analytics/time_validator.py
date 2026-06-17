from datetime import datetime

def parse_and_inspect_date(date_str: str) -> datetime | None:
    """
    Chuyển đổi chuỗi ngày tháng sang đối tượng datetime và bẫy lỗi.
    Trả về đối tượng datetime nếu hợp lệ, trả về None nếu sai định dạng/ngày không tồn tại.
    """
    try:
        # Kiểm tra tính hợp lệ của ngày tháng theo định dạng YYYY-MM-DD
        valid_date = datetime.strptime(date_str, "%Y-%m-%d")
        return valid_date
    except ValueError:
        # Bẫy lỗi an toàn khi biên tập viên nhập sai (ví dụ: ngày 31 tháng 6)
        return None