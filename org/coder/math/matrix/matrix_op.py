# -*- coding: utf-8 -*-

# 导入 numpy 函数，以 np 开头
import numpy as np

if __name__ == '__main__':
    mat1 = np.array([1, 3])
    mat1 = np.mat(mat1)  # mat 函数将目标数据的类型转换为矩阵（matrix）
    print mat1
    # 1 行 2 列的矩阵（也称 1 * 2 矩阵）
    # ==> [[1 3]]

    print ''

    mat2 = np.array([[1, 3], [3, 4]])
    mat2 = np.mat(mat2)
    print mat2
    # 2 * 2 矩阵
    # ==> [[1 3]
    # ==>  [3 4]]

    # 获取矩阵的大小
    print mat1.shape
    print mat2.shape
