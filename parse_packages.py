import os
import re
import openai 
from delete_comments import remove_comments

def translate_code(few_shot,input_code,selected_source,selected_target):
        openai.api_key=os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f"""{few_shot}
            Translate this package declaration :\n\n{input_code}\n\n from {selected_source} to {selected_target}""",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.2
        )

        translated_code = response.choices[0].text.strip()

        return translated_code
def java_parser_pkg(java_file_path, output_dir):
    few_shot = """package com.language.name; =>namespace com.language.name"""
    remove_comments(java_file_path)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(java_file_path, 'r') as f:
        java_code = f.read()

    csharp_code = ""

    package_pattern = re.compile(r"package\s+(\w+(\.\w+)*)\s*;")
    last_package_end = 0

    for package_match in package_pattern.finditer(java_code):
        package_name = package_match.group(1)
        package_start = package_match.start()
        package_end = package_match.end()

        package_code = java_code[package_start:package_end]
        output_code = translate_code(few_shot,package_code, "java","c#")
        csharp_code += f"{output_code}\n"
            

    csharp_file = os.path.join(output_dir, os.path.splitext(os.path.basename(java_file_path))[0] + '_pkgs.cs')

    try:
        with open(csharp_file, 'w') as f:
            f.write(csharp_code)

    except OSError as e:
        print(f"Error writing file: {e}")


def csharp_parser_pkg(csharp_file_path, output_dir):
    remove_comments(csharp_file_path)
    few_shot = """namespace com.language.name => package com.language.name;"""

    with open(csharp_file_path, 'r') as f:
        csharp_code = f.read()

    java_code = ""

    namespace_pattern = re.compile(r"namespace\s+(\w+(\.\w+)*)\s*{")
    last_namespace_end = 0

    for namespace_match in namespace_pattern.finditer(csharp_code):
        namespace_name = namespace_match.group(1)
        namespace_start = namespace_match.start()
        namespace_end = namespace_match.end()

        namespace_code = csharp_code[namespace_start:namespace_end]
        output_code = translate_code(few_shot, namespace_code, "c#", "java")
        java_code += f"{output_code}\n"

    java_file = os.path.join(output_dir, os.path.splitext(os.path.basename(csharp_file_path))[0] + '_pkgs.java')

    try:
        with open(java_file, 'w') as f:
            f.write(java_code)
    except OSError as e:
        print(f"Error writing file: {e}")

#javacode_parser_pkg(r"C:\Users\IRezgui\Desktop\django_fin\javacode\Personne_pkgs.cs",r"C:\Users\IRezgui\Desktop\django_fin\javacode")
