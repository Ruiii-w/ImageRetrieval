import h5py
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sys
import os
import numpy as np
# from model.VGGModel import VGGNet
import keras.models
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input as preprocess_input_vgg
from keras.preprocessing import image
from numpy import linalg as LA


class VGGNet:
    def __init__(self):
        self.input_shape = (224, 224, 3)
        self.model_vgg = keras.models.load_model('m1.h5', compile=False)

    # 提取vgg16最后一层卷积特征
    def vgg_extract_feat(self, img_path):
        img = image.load_img(img_path,
                             target_size=(self.input_shape[0],
                                          self.input_shape[1]))  # 加载图片
        img = image.img_to_array(img)  # 转换为数组
        img = np.expand_dims(img, axis=0)  # 转换为np数组
        img = preprocess_input_vgg(img)  # 进行VGG处理
        feat = self.model_vgg.predict(img)  # 提取特征
        norm_feat = feat[0] / LA.norm(feat[0])  # 求归一化特征向量
        return norm_feat


def readname():
    filePath = sys.argv[1]
    name = os.listdir(filePath)
    return name


def search(querypath):
    # 要搜的原图path，h5文件的name，原数据集的path
    query = querypath

    # read  query image
    # queryImg = mpimg.imread(query)
    # 初始化 VGGNet16 模块
    model = VGGNet()

    # 提取query图片的特征
    queryVec = model.vgg_extract_feat(query)

    scores = np.dot(queryVec, feats.T)
    rank_ID = np.argsort(scores)[::-1]
    rank_score = scores[rank_ID]
    print("Scores: ")
    print(rank_score)

    # 检索出5张相似度最高的图片
    maxres = 5
    imlist = []
    # 输出相似度
    for i, index in enumerate(rank_ID[0:maxres]):
        imlist.append(imgNames[index])
        print("Result image name: " +
              str(imgNames[index]) +
              " scores: %f"
              % rank_score[i])
    print("top %d images in order are: " % maxres, imlist)


if __name__ == '__main__':
    database = "database/result.h5"

    h5f = h5py.File(database, 'r')
    feats = h5f['dataset_1'][:]
    imgNames = h5f['dataset_2'][:]
    h5f.close()

    # cnt = 0
    name = readname()
    for i in name:
        print('--------------------------')
        print("Searching image: " + i)
        print('--------------------------')
        i = sys.argv[1] + "/" + i
        search(i)
        # cnt = cnt + 1
        # print(cnt)
