from sikuli import *
#import org.sikuli.script.ImagePath

def Do_relay():
    doubleClick(Pattern("USB_data_off.png").targetOffset(223,0))
    
    doubleClick(Pattern("PowerCycle_On.png").targetOffset(217,8))
    

    wait("HERO4Silver.png",30)
    
    find("C313D123400l.png")
    
    
    doubleClick("IMPORTNOW.png")
    
    wait("CANCELIMPORT.png",30)
    
    doubleClick("CANCELIMPORT.png")
    
    wait("IMPORTNOW.png",30)
    
    doubleClick(Pattern("USBData_ON.png").targetOffset(318,0))
    
    doubleClick(Pattern("PowerCycle_On-1.png").targetOffset(320,4))
    

    wait("MEDIATYPESAL.png",30)
    

    
do_relay()
do_relay()
do_relay()
do_relay()
do_relay()
do_relay()
do_relay()
do_relay()
do_relay()
