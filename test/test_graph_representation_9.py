import re

def contains_list_comprehension(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    # Regular expression to match list comprehensions
    list_comp_pattern = re.compile(r'\[.*for.*in.*\]')
    return bool(list_comp_pattern.search(content))

def test_contains_list_comprehension():
    # Replace 'your_file.py' with the path to the file you want to test
    assert contains_list_comprehension('student_code.py') == True