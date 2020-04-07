# https://www.jianshu.com/p/2abe38044446
# pip install PyMuPDF
# 将本目录下所有PDF文件转为png文件（第8行）

import fitz
import sys
import glob
pdffile=glob.glob("*.pdf")
pngfile = []
for f in pdffile:
    pngfile.append(f.rstrip("pdf"))
for i in range(len(pdffile)):
    doc = fitz.open(pdffile[i])
    page = doc[0]
    zoom = int(100)
    rotate = int(0)
    trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
    pm = page.getPixmap(matrix=trans, alpha=False)
    pm.writePNG(pngfile[i] + "png")