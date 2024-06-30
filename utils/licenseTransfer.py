'''
Descripttion: 
Author: sora
Date: 2024-05-15 14:03:22
LastEditors: sora
LastEditTime: 2024-06-14 17:39:26
'''
import cv2
import numpy as np

def licenseTransfer(img):

    # 定义红色的范围
    lower_red = np.array([0, 0, 150])
    upper_red = np.array([150, 150, 255])

    # 创建一个掩码，将红色部分变为白色
    mask = cv2.inRange(img, lower_red, upper_red)

    # 将红色部分变为白色
    img[mask > 0] = [255, 255, 255]

    # 显示处理后的图片
    # cv2.imshow('Image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    ##########开始增强黑色字体##########

    # 将图像转换为灰度图
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 对灰度图进行阈值处理
    _, threshold_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # 定义一个核用于膨胀操作
    kernel = np.ones((3,3),np.uint8)

    # 对二值化图像进行膨胀操作
    dilated_threshold_img = cv2.dilate(threshold_img, kernel, iterations=1)

    # 将膨胀后的图像叠加到原始图像上，保留黑色文字的轮廓
    enhanced_img = cv2.bitwise_and(img, img, mask=dilated_threshold_img)

    # 显示增强后的图片
    # cv2.imshow('Enhanced Image', enhanced_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # cv2.imwrite("Enhanced Image.png", enhanced_img)
    return enhanced_img