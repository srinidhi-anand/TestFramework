from msilib.schema import Class
import operator as opt

def testnum(num): 
    return Outputval(num)

class ExceptionFailure(RuntimeError):
    def __init__(self, message):
        self.message = message

class Outputresult:
    def __init__(self, numres):
        self.output = numres

class Outputval:
    def __init__(self, num):
        self.num = num
        self.lwrlmt = -100
        self.maxlmt = 100
        self.val = 13
        self.output = ''

    def singleinput(self, inpval):
        self._calc(inpval)

    def sumofarr(self, element):
        element = list(int(ele) if float(ele).is_integer() else float(ele) for ele in element)
        inpval = sum(element) if element else 0
        self._calc(inpval)

    def _calc(self, inpval):
        try:
            if (opt.gt(inpval, self.maxlmt) or opt.lt(inpval, self.lwrlmt) or opt.eq(inpval, self.val)):
                raise
            print(f"\n output for input {inpval} of {type(inpval)} type  is {10/inpval}")
        except Exception as e:
            if (isinstance(inpval,int) or isinstance(inpval,float)) and  (opt.gt(inpval, self.maxlmt) or opt.lt(inpval, self.lwrlmt) or opt.eq(inpval, self.val)):
                raise ExceptionFailure(f"SystemError for input {inpval} of {type(inpval)}")
            else:
                raise ExceptionFailure(f"{type(e).__name__} for input {inpval} of {type(inpval)} ") 
        
