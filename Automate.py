import os

os.chdir('/Users/unterbratka/Desktop/untitled folder')

for f in os.listdir():
    file_name, file_extension = os.path.splitext(f)
    f_title, f_course, f_num = file_name.split('-')

    f_title = f_title.strip() # Get rid of all whitespaces
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2) # [1:] This makes # sign to disappear, zfill(2) make numbers to be 2 digits

    new_name = '{}-{}-{}{}'.format(f_num, f_course, f_title, file_extension)
    os.rename(f, new_name)
