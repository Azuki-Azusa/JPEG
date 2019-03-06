import cv2
import RGB2YUV
import DCT

class DC:
    def DPCM(self, blocks):
        temp = []
        temp.append(blocks[0][0][0])
        for i in range(1, len(blocks)):
            temp.append(blocks[i][0][0] - blocks[i-1][0][0])
        return temp

    def DPCM2(self, arr):
        blocks = []
        for i in range(len(arr)):
            temp = [[0 for i in range(8)] for i in range(8)]
            if i == 0:
                temp[0][0] = arr[0]
            else:
                temp[0][0] = arr[i] + blocks[i-1][0][0]
            blocks.append(temp)
        return blocks

'''
test = DCT.DCT()
img = cv2.imread("../photograph.jpg")
Y, U, V = RGB2YUV.rgb2yuv(img, img.shape[1], img.shape[0])
Y = test.fill(Y)
blocks = test.split(Y)
for block in blocks:
    print(block[0][0], end=' ')
print('')
test = DC()
a = test.DPCM(blocks)
print(a)
blocks = test.DPCM2(a)
for block in blocks:
    print(block[0][0], end=' ')
    '''
