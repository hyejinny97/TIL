# ✔ 컴퓨터에서의 진법

# ✔ 진법 변환

# ✔ 파이썬에서 진법 변환
> 10진수 ⇆ 2진수 변환
1. 10진수 → 2진수 변환
   
   ```python
   print('{:b}'.format(10))
   # '1010'
   ```

   ```python
   print(bin(10))
   # 0b1010
   ```

2. 2진수 → 10진수 변환
   
   - `int(str, radix)`: radix진수로 표현된 문자열을 10진수로 변환 후 반환함
   
   ```python
   print(int('1010', 2))
   # 10
   ```

> 10진수 ⇆ 8진수 변환
1. 10진수 → 8진수 변환
   
   ```python
   print('{:o}'.format(10))
   # '12'
   ```

   ```python
   print(oct(10))
   # 0o12
   ```

2. 8진수 → 10진수 변환
   
   - `int(str, radix)`: radix진수로 표현된 문자열을 10진수로 변환 후 반환함
   
   ```python
   print(int('12', 8))
   # 10
   ```

> 10진수 ⇆ 16진수 변환
1. 10진수 → 16진수 변환
   
   ```python
   print('{:x}'.format(10))
   # 'a'
   ```

   ```python
   print(hex(10))
   # 0xa
   ```

2. 16진수 → 10진수 변환
   
   - `int(str, radix)`: radix진수로 표현된 문자열을 10진수로 변환 후 반환함
   
   ```python
   print(int('10', 8))
   # 16
   ```
