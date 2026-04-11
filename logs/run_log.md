# Run Log – FIT4012 Lab 1

## Thông tin môi trường

- Ngày chạy: 4/11/2026
- Công cụ: Python 3 (test script tương đương C++)

## Kết quả chạy chương trình

### 1. Entropy và Redundancy

#### Test case 1: "aaaa"

```
Input: 'aaaa'
  Entropy: 0.000000
  Redundancy: 8.000000
```

**Nhận xét**: Entropy = 0 vì chỉ có 1 ký tự duy nhất, redundancy = 8 (tối đa).

#### Test case 2: "abcd"

```
Input: 'abcd'
  Entropy: 2.000000
  Redundancy: 6.000000
```

**Nhận xét**: Entropy = 2 (4 ký tự khác nhau, mỗi ký tự xác suất 1/4), redundancy = 6.

#### Test case 3: "hello world"

```
Input: 'hello world'
  Entropy: 2.845351
  Redundancy: 5.154649
```

**Nhận xét**: Entropy khoảng 2.845, redundancy khoảng 5.155.

### 2. Modular Inverse

#### Test case 1: a=3, m=7

```
a=3, m=7 -> nghịch đảo = 5, kiểm tra: 3*5 mod 7 = 1
```

**Kết quả**: Đúng (kỳ vọng = 5)

#### Test case 2: a=10, m=17

```
a=10, m=17 -> nghịch đảo = 12, kiểm tra: 10*12 mod 17 = 1
```

**Kết quả**: Đúng (kỳ vọng = 12)

#### Test case 3: a=6, m=9

```
a=6, m=9 -> Không tồn tại nghịch đảo
```

**Kết quả**: Đúng (gcd(6,9) = 3 ≠ 1)

## Kết luận

Tất cả test cases đều cho kết quả chính xác.
