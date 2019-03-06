class AC:
    def RLC(self, a):
        temp = []
        numof0 = 0
        for num in a:
            if num == 0:
                numof0 += 1
            else:
                temp.append([numof0, num])
                numof0 = 0
        if numof0 != 0:
            temp.append([0, 0])
        return temp

    def RLE(self, a):
        temp = []
        for s in a:
            zero = s[0]
            num = s[1]
            if num == 0:
                for i in range(63 - len(temp)):
                    temp.append(0)
                break
            for i in range(zero):
                temp.append(0)
            temp.append(num)
        return temp

    def Z2Tab(self, a, table):
        arr = self.RLE(a)
        iter = 0
        i = j = 0
        while i < 8 and j < 8:
            if j < 7:
                j = j + 1
            else:
                i = i + 1
            while j >= 0 and i < 8:
                table[i][j] = arr[iter]
                i = i + 1
                j = j - 1
                iter += 1
            i = i - 1
            j = j + 1
            if i < 7:
                i = i + 1
            else:
                j = j + 1
            while j < 8 and i >= 0:
                table[i][j] = arr[iter]
                i = i - 1
                j = j + 1
                iter += 1
            i = i + 1
            j = j - 1

    def ZScan(self, img):
        Z = []
        i = j = 0
        while i < 8 and j < 8:
            if j < 7:
                j = j + 1
            else:
                i = i + 1
            while j >= 0 and i < 8:
                Z.append(img[i][j])
                i = i + 1
                j = j - 1
            i = i - 1
            j = j + 1
            if i < 7:
                i = i + 1
            else:
                j = j + 1
            while j < 8 and i >= 0:
                Z.append(img[i][j])
                i = i - 1
                j = j + 1
            i = i + 1
            j = j - 1
        return Z

'''
test = AC()
a = [11, -5, -5, -1, -6, 4, 1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rlc = test.RLC(a)
rle = test.RLE(rlc)
print(a)
print(rle)
'''
