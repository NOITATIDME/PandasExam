import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import sep


# 도미
bream_length = pd.read_csv(
    'C:/workspace/pythonwork/fish/bream_length.csv', sep=",").to_numpy().flatten()
bream_weight = pd.read_csv(
    'C:/workspace/pythonwork/fish/bream_weight.csv', sep=",").to_numpy().flatten()

# 빙어
smelt_length = pd.read_csv(
    'C:/workspace/pythonwork/fish/smelt_length.csv', sep=",").to_numpy().flatten()
smelt_weight = pd.read_csv(
    'C:/workspace/pythonwork/fish/smelt_weight.csv', sep=",").to_numpy().flatten()

# print(bream_length)
# print(bream_weight)
# print(smelt_length)
# print(smelt_weight)

bream_length = np.array(bream_length)
bream_weight = np.array(bream_weight)

smelt_length = np.array(smelt_length)
smelt_weight = np.array(smelt_weight)

bream_data = np.column_stack((bream_length, bream_weight))
smelt_data = np.column_stack((smelt_length, smelt_weight))

# print(bream_data.shape)
# print(smelt_data.shape)

#plt.scatter(bream_data[:, 0], bream_data[:, 1])
#plt.scatter(smelt_data[:, 0], smelt_data[:, 1])
# plt.xlabel("length")
# plt.ylabel("weight")
# plt.show()

fish_data = np.concatenate((bream_data, smelt_data))
# print(fish_data)
fish_target = np.concatenate((np.ones(34), np.zeros(13)))
fish_target = fish_target.reshape((-1, 1))

fishes = np.hstack((fish_data, fish_target))
# print(fishes)

fish_dataFrame = pd.DataFrame(
    fishes, columns=["fish_len", "fish_wei", "target"])
# print(fish_dataFrame)

index = np.arange(47)  # 34(도미), 13(빙어)
np.random.shuffle(index)
# print(index)

train_input = fish_data[index[:34]]  # 훈련 데이터 (모델)
train_target = fish_target[index[:34]]  # 타겟 데이터 (모델)

train = np.column_stack((train_input, train_target))

test_input = fish_data[index[34:]]  # 훈련 데이터 (검증)
test_target = fish_target[index[34:]]  # 타겟 데이터 (검증)

test = np.column_stack((test_input, test_target))


# plt.scatter(train_input[:, 0], train_input[:, 1])  # 훈련
# plt.scatter(test_input[:, 0], test_input[:, 1])  # 검증
# plt.xlabel("length")
# plt.ylabel("weight")
# plt.show()

def gettrainData():

    train_dataFrame = pd.DataFrame(
        train, columns=["train_target", "train_length", "train_weight"])

    return train_dataFrame


def gettestData():
    test_dataFrame = pd.DataFrame(
        test, columns=["test_target", "test_length", "test_weight"])

    return test_dataFrame
