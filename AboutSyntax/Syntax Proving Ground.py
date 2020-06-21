import commondExample
import AboutOperator
import formula
import Method
import collectionType
#放在資料夾下的呼叫特定class
#但在其他子資料夾要產生__init__.py
#https://blog.csdn.net/zhili8866/article/details/52980924
from AboutClass.NonInstantClass import NonInstantClassManager,TheA 
#放在資料夾下的呼叫所有class

# from aboutClass import *

#commondExample.showCommandExample()
#formula.determineCompoundInterest()
#collectionType.exampleIninListWithRange()

def aboutOperator_exampleMathematics():
        AboutOperator.showOperator() 


class SyntaxProvingGround:
        @staticmethod
        def exampleSet():
        # unordered and unindexed List
                thisset = {"apple", "banana", "cherry"}
                print(thisset)


SyntaxProvingGround.exampleSet() 