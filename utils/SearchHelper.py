import h5py
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from model.VGGModel import VGGNet


def search(querypath, h5name, databasepath="data/data"):
    # 要搜的原图path，h5文件的name，原数据集的path
    query = querypath
    index = h5name
    result = databasepath
    h5f = h5py.File(index, 'r')
    feats = h5f['dataset_1'][:]
    imgNames = h5f['dataset_2'][:]
    h5f.close()

    print("--------------------------------------------------")
    print("               searching starts                   ")
    print("--------------------------------------------------")

    # read  query image
    queryImg = mpimg.imread(query)
    # 初始化 VGGNet16 模块
    model = VGGNet()
    #提取query图片的特征
    queryVec = model.vgg_extract_feat(query)
    print('--------------------------')
    print('--------------------------')
    scores = np.dot(queryVec, feats.T)
    print(scores)
    rank_ID = np.argsort(scores)[::-1]
    print(rank_ID)
    rank_score = scores[rank_ID]
    print(rank_score)

    # 检索出5张相似度最高的图片
    maxres = 5
    imlist = []
    # 输出相似度
    for i, index in enumerate(rank_ID[0:maxres]):
        imlist.append(imgNames[index])
        print("image names: " +
              str(imgNames[index]) +
              " scores: %f"
              % rank_score[i])
    print("top %d images in order are: " % maxres, imlist)
    # 输出前5张
    for i, im in enumerate(imlist):
        image = mpimg.imread(result + "/" + str(im, 'utf-8'))
        plt.title("Result of research %d" % (i + 1))
        plt.imshow(image)
        plt.show()
