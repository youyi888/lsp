from PIL import Image
import time
import numpy as np
import os
t2 = time.time()
# import torch

# CCM = np.array( [[1.499, -0.567, 0.068],
#                 [-0.427, 1.499, -0.071],
#                 [-0.138, -0.36, 1.5000]],dtype=np.double)
# # 打开原始图片并将其转换为RGB模式
# # 要遍历的文件夹路径
# folder_path = '//jingzhu/exam/145fa7b7683c4ff8ba1463599fd4debd'

# # 遍历文件夹中的所有文件
# for dirpath, dirnames, filenames in os.walk(folder_path):
#     # 对于每个文件名
#     for filename in filenames:
#         t1 = time.time()
#         file_path = os.path.join(dirpath, filename)
#         print(filename)
#         if  filename.endswith('.jpg'):
#         # 打开图片
#             im = Image.open(file_path).convert('RGB')
#             # im = Image.open(f'C:/Users/Administrator/Contacts/Desktop/isp/images/{str(x).zfill(3)}.jpg')
#             # height=3648
#             # width=5472
#             width = im.width       #图片的宽
#             height = im.height      #图片的高
#             im = np.array(im,dtype=np.double)
#             print(time.time() - t1)
#             # 将 numpy 矩阵转换为 PyTorch 张量
#             a_tensor = torch.from_numpy(im.reshape(-1, 3))
#             b_tensor = torch.from_numpy(CCM.T)

#             # 计算两个 PyTorch 张量相乘
#             c_tensor = torch.matmul(a_tensor, b_tensor)
#             print(time.time() - t1)
#             im = c_tensor.numpy().reshape(height, width, 3).clip(min=0, max=255).astype(np.uint8)
#             im = Image.fromarray(np.uint8(im))
#             print(time.time() - t1)
#             im.save(file_path)

# print(time.time() - t2)



def ccm_convert():
    # CCM = np.array( [[1.499, -0.567, 0.068],
    #                 [-0.427, 1.499, -0.071],
    #                 [-0.138, -0.36, 1.5000]],dtype=np.double)
    CCM = np.array( [[0.98, 0.73, -0.69], [-0.48, 1.89, -0.38], [0.12, -0.83, 1.71]],dtype=np.double)

    # CCM[0][0] *= 1.50
    # CCM[0][1] *= 0.70
    # CCM[0][2] *= 0.90
    # CCM[1][0] *= 1.50
    # CCM[1][1] *= 1.10
    # CCM[1][2] *= 0.90
    # CCM[2][0] -= 0.15
    # CCM[2][1] *= 0.74
    # CCM[2][2] *= 0.96

    # CCM[0][1] -= 0.07
    # CCM[1][0] += 0.15
    # CCM *= 0.90
    


    CCM[0][0] *= 1.118
    CCM[0][1] *= 1.02
    CCM[0][2] *= 0.90
    CCM[2][0] *= 1.05
    CCM[2][1] *= 0.74
    CCM[2][2] *= 0.97
    
    CCM[0][1] -= 0.07
    CCM[1][1] *= 0.995
    CCM[1][0] += 0.15
    CCM *= 0.85
    t1 = time.time()
    print(CCM)
    # folder_path = 'E:/yangxing/新建文件夹/'

    # # 遍历文件夹中的所有文件
    # for dirpath, dirnames, filenames in os.walk(folder_path):
    #     # 对于每个文件名
    #     for filename in filenames:
    #         t1 = time.time()
    #         file_path = os.path.join(dirpath, filename)
    #         if  filename.endswith('.png'):
                # 打开原始图片并将其转换为RGB模式
                # 要遍历的文件夹路径
    im = Image.open('C:/Users/Administrator/Contacts/Desktop/isp/20x_0.75.raw.png').convert('RGB')
    # im = Image.open(f'C:/Users/Administrator/Contacts/Desktop/isp/images/{str(x).zfill(3)}.jpg')
    # height=3648
    # width=5472
    width = im.width       #图片的宽
    height = im.height      #图片的高
    im = np.array(im,dtype=np.double)
    output_img = np.dot(im.reshape(-1, 3), CCM.T)
    print(time.time() - t1)
    output_img = output_img.reshape(height, width, 3).clip(min=0, max=255).astype(np.uint8)
    print(time.time() - t1)
    im = Image.fromarray(np.uint8(output_img))
    print(time.time() - t1)
    im.show()
    #im.save('C:/Users/Administrator/Contacts/Desktop/isp/20x_0.75-ccm.raw.png')
ccm_convert()
print(time.time() - t2)