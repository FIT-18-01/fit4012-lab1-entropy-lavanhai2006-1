# Report 1 Page - FIT4012 Lab 1

## 1. Muc tieu

Bai lab nham giup sinh vien:

- Hieu va chay duoc chuong trinh tinh entropy cua mot chuoi ky tu.
- Bo sung chuc nang tinh do du thua thong tin dua tren entropy thuc te.
- Cai dat ham tim nghich dao modulo bang thuat toan Euclid mo rong.

## 2. Cach lam

- Doc hieu chuong trinh entropy mau (ham `calculate_entropy`).
- Bo sung ham `calculate_redundancy` voi cong thuc: Redundancy = log2(256) - H(X).
- Hoan thien ham `mod_inverse` su dung thuat toan Euclid mo rong.
- Chay thu tren nhieu test case de kiem tra tinh dung dan.

## 3. Ket qua chinh

### 3.1 Entropy va redundancy

| Input       | Entropy | Redundancy | Nhan xet                                       |
| ----------- | ------: | ---------: | ---------------------------------------------- |
| aaaa        |   0.000 |      8.000 | Entropy = 0 (chi 1 ky tu), redundancy toi da   |
| abcd        |   2.000 |      6.000 | Entropy = 2 (4 ky tu deu nhau), redundancy = 6 |
| hello world |   2.845 |      5.155 | Entropy trung binh, redundancy khoang 5.155    |

### 3.2 Modulo inverse

|   a |   m | Ket qua mong doi | Ket qua chuong trinh |
| --: | --: | ---------------- | -------------------- |
|   3 |   7 | 5                | 5                    |
|  10 |  17 | 12               | 12                   |
|   6 |   9 | Khong ton tai    | Khong ton tai        |

## 4. Ket luan

- **Bai hoc rut ra**: Hieu ro hon ve khai niem entropy trong ly thuyet thong tin va cach tinh nghich dao modulo su dung thuat toan Euclid mo rong.
- **Kho khan lon nhat**: Hieu cach hoat dong cua thuat toan Euclid mo rong va cach ap dung de tim nghich dao modulo.
- **Dieu giup hieu ro hon**: Viec chay thu cac test cases cu the giup kiem chung tinh dung dan cua thuat toan va cung co kien thuc ly thuyet.
