# Report 1 Page – FIT4012 Lab 1

## 1. Mục tiêu

Bài lab nhằm giúp sinh viên:

- Hiểu và chạy được chương trình tính entropy của một chuỗi ký tự.
- Bổ sung chức năng tính độ dư thừa thông tin dựa trên entropy thực tế.
- Cài đặt hàm tìm nghịch đảo modulo bằng thuật toán Euclid mở rộng.

## 2. Cách làm

- Đọc hiểu chương trình entropy mẫu (hàm `calculate_entropy`).
- Bổ sung hàm `calculate_redundancy` với công thức: Redundancy = log₂(256) - H(X).
- Hoàn thiện hàm `mod_inverse` sử dụng thuật toán Euclid mở rộng.
- Chạy thử trên nhiều test case để kiểm tra tính đúng đắn.

## 3. Kết quả chính

### 3.1 Entropy và redundancy

| Input       | Entropy | Redundancy | Nhận xét                                       |
| ----------- | ------: | ---------: | ---------------------------------------------- |
| aaaa        |   0.000 |      8.000 | Entropy = 0 (chỉ 1 ký tự), redundancy tối đa   |
| abcd        |   2.000 |      6.000 | Entropy = 2 (4 ký tự đều nhau), redundancy = 6 |
| hello world |   2.845 |      5.155 | Entropy trung bình, redundancy khoảng 5.155    |

### 3.2 Modulo inverse

|   a |   m | Kết quả mong đợi | Kết quả chương trình |
| --: | --: | ---------------- | -------------------- |
|   3 |   7 | 5                | 5                    |
|  10 |  17 | 12               | 12                   |
|   6 |   9 | Không tồn tại    | Không tồn tại        |

## 4. Kết luận

- **Bài học rút ra**: Hiểu rõ hơn về khái niệm entropy trong lý thuyết thông tin và cách tính nghịch đảo modulo sử dụng thuật toán Euclid mở rộng.
- **Khó khăn lớn nhất**: Hiểu cách hoạt động của thuật toán Euclid mở rộng và cách áp dụng để tìm nghịch đảo modulo.
- **Điều giúp hiểu rõ hơn**: Việc chạy thử các test cases cụ thể giúp kiểm chứng tính đúng đắn của thuật toán và củng cố kiến thức lý thuyết.
