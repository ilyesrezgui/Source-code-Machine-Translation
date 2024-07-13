import os
import fnmatch
import re

def remove_comments(directory_path):
    """
    Removes all comments from Java and C# files in a directory and its subdirectories.
    """
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            if fnmatch.fnmatch(filename, '*.java') or fnmatch.fnmatch(filename, '*.cs'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r') as file:
                    contents = file.read()

                # Remove all multi-line comments
                contents = re.sub(re.compile("/\*.*?\*/",re.DOTALL ),"", contents)

                # Remove all single-line comments
                contents = re.sub(re.compile("//.*?\n" ),"",contents)

                with open(file_path, 'w') as file:
                    file.write(contents)

#remove_comments(r"C:\Users\IRezgui\Desktop\django_fin\javacode")

def remove_comments_plsql(directory_path):
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            if fnmatch.fnmatch(filename, '*.sql'):
                file_path = os.path.join(dirpath, filename)
                print("hello",file_path)
                with open(file_path,"r") as input_file:
                    sql_text = input_file.read()
                single_line_comment_pattern = re.compile(r"--.*")
                multi_line_comment_pattern = re.compile(r"/\*.*?\*/", re.DOTALL)
                sql_text = multi_line_comment_pattern.sub("", sql_text)
                sql_text = single_line_comment_pattern.sub("", sql_text)
                with open(file_path, "w") as output_file:
                    output_file.write(sql_text)

