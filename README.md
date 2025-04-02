# Chess AI with Pygame

Đây là một dự án cờ vua đơn giản được xây dựng bằng Python sử dụng thư viện `pygame` cho giao diện đồ họa và thư viện `python-chess` để quản lý logic bàn cờ và các nước đi hợp lệ. AI đối thủ sử dụng thuật toán Minimax với cắt tỉa Alpha-Beta để quyết định nước đi tốt nhất.

## Tính năng

* Giao diện đồ họa bàn cờ vua.
* Người chơi (Trắng) đấu với AI (Đen).
* Hiển thị các quân cờ bằng ký tự Unicode.
* Xử lý nước đi của người chơi thông qua click chuột.
* AI sử dụng thuật toán Minimax với cắt tỉa Alpha-Beta.
* Hàm đánh giá bàn cờ cơ bản dựa trên giá trị quân cờ.
* Phát hiện các trạng thái kết thúc ván cờ (Chiếu hết, Hòa cờ).
* Đánh dấu ô cờ đang được chọn.

## Yêu cầu

* Python 3.9 trở lên
* Thư viện Pygame
* Thư viện python-chess

## Cài đặt

1.  **Clone repository (hoặc tải mã nguồn):**
    ```bash
    git clone <your-repository-link> # Hoặc giải nén file zip nếu bạn tải về
    cd <tên-thư-mục-dự-án>
    ```

2.  **Cài đặt các thư viện cần thiết:**
    Mở terminal hoặc command prompt trong thư mục dự án và chạy lệnh sau:
    ```bash
    pip install -r requirements.txt
    ```
    *(Lệnh này sẽ đọc file `requirements.txt` và cài đặt `pygame` và `python-chess`)*

## Cách chạy

Để bắt đầu trò chơi, chạy file Python chính từ terminal hoặc command prompt:

```bash
python <tên_file_python_của_bạn>.py
