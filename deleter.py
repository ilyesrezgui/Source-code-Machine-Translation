import os
import glob
# specify the directory path where files need to be deleted
def delete(dir_path):
    # define the file patterns to be deleted
    file_patterns = ["*_meth.java","*_meth.cs", "*_clas.java","*_clas.cs", "*_vars.java","*_vars.cs", "*_pkgs.java","*_pkgs.cs", "*meth.java","*meth.cs", "*impo.cs","*impo.java"]

    # loop through each file pattern
    for pattern in file_patterns:
        # get a list of all files in the directory that match the pattern
        files = glob.glob(os.path.join(dir_path, pattern))
        # loop through each file and delete it
        for file in files:
            os.remove(file)