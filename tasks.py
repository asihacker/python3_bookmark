import os
print(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(BASE_DIR))
# b = sys.path.append(BASE_DIR)

# print(b)