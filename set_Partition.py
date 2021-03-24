import os
import random
import torch
import numpy as np

label_path = 'data/annotations_image'
dataSetDir = 'data'
train_image_filename = 'train_image.txt'
train_label_filename = 'train_label.txt'
test_image_filename = 'test_image.txt'
test_label_filename = 'test_label.txt'

all_sample_sum = 19000
test_sample_sum = 1000  # 测试集样本数
random_list = []  # 随机序列 （测试集）

labels = []  # 所有image的label信息
image_label = ""  # 每一个image的label信息
train_image_labels = []  # 训练集image的label信息
test_image_labels = []  # 测试集image的label信息


def load_file(filename, DATA_DIR):
    label_filepath = os.path.join(DATA_DIR, filename)
    # print(label_filepath)
    label = np.loadtxt(label_filepath, dtype=np.int64)
    return label


def PartitionWithLabels():
    """
        对数据集进行划分 并为划分好的数据集打上label
        :return:None
    """
    random_list = random.sample(range(1, all_sample_sum + 1), test_sample_sum)

    train_data_file = os.path.join(dataSetDir, train_image_filename)
    train_label_file = os.path.join(dataSetDir, train_label_filename)
    test_data_file = os.path.join(dataSetDir, test_image_filename)
    test_label_file = os.path.join(dataSetDir, test_label_filename)

    label_files = os.listdir(label_path)  # label文件

    for file in label_files:
        label = load_file(file, label_path)
        labels.append(label)

    train_data_fp = open(train_data_file, 'w')
    train_label_fp = open(train_label_file, 'w')
    test_data_fp = open(test_data_file, 'w')
    test_label_fp = open(test_label_file, 'w')

    train_data = []
    test_data = []
    for i in range(1, all_sample_sum + 1):
        print(i)
        image_label = ""
        if i not in random_list:
            # train_data_fp.write('im{}.jpg\n'.format(i))
            train_data.append('data/im{}.jpg\n'.format(i))
            for label in labels:
                if i in label:
                    image_label += '1'
                else:
                    image_label += '0'
                image_label += ' '
            image_label += '\n'
            train_image_labels.append(image_label)
        else:
            test_data.append('data/im{}.jpg\n'.format(i))
            # test_data_fp.write('im{}.jpg\n'.format(i))
            for label in labels:
                if i in label:
                    image_label += '1'
                else:
                    image_label += '0'
                image_label += ' '
            image_label += '\n'
            test_image_labels.append(image_label)

    for i in range(len(train_data)):
        train_data_fp.write(train_data[i])
        train_label_fp.write(train_image_labels[i])

    for i in range(len(test_data)):
        test_data_fp.write(test_data[i])
        test_label_fp.write(test_image_labels[i])

    # with open(train_data_file, 'w', encoding= 'utf-8') as trf:
    #     for i in range(1, all_sample_sum + 1):
    #         if i not in random_list:
    #             trf.write('im{}.jpg\n'.format(i))
    #
    # with open(test_data_file, 'w', encoding='utf-8') as tsf:
    #     for i in random_list:
    #         tsf.write('im{}.jpg\n'.format(i))

    train_data_fp.close()
    train_label_fp.close()
    test_data_fp.close()
    test_label_fp.close()


if __name__ == '__main__':
    PartitionWithLabels()
