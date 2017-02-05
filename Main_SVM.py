import numpy as np
from sklearn import svm

neg_pval = np.loadtxt('GDM_neg_pval.csv', delimiter=",")
pos_pval = np.loadtxt('GDM_pos_pval.csv', delimiter=",")
pos_detec = np.loadtxt('GDM_pos_detec.csv', delimiter = ",")
neg_detec = np.loadtxt('GDM_neg_detec.csv', delimiter = ",")

new_neg_pval = 1 - neg_pval
new_pos_pval = 1 - pos_pval
norm_pos = pos_detec * new_pos_pval
norm_neg = neg_detec * new_neg_pval