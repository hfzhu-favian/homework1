import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("cat,png.jpg")
if img is None:
    print("错误：无法读取图片，请检查路径/文件名是否正确！")
    exit()


height, width, channels = img.shape
dtype = img.dtype
print(f"图像尺寸：{width} × {height}")
print(f"通道数：{channels}")
print(f"像素数据类型：{dtype}")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure("Original Image (Matplotlib)")
plt.imshow(img_rgb)
plt.axis("off")
# 可选：注释掉plt.show()避免弹窗，只保留文件保存
# plt.show()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray_test.jpg", gray_img)
print("✅ 灰度图已保存为 gray_test.jpg")


if channels == 3:
    pixel_val = img[100, 100]
    print(f"像素 (100,100) 的 BGR 值：{pixel_val}")
else:
    pixel_val = gray_img[100, 100]
    print(f"像素 (100,100) 的灰度值：{pixel_val}")


if height >= 200 and width >= 200:
    crop_img = img[0:200, 0:200]
    cv2.imwrite("crop_test.jpg", crop_img)
    print("✅ 裁剪区域已保存为 crop_test.jpg")
else:
    print("⚠️ 图片尺寸小于200×200，跳过裁剪保存")

plt.close('all')
print("\n🎉 所有核心任务执行完成！")
