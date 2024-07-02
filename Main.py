
## Triangular star pattern with Python
s = '*';
def triangle(limit):
  for i in range(1, limit + 1):
    print(f'{s}' * i);

limit = int(input('Masukkan angka: -> '));
print();
triangle(limit);