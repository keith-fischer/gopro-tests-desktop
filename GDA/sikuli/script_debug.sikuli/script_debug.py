


def cleartxfield(regionclick,macwin="mac",fldvalidate="Title.png"):
    rc=True
    if not regionclick:
        print "regionclick is invalid"
        return rc
    
    if macwin=="mac":
        regionclick.click()
        regionclick.keyDown(Key.CMD)
        regionclick.type("a")
        regionclick.keyUp(Key.CMD)
        regionclick.type(Key.BACKSPACE)
    elif macwin=="win":
        regionclick.click()
        regionclick.keyDown(Key.CTRL)
        regionclick.type("a")
        regionclick.keyUp(Key.CTRL)
        regionclick.type(Key.BACKSPACE)
    else:
        print "macwin is invalid"
        return rc
    if regionclick.exists(fldvalidate):
        rc=True
    return rc
        

r0=find("NAMEYOURNEWVIDEO.png")
r1=r0.below(500)

r2=r1.find("ZZZZ.png")
print cleartxfield(r2)