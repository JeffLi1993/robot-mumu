# -*- coding: UTF-8 -*-

from sklearn import svm

# 支持向量机 SVM 算法

x = [[2, 0], [1, 1], [2, 3]]
y = [0, 0, 1]

clf = svm.SVC(kernel='linear')
clf.fit(x, y)
# Fit the SVM model according to the given training data.
#
# Parameters
# ----------
# X : {array-like, sparse matrix}, shape (n_samples, n_features)
#     Training vectors, where n_samples is the number of samples
#     and n_features is the number of features.
#     For kernel="precomputed", the expected shape of X is
#     (n_samples, n_samples).
#
# y : array-like, shape (n_samples,)
#     Target values (class labels in classification, real numbers in
#     regression)

print clf

# 支持向量
print clf.support_vectors_

# 支持向量的下标
print clf.support_

# 支持向量的个数
print clf.n_support_

# 预测某个数是否在
print clf.predict([2, 0])
