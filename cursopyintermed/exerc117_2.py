def mult(multiplier):
    def mult2(num):
        return num * multiplier
    return mult2

duplicar = mult(2)
triplicar = mult(3)
quadruplicar = mult(4)

print(f'{duplicar(5)} \n'
      f'{triplicar(5)} \n'
        f'{quadruplicar(5)} \n'
)

