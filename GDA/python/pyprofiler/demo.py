
import cProfile
import random
def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]
# lIn = [random.random() for i in range(1000000)]
# cProfile.run('f1(lIn)')
# cProfile.run('f2(lIn)')
# cProfile.run('f3(lIn)')
####################################################
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

# f(2)
# f(3,[3,2,1])
# f(3)
####################################################
class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

# a = A()
# b = B()
# c = C()
# d = D()
# e = E()
#
#
# # specify output from here onwards
#
# a.go()
# b.go()
# c.go()
# d.go()
# e.go()
#
# a.stop()
# b.stop()
# c.stop()
# d.stop()
# e.stop()
#
# a.pause()
# b.pause()
# c.pause()
# d.pause()
# e.pause()

####################################################


def f(*args,**kwargs): print(args, kwargs)

# l = [1,2,3]
# t = (4,5,6)
# d = {'a':7,'b':8,'c':9}
#
# f()
# f(1,2,3)                    # (1, 2, 3) {}
# f(1,2,3,"groovy")           # (1, 2, 3, 'groovy') {}
# f(a=1,b=2,c=3)              # () {'a': 1, 'c': 3, 'b': 2}
# f(a=1,b=2,c=3,zzz="hi")     # () {'a': 1, 'c': 3, 'b': 2, 'zzz': 'hi'}
# f(1,2,3,a=1,b=2,c=3)        # (1, 2, 3) {'a': 1, 'c': 3, 'b': 2}
#
# f(*l,**d)                   # (1, 2, 3) {'a': 7, 'c': 9, 'b': 8}
# f(*t,**d)                   # (4, 5, 6) {'a': 7, 'c': 9, 'b': 8}
# f(1,2,*t)                   # (1, 2, 4, 5, 6) {}
# f(q="winning",**d)          # () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
# f(1,2,*t,q="winning",**d)   # (1, 2, 4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
#
# def f2(arg1,arg2,*args,**kwargs): print(arg1,arg2, args, kwargs)
#
# f2(1,2,3)                       # 1 2 (3,) {}
# f2(1,2,3,"groovy")              # 1 2 (3, 'groovy') {}
# f2(arg1=1,arg2=2,c=3)           # 1 2 () {'c': 3}
# f2(arg1=1,arg2=2,c=3,zzz="hi")  # 1 2 () {'c': 3, 'zzz': 'hi'}
# f2(1,2,3,a=1,b=2,c=3)           # 1 2 (3,) {'a': 1, 'c': 3, 'b': 2}
#
# f2(*l,**d)                   # 1 2 (3,) {'a': 7, 'c': 9, 'b': 8}
# f2(*t,**d)                   # 4 5 (6,) {'a': 7, 'c': 9, 'b': 8}
# f2(1,2,*t)                   # 1 2 (4, 5, 6) {}
# f2(1,1,q="winning",**d)      # 1 1 () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
# f2(1,2,*t,q="winning",**d)   # 1 2 (4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}

####################################################

class Node(object):
    def __init__(self,sName):
        self._lChildren = []
        self.sName = sName
    def __repr__(self):
        return "<Node '{}'>".format(self.sName)
    def append(self,*args,**kwargs):
        self._lChildren.append(*args,**kwargs)
    def print_all_1(self):
        print(self)
        for oChild in self._lChildren:
            oChild.print_all_1()
    def print_all_2(self):
        def gen(o):
            lAll = [o,]
            while lAll:
                oNext = lAll.pop(0)
                lAll.extend(oNext._lChildren)
                yield oNext
        for oNode in gen(self):
            print(oNode)

# oRoot = Node("root")
# oChild1 = Node("child1")
# oChild2 = Node("child2")
# oChild3 = Node("child3")
# oChild4 = Node("child4")
# oChild5 = Node("child5")
# oChild6 = Node("child6")
# oChild7 = Node("child7")
# oChild8 = Node("child8")
# oChild9 = Node("child9")
# oChild10 = Node("child10")
#
# oRoot.append(oChild1)
# oRoot.append(oChild2)
# oRoot.append(oChild3)
# oChild1.append(oChild4)
# oChild1.append(oChild5)
# oChild2.append(oChild6)
# oChild4.append(oChild7)
# oChild3.append(oChild8)
# oChild3.append(oChild9)
# oChild6.append(oChild10)
#
#
# # specify output from here onwards
#
# oRoot.print_all_1()
# oRoot.print_all_2()

####################################################

def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


print_directory_contents("/Users/keithfisher/Desktop/iosAutomation")




####################################################