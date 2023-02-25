# Python
Lasso/Ridge/Mic/Relief Select n features from M features

Ridge

由于ridge本身是不会做变量选择的，但是考虑到正则的原理，可以通过挑选coef最大的features来作为自变量的选择结果。

整体来讲，不建议用ridge做自变量选择，所以这里的处理逻辑也比较简单，通过Grid Search算法找到最优的正则系数之后，选择该最优系数之下，coef绝对值最大的n个

Lasso

LASSO本身有自变量选择功能，所以这里的问题就转变成，如何选择合适的C，使得lasso刚好选出我们想要的n个自变量。

由于C的取值和选出的自变量个数存在严格的正相关关系，所以这里直接用二分法做优化。

给出一个0-100000的C的初始取值，设定的收敛条件是当lasso选择的自变量个数大于等于n，小于等于n*1.05的范围内时，迭代结束。

同时，给出最大迭代次数，默认100次，如果100次迭代后依然不收敛，将初始的取值区间放大十倍，再次迭代，以此类推。

再次迭代的过程最多会重复10次，其后则默认为无法收敛。

最后，由于最后收敛的位置不一定刚好选择n个自变量（但一定比n大），我们在lasso选择的所有自变量中再选出coef最大的n个，作为最后结果

Mic

python的minepy包直接提供了mic的计算，所以这里的逻辑非常简单，遍历所有feature，计算其和y的mic，取最大的n个

Relief

Relief的选择逻辑和mic一样，计算出每个feature对应的relief统计量之后，取最大的n个。这里的难点在于实现relief统计量的计算，分为三步：

归一化。因为要对feature的距离求和，一开始一定要归一化
求hit和miss。用欧式几何距离作为判断最近邻的标准
求relief统计量。
