#MERCI GOODKATT ALL CREDITS GOES TO HIM
import numpy as np 
import os
import time

def generate_donut(A, B):
    z = np.zeros((1760,))
    b = [' '] * 1760

    for j in np.arange(0, 6.28, 0.07):
        for i in np.arange(0, 6.28, 0.02):
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
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * m + t * m))
            o = x + 80 * y
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 22 > y > 0 and 80 > x > 0 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
    
    # Retourner 'b', pas 'B'
    return b

def main():
    A, B = 0, 0  # Initialisation des angles

    while True:
        donut_frame = generate_donut(A, B)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('\n'.join([''.join(donut_frame[i:i+80]) for i in range(0, 1760, 80)]))
        
        A += 0.04
        B += 0.02
        
        time.sleep(0.03)
        
        print("\033[F" * 22, end="")

if __name__ == "__main__":
    main()
#plus d'erreur car GoodKat est passer par la 
