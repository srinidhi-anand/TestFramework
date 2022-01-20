import importlib.machinery
import types
from inspect import getmembers, isfunction
import sys
from program import ExceptionFailure

class TestRunner:
    def __init__(self, filename):
        self.test_file = filename
        self.successes, self.failures = 0, 0


    def load_tests(self, mod):
        return [m for m in getmembers(mod) if isfunction(m[1]) and m[0].endswith("_test")]

    def load_module(self):
        loader = importlib.machinery.SourceFileLoader("testmod", self.test_file)
        mod = types.ModuleType("testmod")
        loader.exec_module(mod)
        return mod

    def run(self):
        mod = self.load_module()
        tests = self.load_tests(mod)
        for test in tests:
            (test_name, test_function) = test
            try:
                test_function()
                self.successes += 1
                print(f"{test_name} - success\n")
            except ExceptionFailure as e:
                print(f"{test_name} - failure: {e.message}\n")
                self.failures += 1
            except AssertionError:
                print(f"{test_name} - failure\n")
                self.failures += 1


        print("\n**************")
        print(f"Total number of tests: {self.successes + self.failures}")
        if self.failures == 0:
            print("Test Cases Passed")
        else:
            print(f"{self.failures} Test Cases Failed")

if __name__ == "__main__":
    TestRunner(sys.argv[1]).run()
