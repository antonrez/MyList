
def Mist(l1, l2):
    for sub in l1:
        if type(sub) == list:
            Mist(sub, l2)
        elif sub == None:
            break
        else:
            l2.append(sub)

def InputList (l1):
    print("Input: {}".format(l1))

def OutputList (l1):
    print("Output: {}".format(l1))
