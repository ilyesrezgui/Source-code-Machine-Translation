import re
import os
import openai 
from delete_comments import remove_comments
def translate_code(input_code,selected_source,selected_target):
        openai.api_key=os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f"Translate this variable declaration :\n\n{input_code}\n\n from {selected_source} to {selected_target}",
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=1
        )
        translated_code = response.choices[0].text.strip()
        return translated_code



def java_parser_var(java_file_path,output_dir):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(java_file_path, 'r') as f:
        java_code = f.read()

    csharp_code = ""

    instance_variable_pattern = re.compile(r"(private|protected|public)\s+(\w+)\s+(\w+)\s*;")
    last_variable_end = 0

    for variable_match in instance_variable_pattern.finditer(java_code):
        variable_access = variable_match.group(1)
        variable_type = variable_match.group(2)
        variable_name = variable_match.group(3)
        variable_start = variable_match.start()
        variable_end = variable_match.end()

        variable_code = java_code[variable_start:variable_end]
        output_code = translate_code(variable_code, "java", "c#")
        csharp_code += f"{output_code}\n"

    csharp_file = os.path.join(output_dir, os.path.splitext(os.path.basename(java_file_path))[0] + '_vars.cs')

    try:
        with open(csharp_file, 'w') as f:
            f.write(csharp_code)
    except OSError as e:
        print(f"Error writing file: {e}")



def csharp_parser_var(csharp_file_path,output_dir):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(csharp_file_path, 'r') as f:
        csharp_code = f.read()

    java_code = ""
    instance_variable_pattern = re.compile(r"(private|protected|public)\s+(static\s+)?([\w<>\[\],]+\s+)+(\w+)\s*(=\s*.+)?\s*;")
    last_variable_end = 0

    for variable_match in instance_variable_pattern.finditer(csharp_code):
        variable_access = variable_match.group(1)
        variable_type = variable_match.group(2)
        variable_name = variable_match.group(3)
        variable_start = variable_match.start()
        variable_end = variable_match.end()

        variable_code = csharp_code[variable_start:variable_end]
        output_code = translate_code(variable_code, "c#", "java")
        java_code += f"{output_code}\n"

    java_file = os.path.join(output_dir, os.path.splitext(os.path.basename(csharp_file_path))[0] + '_vars.java')

    try:
        with open(java_file, 'w') as f:
            f.write(java_code)
    except OSError as e:
        print(f"Error writing file: {e}")




#javacode_parser_var(r"C:\Users\IRezgui\Desktop\django_fin\javacode\Personne_vars.cs",r"C:\Users\IRezgui\Desktop\django_fin\javacode",)