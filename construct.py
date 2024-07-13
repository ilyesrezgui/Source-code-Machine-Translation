import os
def csharp_construct(directory_path):
    # Traverse the directory tree and read in the contents of the relevant files
    file_contents = {}
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith("_pkgs.cs") or file.endswith("_clas.cs") or file.endswith("_vars.cs") or file.endswith("_meth.cs") or file.endswith("_impo.cs"):
                with open(os.path.join(root, file), 'r') as f:
                    prefix = os.path.splitext(file)[0][:-4]
                    if prefix not in file_contents:
                        file_contents[prefix] = {'package': '', 'class': '', 'variables': '','imports': '', 'methods': ''}
                    if file.endswith("_pkgs.cs"):
                        file_contents[prefix]['package'] += f.read().strip() + "\n"
                    elif file.endswith("_clas.cs"):
                        file_contents[prefix]['class'] += f.read().strip() + "\n"
                    elif file.endswith("_vars.cs"):
                        file_contents[prefix]['variables'] += f.read().strip() + "\n"
                    elif file.endswith("_impo.cs"):
                        file_contents[prefix]['imports'] += f.read().strip() + "\n"
                    elif file.endswith("_meth.cs"):
                        file_contents[prefix]['methods'] += f.read().strip() + "\n"
    # Construct the C# code as a string for each prefix
    for prefix, contents in file_contents.items():
        code = f'''
    {contents['package']}
    {contents['imports']}
    {{
        {contents['class']}
        {{
            {contents['variables']}

            {contents['methods']}
        }}
    }}
    '''
            # Write the C# code to a file with the prefix from the input files
        output_file = os.path.join(directory_path, f"{prefix}combined.cs")
        with open(output_file, 'w') as f:
            f.write(code)

def java_construct(directory_path):
    # Traverse the directory tree and read in the contents of the relevant files
    file_contents = {}
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith("_pkgs.java") or file.endswith("_clas.java") or file.endswith("_vars.java") or file.endswith("_meth.java")or file.endswith("_impo.java"):
                with open(os.path.join(root, file), 'r') as f:
                    prefix = os.path.splitext(file)[0][:-4]
                    if prefix not in file_contents:
                        file_contents[prefix] = {'package': '', 'imports': '', 'class': '', 'variables': '', 'methods': ''}
                    if file.endswith("_pkgs.java"):
                        file_contents[prefix]['package'] += f.read().strip() + "\n"
                    elif file.endswith("_clas.java"):
                        file_contents[prefix]['class'] += f.read().strip() + "\n"
                    elif file.endswith("_vars.java"):
                        file_contents[prefix]['variables'] += f.read().strip() + "\n"
                    elif file.endswith("_meth.java"):
                        file_contents[prefix]['methods'] += f.read().strip() + "\n"
                    elif file.endswith("_impo.java"):
                        file_contents[prefix]['imports'] += f.read().strip() + "\n"
    # Construct the Java code as a string for each prefix
    for prefix, contents in file_contents.items():
        code = f'''
   {contents['package']}
    {contents['imports']}
    {{
        {contents['class']}
        {{
            {contents['variables']}

            {contents['methods']}
        }}
    }}
'''
        # Write the Java code to a file with the prefix from the input files
        output_file = os.path.join(directory_path, f"{prefix}combined.java")
        with open(output_file, 'w') as f:
            f.write(code)

#java_construct(r"C:\Users\IRezgui\Desktop\django_fin\javacode")