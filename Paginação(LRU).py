Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Digite a string de referências separadas por espaço: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
Digite o tamanho do frame de memória: 3

Traceback (most recent call last):
  File "C:\Users\Thyago Antonio\Desktop\testelru.py", line 22, in <module>
    for j in range (0,ref):
TypeError: range() integer end argument expected, got str.
>>> ================================ RESTART ================================
>>> 
Digite a string de referências separadas por espaço: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
Digite o tamanho do frame de memória: 3
Inserindo o 7

Miss
[7]

Inserindo o 0

Miss
[7, 0]

Inserindo o 1

Miss
[7, 0, 1]

Inserindo o 2

Miss
[2, 0, 1]

Inserindo o 0

Hit na página 4

Inserindo o 3

Miss
[2, 0, 3]

Inserindo o 0

Hit na página 6

Inserindo o 4

Miss
[4, 0, 3]

Inserindo o 2

Miss
[4, 0, 2]

Inserindo o 3

Miss
[4, 3, 2]

Inserindo o 0

Miss
[0, 3, 2]

Inserindo o 3

Hit na página 11

Inserindo o 2

Hit na página 12

Inserindo o 1

Miss
[1, 3, 2]

Inserindo o 2

Hit na página 14

Inserindo o 0

Miss
[1, 0, 2]

Inserindo o 1

Hit na página 16

Inserindo o 7

Miss
[1, 0, 7]

Inserindo o 0

Hit na página 18

Inserindo o 1

Hit na página 19

No total ocorream 8 hit(s) e 12 miss(es).
>>> ================================ RESTART ================================
>>> 
Digite a string de referências separadas por espaço: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
Digite o tamanho do frame de memória: 3
Inserindo o 7

Miss
[7]

Inserindo o 0

Miss
[7, 0]

Inserindo o 1

Miss
[7, 0, 1]

Inserindo o 2

Miss
[2, 0, 1]

Inserindo o 0

Hit na página 0

Inserindo o 3

Miss
[2, 0, 3]

Inserindo o 0

Hit na página 0

Inserindo o 4

Miss
[4, 0, 3]

Inserindo o 2

Miss
[4, 0, 2]

Inserindo o 3

Miss
[4, 3, 2]

Inserindo o 0

Miss
[0, 3, 2]

Inserindo o 3

Hit na página 3

Inserindo o 2

Hit na página 2

Inserindo o 1

Miss
[1, 3, 2]

Inserindo o 2

Hit na página 2

Inserindo o 0

Miss
[1, 0, 2]

Inserindo o 1

Hit na página 1

Inserindo o 7

Miss
[1, 0, 7]

Inserindo o 0

Hit na página 0

Inserindo o 1

Hit na página 1

No total ocorream 8 hit(s) e 12 miss(es).
>>> 
