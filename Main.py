
## Triangular star pattern with Python
'''
- Right triangle = Segitiga siku siku
- Inverted right triangle = Segitiga siku siku terbalik
- Equilateral triangle = Segitiga sama sisi
- Pascal's triangle = Segitiga pascal
'''

def validateInput():
  n = len(triangle);
  index = triangle_option;
  if 0 <= index <= n:
    # Jika pilihan sesuai yang tertera, maka kembalikan nilai
    return;
  else:
    raise ValueError(f'Masukkan pilihan sesuai nomor yang tertera dari 1 - {n}. Coba lagi!');

def show_triangle_list():
  for index, show_option in enumerate(triangle, start=1):
    print(f'{index}. {show_option[1]}');
# ==========================================================================================

# Jenis-jenis bentuk segitiga
def right_triangle(limit):
  for i in range(1, limit + 1):
    print(f'{star}' * i);

def inverted_right_triangle(limit):
  for i in range(limit, 0, -1):
    print(f'{star}' * i);

def equilateral_triangle(limit):
  for i in range(limit):
    print(' ' * (limit - i - 1), end = '');
    print(star * (2 * i + 1));

def pascal_triangle(limit):
  for line in range(1, limit + 1):
    C = 1; # Nilai pertama pada setiap baris selalu 1
    for i in range(1, line + 1):
      print(C, end=' ');
      C = C * (line - i) // i;
    print();
# ============================================================

def process_the_limit_input(limit, triangle_option): # Menyimpan 2 parameter untuk di proses ke jenis segitiga yang dipilih
  if triangle_option == triangle[0]:right_triangle(limit);
  elif triangle_option == triangle[1]:inverted_right_triangle(limit);
  elif triangle_option == triangle[2]:equilateral_triangle(limit);
  elif triangle_option == triangle[3]:pascal_triangle(limit);

# ============================================================================================

triangle = [
  [right_triangle, 'Segitiga siku-siku'],
  [inverted_right_triangle, 'Segitiga siku-siku terbalik'],
  [equilateral_triangle, 'Segitiga sama sisi'],
  [pascal_triangle, 'Segitiga pascal']
];
star = '*';

# User input
show_triangle_list();
triangle_option = int(input('\n==================\n\nPilih opsi segitiga yang kamu inginkan!\n-> '));
validateInput(); #! Validate input

triangle_option = triangle_option - 1;
print (f'kamu memilih: {triangle[triangle_option][1]}\n');

limit = int(input('Masukkan ukuran dengan angka berapapun: -> '));
print (f'Ukuran: {limit} x {limit}\n==============\n');

# Output
process_the_limit_input(limit, triangle[triangle_option]);