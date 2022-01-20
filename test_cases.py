from program import testnum

# input valid single negative number to get desired result
def singlenegval_success_test():
    testnum(-99).singleinput(-99)

# input valid array of nos with +ve /-ve to get desired result
def arraysum_negval_success_test():
    testnum([1,-33,-3]).sumofarr([1,-33,-3])

# input valid single number to get desired result
def singleval_success_test():
    testnum(72).singleinput(72)

# input valid array of numbers to sum up to get desired result
def arraysum_success_test():
    testnum([1,33,3]).sumofarr([1,33,3])

# input invalid number to produce System Error Exception
def singleval_syserr_test():
    testnum(101).singleinput(101)

# input invalid number to produce ZeroDivisionError Exception
def singleval_divbyzero_test():
    testnum(0).singleinput(0)

# String type input to produce Type Error Exception
def singleval_typeErr_test():
    testnum('3').singleinput('3')

# input invalid numbers to sum up to produce System Error Exception
def arraysum_syserr_failure_test():
    testnum([20,0,-7]).sumofarr([20,0,-7])
