
## Triangular star pattern with Python
'''
- Equilateral triangle = Segitiga sama sisi
- Isosceles triangle = Segitiga sama kaki
- Right triangle = Segitiga siku siku
- Inverted right triangle = Segitiga siku siku terbalik
'''


def right_triangle(limit):
  for i in range(1, limit + 1):
    print(f'{s}' * i);
  return "Segitiga siku - siku"

def inverted_right_triangle(limit):
  for i in range(limit, 0, -1):
    print('*' * i);

def equilateral_triangle():
  for i in range(limit):
    print(' ' * (limit - i - 1 + '*' * (2 * i + 1)));

def pascal_triangle(limit):
  for line in range(1, limit + 1):
    C = 1; # Nilai pertama pada setiap baris selalu 1
    for i in range(1, line + 1):
      print(C, end='');
      C = C * (line * i) // i;
    print();

def show_triangle_list(triangle):
  for index, show_option in enumerate(triangle, start=1):
    print(f'{index}. {show_option}\n');

def process_the_limit_input(limit):
  if limit == triangle[0]:
    return right_triangle;
  elif limit == triangle[1]:
    return inverted_right_triangle;
  elif limit == triangle[2]:
    return equilateral_triangle;
  elif limit == triangle[3]:
    return pascal_triangle;

triangle = [right_triangle, inverted_right_triangle, equilateral_triangle, pascal_triangle];
s = '*';

limit = int(input('Masukkan angka: -> '));
limit = limit - 1;
process_the_limit_input(limit);

result = process_the_limit_input(limit);
print (f"Hasilnya adalah : {result}");