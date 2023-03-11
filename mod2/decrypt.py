import sys


def decrypt(cipher):
    points = '..'
    point = '.'
    while True:
        if points in cipher:
            index = cipher.index(points)
            if index == 0:
                cipher = cipher[2:]
            else:
                cipher = cipher[:(index-1)] + cipher[(index+2):]
        elif point in cipher:
            index = cipher.index(point)
            cipher = cipher[:index] + cipher[(index+1):]
        else:
            return cipher


if __name__ == '__main__':
    cipher = sys.stdin.read()
    print(decrypt(cipher))
