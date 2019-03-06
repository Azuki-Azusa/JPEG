import numpy as np
import cv2

#img = cv2.imread("../photograph.jpg")

'''
print(img.shape[0], img.shape[1])
print(len(img), len(img[0]))
'''


def rgb2yuv(img, width, height):
    Y = [[0 for i in range(width)] for i in range(height)]
    U = [[0 for i in range((width - 1) // 2 + 1)] for i in range((height - 1) // 2 + 1)]
    V = [[0 for i in range((width - 1) // 2 + 1)] for i in range((height - 1) // 2 + 1)]
    for i in range(height):
        flag = False
        if i % 2 == 1 or i == height - 1:
            flag = True
        for j in range(width):
            B = img[i][j][0]
            G = img[i][j][1]
            R = img[i][j][2]
            Y[i][j] = (0.299 * R + 0.587 * G + 0.144 * B - 128)
            if i % 2 == 0 and j % 2 == 0:
                U[i // 2][j // 2] = (-0.168736 * R + (-0.331264) * G + 0.5 * B) + 128
            if flag:
                V[i // 2][j // 2] = (0.5 * R + (-0.418688) * G + (-0.081312) * B) + 128
    return Y, U, V


def yuv2rgb(Y, U, V, width, height):
    img = np.zeros([height, width, 3], dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            img[i][j][0] = (Y[i][j] + 128) + 1.1772 * (U[i//2][j//2] - 128)
            img[i][j][1] = (Y[i][j] + 128) + (-0.34414) * (U[i//2][j//2] - 128) + (-0.71414) * (V[i//2][j//2] - 128)
            img[i][j][2] = (Y[i][j] + 128) + 1.402 * (V[i//2][j//2] - 128)
    return img


'''
Y, U, V = rgb2yuv(img, img.shape[1], img.shape[0])
imgY = np.zeros([img.shape[0], img.shape[1], 1], dtype=np.uint8)
imgU = np.zeros([img.shape[0] // 2, img.shape[1] // 2, 1], dtype=np.uint8)
imgV = np.zeros([img.shape[0] // 2, img.shape[1] // 2, 1], dtype=np.uint8)
for i in range(682):
    for j in range(1024):
        imgY[i][j][0] = Y[i][j]
for i in range(341):
    for j in range(512):
        imgU[i][j][0] = U[i][j]
for i in range(341):
    for j in range(512):
        imgV[i][j][0] = V[i][j]
cv2.imshow("created_imgY", imgY)
cv2.imshow("created_imgU", imgU)
cv2.imshow("created_imgV", imgV)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
img = cv2.imread("../photograph.jpg")
Y, U, V = rgb2yuv(img, img.shape[1], img.shape[0])
img = yuv2rgb(Y, U, V, img.shape[1], img.shape[0])
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
