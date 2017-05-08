

class utils():
    def test(self):
        print
def intToTimeFormat(secs):
    n1=secs%60
    n2=secs/60
    return "%02d:%02d" % (n2,n1)

for i in range(121):
    n=i%60
    n1=i/60
    print "%d - %02d:%02d" % (i,n1,n)


