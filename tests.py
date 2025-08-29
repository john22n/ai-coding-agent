import unittest
#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
#from functions.write_file import write_file
from functions.run_python import run_python_file


class TestToolFunctions(unittest.TestCase):
    ''' 
    def test_cal_list(self):
        result = get_files_info("calculator", ".")
        print(result)

    def test_pkg_dir(self):
        result = get_files_info("calculator", "pkg")
        print(result)

    def test_dir_not_in_working_dir(self):
        result = get_files_info("calculator", "./bin")
        print(result)

    def test_outside_dir(self):
        result = get_files_info("calculator", "../")
        print(result)
'''
    '''

    def test_file_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)

    def test_file_pkg_cal(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_file_bin(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)

    def test_file_not_found(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(result)

    '''
    
    def test_file_pkg_cal(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_file_bin(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)

    def test_file(self):
        result = run_python_file("calculator", "test.py")
        print(result)

    def test_file_main(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_file_nonexistent(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        
if __name__ == "__main__":
    unittest.main()
