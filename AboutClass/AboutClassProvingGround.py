#放在資料夾下的呼叫特定class
# import NonInstantClassManager,TheA 
#放在資料夾下的呼叫所有class
import InstantClass
from NonInstantClass import NonInstantClassManager

class AboutClassProvingGround:
    @staticmethod
    def aboutClass_exampleInstantClassAndInheritance():
        frankLu = InstantClass.TheFather("Frank",30)
        frankLu.showMyself()

        youngLu = InstantClass.TheSon("Young",40)
        youngLu.showMyself()
    def aboutClass_exampleStaticMethodAndClassMethod():
        NonInstantClassManager.exampleClassMethod()
        NonInstantClassManager.exampleStaticMethod()
    

#
#KILL ZONE 
# 
AboutClassProvingGround.aboutClass_exampleInstantClassAndInheritance()
AboutClassProvingGround.aboutClass_exampleStaticMethodAndClassMethod()
