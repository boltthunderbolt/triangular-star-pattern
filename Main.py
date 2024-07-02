
## Triangular star pattern with Python
'''
- Equilateral triangle = Segitiga sama sisi
- Isosceles triangle = Segitiga sama kaki
- Right triangle = Segitiga siku siku
- Inverted right triangle = Segitiga siku siku terbalik
'''

def show_triangle_list():
  for index, show_option in enumerate(triangle, start=1):
    print(f'{index}. {show_option[1]}');

# Jenis-jenis bentuk segitiga
def right_triangle(limit):
  for i in range(1, limit + 1):
    # proses print langsung ditunjukkan kesini
    print(f'{star}' * i); #todo: harus diubah caranya dengan sekali perintah print daripada di cetak di function langsung

def inverted_right_triangle(limit):
  for i in range(limit, 0, -1):
    print(f'{star}' * i);

def equilateral_triangle(limit):
  for i in range(limit):
    print(' ' * (limit - i - 1 + f'{star}' * (2 * i + 1)));

def pascal_triangle(limit):
  for line in range(1, limit + 1):
    C = 1; # Nilai pertama pada setiap baris selalu 1
    for i in range(1, line + 1):
      print(C, end='');
      C = C * (line * i) // i;
    print();
# ============================================================

#! proses mengambil hasil proses dari function jenis triangular-star-pattern belum berfungsi di function ini
#todo: seharusnya ini juga menjadi function mengambil hasil dari function jenis triangular-star-pattern
def process_the_limit_input(limit, triangle_option): # Menyimpan 2 parameter untuk di proses ke jenis segitiga yang dipilih
  if triangle_option == triangle[0]:
    hasil = right_triangle(limit);
    return hasil;
  elif triangle_option == triangle[1]:
    hasil = inverted_right_triangle(limit);
    return hasil;
  elif triangle_option == triangle[2]:
    hasil = equilateral_triangle(limit);
    return hasil;
  elif triangle_option == triangle[3]:
    hasil = pascal_triangle(limit);
    return hasil;



triangle = [
  [right_triangle, 'Segitiga siku-siku'],
  [inverted_right_triangle, 'Segitiga siku-siku terbalik'],
  [equilateral_triangle, 'Segitiga sama sisi'],
  [pascal_triangle, 'Segitiga pascal']
];
star = '*';

# User input
show_triangle_list();
triangle_option = int(input('Pilih opsi segitiga yang kamu inginkan!\n-> '));
triangle_option = triangle_option - 1;
print (f'kamu memilih: {triangle[triangle_option][1]}');


limit = int(input('Masukkan angka: -> '));

final_result = process_the_limit_input(limit, triangle[triangle_option]);