class Quantization:
    table0 = \
        [
            [16, 11, 10, 16, 24, 40, 51, 61],
            [12, 12, 14, 19, 26, 58, 60, 55],
            [14, 13, 16, 24, 40, 57, 69, 56],
            [14, 17, 22, 29, 51, 87, 80, 62],
            [18, 22, 37, 56, 68, 109, 103, 77],
            [24, 35, 55, 64, 81, 104, 113, 92],
            [49, 64, 78, 87, 103, 121, 120, 101],
            [72, 92, 95, 98, 112, 100, 103, 99]
        ]

    table1 = \
        [
            [17, 18, 24, 47, 99, 99, 99, 99],
            [18, 21, 26, 66, 99, 99, 99, 99],
            [24, 26, 56, 99, 99, 99, 99, 99],
            [47, 66, 99, 99, 99, 99, 99, 99],
            [99, 99, 99, 99, 99, 99, 99, 99],
            [99, 99, 99, 99, 99, 99, 99, 99],
            [99, 99, 99, 99, 99, 99, 99, 99],
            [99, 99, 99, 99, 99, 99, 99, 99]
        ]

    def quanY(self, img):
        temp = [[0 for i in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                temp[i][j] = round(img[i][j] / self.table0[i][j])
        return temp

    def quanUV(self, img):
        temp = [[0 for i in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                temp[i][j] = round(img[i][j] / self.table1[i][j])
        return temp
    
    def reY(self, img):
        temp = [[0 for i in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                temp[i][j] = round(img[i][j] * self.table0[i][j])
        return temp

    def reUV(self, img):
        temp = [[0 for i in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                temp[i][j] = round(img[i][j] * self.table1[i][j])
        return temp

'''
test = Quantization()
DCT = \
    [
        [190.0, 116.0, -62.0, 70.0, -12.0, -1.0, -2.0, 1.0],
        [-63.0, -15.0, 9.0, -1.0, 1.0, 0.0, -1.0, 0.0],
        [-65.0, 8.0, 38.0, -4.0, -0.0, 1.0, 0.0, -0.0],
        [3.0, -2.0, -5.0, -1.0, -1.0, -1.0, 0.0, -0.0],
        [2.0, 2.0, 2.0, 1.0, 1.0, -2.0, 1.0, -1.0],
        [-2.0, 1.0, -3.0, 1.0, 1.0, 1.0, 1.0, -1.0],
        [-2.0, 1.0, -3.0, -2.0, -1.0, -1.0, -1.0, -1.0],
        [-0.0, 2.0, 1.0, 1.0, 0.0, -0.0, 1.0, 1.0]
    ]
output = test.quanY(DCT)
for row in output:
    print(row)
'''