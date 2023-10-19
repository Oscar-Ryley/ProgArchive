#2021 -GCSE

def bubblesort(elist):
  listlen = len(elist)
  for i in range(0, listlen - 1):
    for j in range(listlen - i - 1):
      if elist[j] > elist[j + 1]:
        t = elist[j]
        elist[j] = elist[j + 1]
        elist[j + 1] = t


examplelist = [5, 3, 8, 6, 7, 1, 4, 2, 0, 9, 10, 15, 11, 13, 14]

bubblesort(examplelist)
print(examplelist)
