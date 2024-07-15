# Hướng Dẫn Sử Dụng Photoreviewer

Photoreviewer là một ứng dụng giúp bạn duyệt và ôn tập các hình ảnh trong một thư mục, bao gồm ảnh trong thư mục và toàn bộ các thư mục con. Photoreviewer là một phiên bản đơn giản của Anki, nhưng chỉ hoạt động với ảnh và thứ tự xuất hiện của các nội dung có yếu tố ngẫu nhiên.

Nguyên lý cơ bản của Photoreviewer là một hình ảnh càng được bấm thích nhiều lần càng xuất hiện với tần suất cao hơn, nhưng tất cả ảnh vẫn xuất hiện ngẫu nhiên. (Việc bấm nút thích làm thay đổi phân bố xác suất.) Bạn có thể chụp màn hình khu vực bạn muốn học và bấm thích những hình mà bạn muốn ôn tập lại.

Ngoài ra thì Photoreviewer có thể được dùng như một ứng dụng xem ảnh nhỏ gọn có tích hợp chức năng nhận diện văn bản.

Để bắt đầu sử dụng, hãy tải Photoreviewer.zip từ Github và giải nén.

https://github.com/quyhoang/Photoreviewer

## Điểm Chính Của Ứng Dụng

Mục tiêu chính của Photoreviewer là giúp người dùng quản lý hình ảnh một cách hiệu quả và tiện lợi. Các chức năng chính của ứng dụng bao gồm:

- Xem hình ảnh
- Thích và tăng xác suất hiển thị các hình ảnh đã thích
- Nhận dạng và sao chép văn bản từ hình ảnh
- Mở hình ảnh trong trình quản lý tệp

## Hướng Dẫn Sử Dụng

### Khởi Động Ứng Dụng

- Để khởi động ứng dụng, bạn chỉ cần chạy tệp `Photoreviewer.exe` hoặc click chuột phải lên một file ảnh và chọn `Open with → Choose another app → Choose an app on your PC` , sau đó chọn file Photoreviewer.exe trong máy tính.
- Khi bạn chỉ click vào `Photoreviewer.exe` , ứng dụng sẽ mở ảnh trong thư mục Pictures của bạn. Khi bạn mở ứng dụng này bằng cách chọn `Open with` từ một bức ảnh, ứng dụng sẽ mở ảnh trong thư mục chứa bức ảnh đó và các thư mục con của nó.

### Phím Tắt (Keyboard Shortcuts)

Ứng dụng Photoreviewer hỗ trợ nhiều phím tắt để tăng tốc độ và hiệu quả quản lý hình ảnh. Sau đây là danh sách các phím tắt và chức năng tương ứng:

- **Phím Mũi Tên Phải (Right Arrow Key)**: Xem hình ảnh tiếp theo (ngẫu nhiên)
- **Phím Mũi Tên Trái (Left Arrow Key)**: Xem hình ảnh trước đó.
- **Phím Mũi Tên Lên (Up Arrow Key)**: Thích hình ảnh hiện tại và tăng xác suất hiển thị hình ảnh này.
- **Phím Mũi Tên Xuống (Down Arrow Key)**: Di chuyển hình ảnh hiện tại vào thư mục "cleared". Mọi ảnh trong thư mục “cleared” sẽ không xuất hiện trở lại. Để xem ảnh đó, nhấn phím `End` để đổi tên thư mục “cleared” thành “reviewed” và kết thúc phiên làm việc. Khi bắt đầu phiên làm việc mới, các ảnh trong thư mục “reviewed” sẽ được xuất hiện nếu bạn mở ứng dụng từ thư mục chứa “reviewed”.
- **Phím Delete (Delete Key)**: Xóa hình ảnh hiện tại.
- **Phím Enter (Return Key)**: Mở hình ảnh hiện tại trong trình quản lý tệp (Window Explorers)
- **Phím "o"**: Nhận dạng văn bản từ hình ảnh hiện tại và sao chép vào clipboard.
- **Phím Home**: Mở trang này (trang hướng dẫn)
- **Phím End**: Đổi tên thư mục "cleared" thành "reviewed" và thoát ứng dụng.

### Thư Mục

- **Thư Mục Hình Ảnh**: Photoreviewer sẽ mặc định sử dụng thư mục "Pictures" của người dùng để lấy hình ảnh. Bạn cũng có thể chỉ định một thư mục khác thông qua dòng lệnh khi khởi chạy ứng dụng.
- **Thư Mục "cleared"**: Hình ảnh được di chuyển vào thư mục này khi bạn nhấn phím mũi tên xuống.
- **Thư Mục "reviewed"**: Thư mục "cleared" sẽ được đổi tên thành "reviewed" khi bạn nhấn phím End để kết thúc và thoát ứng dụng.

## Lưu Ý

- Để nhận dạng văn bản, ứng dụng sử dụng thư viện pytesseract và hỗ trợ nhận dạng tiếng Anh, Nhật, và Việt.
- Khi nhận dạng văn bản, kết quả sẽ được sao chép vào clipboard để bạn có thể dán vào các ứng dụng khác.
- Ứng dụng sẽ hiển thị các thông báo tạm thời để xác nhận hành động của bạn như "Liked", "Cleared", "Deleted",...

Chúc bạn sử dụng Photoreviewer hiệu quả và tiện lợi!
