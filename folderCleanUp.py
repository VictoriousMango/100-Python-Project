import os
cleanup_files = [file for file in os.listdir('.') if file.endswith('.gif') or file.endswith('.png')]
print(cleanup_files)
for file in cleanup_files:
    os.remove(file)
cleanup_files = [file for file in os.listdir('./data') if file.endswith('.gif') or file.endswith('.png')]
print(cleanup_files)
for file in cleanup_files:
    os.remove('./data/'+file)