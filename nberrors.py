import subprocess
import os 

def calculate_errors_in_java_file(java_file):
    """
    Check the syntax of a Java file using the javac command.
    """
    try:
        result = subprocess.run([r"C:\Users\IRezgui\Desktop\django_fin\myenv\javac", java_file], capture_output=True, text=True)
    except FileNotFoundError:
        print("javac command not found. Make sure Java is installed.")
        return -1
    if result.returncode == 0:
        print("Java syntax is correct for the file :",java_file)
        return 0
    else:
        errors = result.stderr.strip().split('\n')
        num_errors = len(errors)
        return num_errors
##################################################################################################################
##################################################################################################################
def calculate_errors_in_csharp_file(csharp_file):
    """
    Check the syntax of a C# file using the csc command.
    """
    try:
        result = subprocess.run([r'C:\Users\IRezgui\Desktop\django_fin\myenv\c\csc', csharp_file], capture_output=True, text=True)
    except FileNotFoundError:
        print("csc command not found. Make sure .NET is installed.")
        return -1
    if result.returncode == 0:
        print("C# syntax is correct for the file :", csharp_file)
        return 0
    else:
        errors = result.stderr.strip().split('\n')
        num_errors = len(errors)
        return num_errors

def sum_errors_in_repository(repo_path,target_repo,language):
    total_errors = 0
    total_errors_target = 0
    l=[]
    l2=[]
    l3=[]
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            if language=="c#" and file_path.endswith('.cs'):  # Only process C# files
                errors = calculate_errors_in_csharp_file(file_path)
                filename_with_ext=os.path.basename(file_path) 
                filename_without_ext, ext = os.path.splitext(filename_with_ext)
                errors_target = calculate_errors_in_java_file(target_repo+filename_without_ext+"_combined.java")
                l.append(errors)
                l2.append(errors_target)
                l3.append(filename_without_ext )
                total_errors += errors
                total_errors_target +=errors_target
            if language=="java" and file_path.endswith('.java'):  # Only process Java files
                errors = calculate_errors_in_java_file(file_path)
                filename_with_ext=os.path.basename(file_path) 
                filename_without_ext, ext = os.path.splitext(filename_with_ext)
                errors_target = calculate_errors_in_java_file(target_repo+filename_without_ext+"_combined.java")
                l.append(errors)
                l2.append(errors_target)
                l3.append(filename_without_ext )
                total_errors += errors
                total_errors_target +=errors_target
    return l,l2,l3,total_errors,total_errors_target






