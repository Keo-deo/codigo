def fatorial(n):
     if n == 1:
         return 1
     return n * fatorial(n-1)
#4 - fatorial (4 - 1) ou sj fatorial(3)
#entao return 4 * fatorial(3)



print(fatorial(4))