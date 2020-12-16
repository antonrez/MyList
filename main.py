"""
Нужно написать функцию, которая из списка списков неопределнной глубины сделает одноуровневый список элементов, исключая None.

Примеры входа и выхода
Input: [0, 1, 2]
Output: [0, 1, 2]
Input: [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
Output: [0, 2, 2, 3, 8, 100, 4, 50, -2]
Input: [0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]
Output: [0, 2, 2, 3, 8, 100, -2]
Input: [None, [[[None]]], None, None, [[None, None], None], None]
Output: []
"""
import MyList as ml

l2 = []

l1 = [0, 1, 2]
ml.Mist(l1, l2)
print("Input: {}".format(l1))
print("Output: {}".format(l2))

l2.clear()
l1 = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
ml.Mist(l1, l2)
ml.InputList(l1)
ml.OutputList(l2)

l2.clear()
l1 = [0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]
ml.Mist(l1, l2)
ml.InputList(l1)
ml.OutputList(l2)

l2.clear()
l1 = [None, [[[None]]], None, None, [[None, None], None], None]
ml.Mist(l1, l2)
ml.InputList(l1)
ml.OutputList(l2)
