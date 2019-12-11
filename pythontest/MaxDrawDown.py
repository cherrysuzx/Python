
import numpy as np
# import matplotlib.pyplot as plt

def maxdrawdown(return_list):
    '''最大回撤率'''
    i = np.argmax((np.maximum.accumulate(return_list) - return_list) / np.maximum.accumulate(return_list))  # 结束位置
    if i == 0:
        return 0
    j = np.argmax(return_list[:i])  # 开始位置
    return (return_list[j] - return_list[i]) / (return_list[j])


return_list=[12,12,21,15,27,16,21,22,25,20,16,17]
print(maxdrawdown(return_list))
