import math

def calculate_disk_blocks(size_bytes: int, block_size: int = 4096) -> int:
    """
    Tính chính xác số lượng khối ổ đĩa (blocks) tiêu tốn bằng cách làm tròn lên.
    Ví dụ: 4500 bytes ứng với block_size 4096 sẽ tiêu tốn 2 blocks.
    """
    if size_bytes <= 0:
        return 0
    return math.ceil(size_bytes / block_size)