import cv2
import numpy as np

import streamlit as st
import os
import streamlit.components.v1 as com

import mazevector as vec

os.chdir(os.getcwd())

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    
    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
    ], dtype="float32")
    
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    
    return warped
st.set_page_config(page_title='MAZERUNNER', page_icon = 'https://free.clipartof.com/2142-Free-Clipart-Of-A-Maze.jpg')
st.markdown(
     f"""
     <style>
     .stApp {{
         background: url('https://i.postimg.cc/LsRVH6L5/3418448.jpg');
         background-size: cover
     }}
     </style>
     """,
     unsafe_allow_html=True
 )
#com.iframe('https://lottie.host/?file=cb4ab332-b345-4eab-b2c2-3b7f6548fb8f/UwN8mO3Dyv.json')
com.iframe('https://lottie.host/?file=83d95322-fdbb-4ded-8ff9-d36207e5b5d1/irmPc70uvB.json')
st.image('https://i.postimg.cc/GmmXDMs2/2-removebg-preview.png', width = 400)

#st.info("MEMBERS:\n 1.SHARVIN \n 2.ISHAAN")

pic=st.file_uploader("Upload your image here")
sp = st.text_input('Start Position')
ep = st.text_input('End Position')
if pic and sp and ep:
    sp = eval(sp)
    ep = eval(ep)
    st.success("IMAGE HAS BEEN UPLOADED SUCCESSFULLY.")
#image = cv2.resize(image, (500, 500))
    image = cv2.imdecode(np.frombuffer(pic.read(), np.uint8), cv2.IMREAD_COLOR)
    h,w,d = image.shape
    aspect_ratio = w/h
    nw = 900
    nh = int(500//aspect_ratio)
    st.write(nw,nh)
    image = cv2.resize(image, (nw, nh))
    cv2.imwrite('Image.jpg', image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
    
    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        
        if len(approx) == 4:
            docCnt = approx
            break
        
    warped = four_point_transform(image, docCnt.reshape(4, 2))
    warped = cv2.resize(warped, (31, 31))
    warp_gr = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    matrix = []
    for x in warp_gr:
        row = []
        for y in x:
            if y>=80:
                row.append(0)
            else:
                row.append(1)
        matrix.append(row)
        
    nmatrix = []
    for i in range(0,len(matrix),3):
        mat =[]
        for j in range(0,len(matrix),3):
            mat.append(matrix[i][j])
        nmatrix.append(mat)    
        
    
    for x in nmatrix :
        st.success(str(x))
    st.success(vec.SolveMaze(nmatrix, sp, ep))