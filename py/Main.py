import RGB2YUV
import DCT
import Quantization
import AC
import DC
import Compress
import cv2

def printBlock(block):
    for row in block:
        print(row)


DCT = DCT.DCT()
Quantization = Quantization.Quantization()
AC = AC.AC()
DC = DC.DC()
Compress = Compress.Compress()

def compress(path):
    img = cv2.imread(path)
    height = img.shape[0]
    width = img.shape[1]
    Y, U, V = RGB2YUV.rgb2yuv(img, img.shape[1], img.shape[0])
    Y = DCT.fill(Y)
    U = DCT.fill(U)
    V = DCT.fill(V)
    blocksY = DCT.split(Y)
    blocksU = DCT.split(U)
    blocksV = DCT.split(V)
    FDCT = []
    Quan = []
    Z = []
    ACnum = []
    for block in blocksY:
        FDCT.append(DCT.FDCT(block))
        Quan.append(Quantization.quanY(FDCT[-1]))
        Z.append(AC.ZScan(Quan[-1]))
        ACnum.append(AC.RLC(Z[-1]))
    DCnum = DC.DPCM(Quan)
    #print('Y: ')
    Bstr0 = ''
    for i in range(len(ACnum)):
        Bstr0 += Compress.AllCompressY(DCnum[i], ACnum[i])
    #print(Bstr0)
    #print(len(Bstr0))

    FDCT = []
    Quan = []
    Z = []
    ACnum = []
    for block in blocksU:
        FDCT.append(DCT.FDCT(block))
        Quan.append(Quantization.quanUV(FDCT[-1]))
        Z.append(AC.ZScan(Quan[-1]))
        ACnum.append(AC.RLC(Z[-1]))
    DCnum = DC.DPCM(Quan)
    #print('U: ')
    Bstr1 = ''
    for i in range(len(ACnum)):
        Bstr1 += Compress.AllCompressUV(DCnum[i], ACnum[i])
    #print(Bstr1)
    #print(len(Bstr1))

    FDCT = []
    Quan = []
    Z = []
    ACnum = []
    for block in blocksV:
        FDCT.append(DCT.FDCT(block))
        Quan.append(Quantization.quanUV(FDCT[-1]))
        Z.append(AC.ZScan(Quan[-1]))
        ACnum.append(AC.RLC(Z[-1]))
    DCnum = DC.DPCM(Quan)
    #print('V: ')
    Bstr2 = ''
    for i in range(len(ACnum)):
        Bstr2 += Compress.AllCompressUV(DCnum[i], ACnum[i])
    #print(Bstr2)
    #print(len(Bstr2))
    s = Bstr0 + Bstr1 + Bstr2
    print(len(s))

    return height, width, s

def encoding(bs, width, heigth):
    DCY, DCU, DCV, ACY, ACU, ACV = Compress.encoding(bs, height, width)
    YBlocks = DC.DPCM2(DCY)
    UBlocks = DC.DPCM2(DCU)
    VBlocks = DC.DPCM2(DCV)
    for i in range(len(YBlocks)):
        AC.Z2Tab(ACY[i], YBlocks[i])
        YBlocks[i] = Quantization.reY(YBlocks[i])
        YBlocks[i] = DCT.IDCT(YBlocks[i])
    for i in range(len(UBlocks)):
        AC.Z2Tab(ACU[i], UBlocks[i])
        UBlocks[i] = Quantization.reUV(UBlocks[i])
        UBlocks[i] = DCT.IDCT(UBlocks[i])
    for i in range(len(VBlocks)):
        AC.Z2Tab(ACV[i], VBlocks[i])
        VBlocks[i] = Quantization.reUV(VBlocks[i])
        VBlocks[i] = DCT.IDCT(VBlocks[i])

    Y, U, V = DCT.merge(YBlocks, UBlocks, VBlocks, height, width)
    img = RGB2YUV.yuv2rgb(Y, U, V, width, height)
    cv2.imwrite(r'../photograph_JPEG.jpeg', img)
    cv2.imshow("img after encoding", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

height, width, s = compress(r"../photograph.jpg")
print(height, width)
f = open(r'../txt.txt', 'w', encoding='utf-8')
f.write(s)
f.close()



f = open(r'../txt.txt', 'r', encoding='utf-8')
s = f.read()
encoding(s, width, height)
f.close()
