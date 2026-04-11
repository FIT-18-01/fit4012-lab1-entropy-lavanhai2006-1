# Run Log - FIT4012 Lab 1

## Thong tin moi truong

- Ngay chay: 4/11/2026
- Cong cu: Python 3 (test script tuong duong C++)

## Ket qua chay chuong trinh

### 1. Entropy va Redundancy

#### Test case 1: "aaaa"

```
Input: 'aaaa'
  Entropy: 0.000000
  Redundancy: 8.000000
```

**Nhan xet**: Entropy = 0 vi chi co 1 ky tu duy nhat, redundancy = 8 (toi da).

#### Test case 2: "abcd"

```
Input: 'abcd'
  Entropy: 2.000000
  Redundancy: 6.000000
```

**Nhan xet**: Entropy = 2 (4 ky tu khac nhau, moi ky tu xac suat 1/4), redundancy = 6.

#### Test case 3: "hello world"

```
Input: 'hello world'
  Entropy: 2.845351
  Redundancy: 5.154649
```

**Nhan xet**: Entropy khoang 2.845, redundancy khoang 5.155.

### 2. Modular Inverse

#### Test case 1: a=3, m=7

```
a=3, m=7 -> nghich dao = 5, kiem tra: 3*5 mod 7 = 1
```

**Ket qua**: Dung (ky vong = 5)

#### Test case 2: a=10, m=17

```
a=10, m=17 -> nghich dao = 12, kiem tra: 10*12 mod 17 = 1
```

**Ket qua**: Dung (ky vong = 12)

#### Test case 3: a=6, m=9

```
a=6, m=9 -> Khong ton tai nghich dao
```

**Ket qua**: Dung (gcd(6,9) = 3 != 1)

## Ket luan

Tat ca test cases deu cho ket qua chinh xac.
