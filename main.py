import numpy as np 
import os
import time


def  generate_donut(A, B):
      #on initialiser les array ou on storee les point du donut et les caracteree
    z = np.zeros((1760,))
    b = [' '] * 1760


     #ici on geener eles point du donbut
    for j in np.arange(0, 6.28, 0.07):
         for i in np.arange(0, 6.28, 0.02):
                  #les equation paremeetriquee pour deefinir la forme du donout
                  c = np.sin(i)
                  d = np.cos(j)
                  e = np.sin(A)
                  f = np.sin(j)
                  g = np.cos(A)
                  h = d + 2
                  D = 1 / (c * h * e + f * g + 5)
                  l = np.cos(i)
                  m = np.cos(B)
                  n = np.sin(B)
                  t = c * h * g - f * e
                  #on projete le dooonout en 3d dans lecran 2d de la personeuh
                  x = int(40 + 30 * D * (l * h * m - t * n))
                  y = int(12 + 15 * D * (l * h * m + t * m))
                  o = x + 80 * y
                  #on essayee de determiner l'illimunation en calculant la surefacee normal
                  N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                  #stocker les caractere represantent chaque point
                  if 22 > y > 0 and 80 > x > 0 and D > z[o]:
                       z[o] = D
                       b[o] = ".,-~:;=!*#$@" [N if N > 0 else 0]
    return B

def main():
      A = 0 #angle initiale de la rotation autour l'axe x et l'axe z
      B = 0 #angle initiale de la rotation autour de laxe y

      while True:
            #on genere la frame du donut
            donut_frame = generate_donut(A, B)

            #conosle clear mes couilles a base de os
            os.system('cls' if os.name == 'nt' else 'clear')

            #enfin pr int  la framee ACTUEL du donut
            print('\n'.join([''.join(str(donut_frame[i:i+80])) for i in range(0, 1760, 80)])) #SAUF QUE CA NE VEUT PAS??

            #on rotate le donut pour la frame suivantee 
            a += 0.04
            b += 0.02

            #delai
            time.sleep(0.03)

            #bouge le curseur pour overwrite la frame precedente
            print("\033[F" * 22, end= "")


if __name__ == "__main__":
     main()

#"erreur" l.51, l.61 TypeError: 'int' object is not subscriptable la putain de ta mere
















