import math
import cv2
import RGB2YUV


class DCT:
    def fill(self, img):
        width = len(img[0])
        height = len(img)
        if height % 8 != 0:
            for i in range(8 - height % 8):
                img.append([0 for i in range(width)])
        if width % 8 != 0:
            for row in img:
                for i in range(8 - width % 8):
                    row.append(0)

        return img

    def split(self, img):
        width = len(img[0])
        height = len(img)
        blocks = []
        for i in range(height // 8):
            for j in range(width // 8):
                temp = [[0 for i in range(8)] for i in range(8)]
                for r in range(8):
                    for c in range(8):
                        temp[r][c] = img[i * 8 + r][j * 8 + c]
                blocks.append(temp)
        return blocks

    def merge(self, imgY, imgU, imgV, height, width):
        Yheight = (height - 1) // 8 + 1
        Ywidth = (width - 1) // 8 + 1
        UVheight = (height - 1) // 2 // 8 + 1
        UVwidth = (width - 1) // 2 // 8 + 1
        Y = [[0 for i in range(Ywidth * 8)] for i in range(Yheight * 8)]
        U = [[0 for i in range(UVwidth * 8)] for i in range(UVheight * 8)]
        V = [[0 for i in range(UVwidth * 8)] for i in range(UVheight * 8)]
        for i in range(Yheight):
            for j in range(Ywidth):
                for r in range(8):
                    for c in range(8):
                        Y[i * 8 + r][j * 8 + c] = imgY[i * Ywidth + j][r][c]
        for i in range(UVheight):
            for j in range(UVwidth):
                for r in range(8):
                    for c in range(8):
                        U[i * 8 + r][j * 8 + c] = imgU[i * UVwidth + j][r][c]
                        V[i * 8 + r][j * 8 + c] = imgV[i * UVwidth + j][r][c]
        while len(Y) > height:
            Y.pop()
        for row in Y:
            while len(row) > width:
                row.pop()
        while len(U) > (height - 1) // 2 + 1:
            U.pop()
            V.pop()
        for row in U:
            while len(row) > (width - 1) // 2 + 1:
                row.pop()
        for row in V:
            while len(row) > (width - 1) // 2 + 1:
                row.pop()

        return Y, U, V

    def C(self, n):
        if n == 0:
            return pow(2, 1/2)/2
        else:
            return 1

    def FDCT(self, block):
        temp = [[0 for i in range(8)] for i in range (8)]
        for u in range(8):
            for v in range(8):
                n = 0
                for i in range(8):
                    for j in range(8):
                        n += math.cos((2 * i + 1) * u * math.pi / 16) * math.cos((2 * j + 1) * v * math.pi / 16) * \
                             block[i][j]
                temp[u][v] = round(self.C(u) * self.C(v) / 4 * n)
        return temp

    def IDCT(self, block):
        temp = [[0 for i in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                n = 0
                for u in range(8):
                    for v in range(8):
                        n += math.cos((2 * i + 1) * u * math.pi / 16) * math.cos((2 * j + 1) * v * math.pi / 16) * \
                             block[u][v] * self.C(u) * self.C(v) / 4
                temp[i][j] = round(n)
        return temp

'''
img = cv2.imread("../photograph.jpg")
Y, U, V = RGB2YUV.rgb2yuv(img, img.shape[1], img.shape[0])
print(len(img), len(img[0]))
test = DCT()
Y = test.fill(Y)
print(len(Y), len(Y[0]))
blocks = test.split(Y)
first = blocks[0]
print(len(first), len(first[0]))
for row in first:
    print(row)
print("\n")
first = test.FDCT(first)
for row in first:
    print(row)
'''
'''
test = DCT()
D = \
    [
        [-81.0, 111.0, 186.0, 84.0, 38.0, 30.0, -44.0, 52.0],
        [96.0, 299.0, -87.0, -65.0, -1.0, -41.0, -48.0, -2.0],
        [-87.0, 61.0, 132.0, -17.0, -1.0, -2.0, -1.0, -46.0],
        [55.0, -301.0, 18.0, 116.0, -40.0, -1.0, 63.0, 2.0],
        [83.0, 18.0, -60.0, 46.0, 54.0, 3.0, -79.0, 60.0],
        [82.0, -27.0, -49.0, -52.0, 3.0, 78.0, -4.0, 4.0],
        [36.0, 52.0, -62.0, -1.0, -2.0, 4.0, 7.0, -6.0],
        [2.0, -75.0, -2.0, 2.0, 1.0, 78.0, -1.0, 0.0]
    ]
temp = test.IDCT(D)
for row in temp:
    print(row)
'''