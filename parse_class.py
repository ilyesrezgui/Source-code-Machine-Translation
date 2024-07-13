import os
import re
import openai 
from delete_comments import remove_comments
def translate_code(input_code,selected_source,selected_target):
        openai.api_key=os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f'Translate this class declation: \n\n{input_code}\n\n from {selected_source} to {selected_target}',
            max_tokens=400,
            n=1,
            stop=None,
            temperature=0.2
        )
        translated_code = response.choices[0].text.strip()
        return translated_code
def java_parser_cls(java_file_path, output_dir):
    remove_comments(java_file_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(java_file_path, 'r') as f:
        java_code = f.read()
    csharp_code = ""
    class_pattern = re.compile(r"(public\s+)?(abstract\s+)?(final\s+)?(strictfp\s+)?(class|interface)\s+(\w+)\s*"
                               r"((extends\s+\w+(\.\w+)*(\s*,\s*\w+(\.\w+)*)*)?(\s+implements\s+\w+(\.\w+)*"
                               r"(\s*,\s*\w+(\.\w+)*)*)?)?\s*")
    last_class_end = 0

    for class_match in class_pattern.finditer(java_code):
        class_name = class_match.group(4)
        class_start = class_match.start()
        class_end = class_match.end()

        if class_start < last_class_end:
            continue

        class_code = java_code[class_start:class_end]
        output_code = translate_code(class_code, "java", "c#")
        csharp_code += f"{output_code}\n"

        last_class_end = class_end

    csharp_file = os.path.join(output_dir, os.path.splitext(os.path.basename(java_file_path))[0] + '_clas.cs')

    try:
        with open(csharp_file, 'w') as f:
            f.write(csharp_code)

    except OSError as e:
        print(f"Error writing file: {e}")

def csharp_parser_cls(file_path, output_dir):
    dir_path = os.path.dirname(file_path)
    remove_comments(dir_path)

    with open(file_path, 'r') as f:
        csharp_code = f.read()

    java_code = ""

    class_pattern = re.compile(r"\b(public|private|internal)?\s+(sealed\s+)?\b(class|struct|interface)\s+(\w+)\s*(<\s*\w+\s*>)?\s*(:\s*\w+\s*(,\s*\w+\s*)*)?\s*{")
    last_class_end = 0

    for class_match in class_pattern.finditer(csharp_code):
        class_name = class_match.group(5)
        class_start = class_match.start()
        class_end = class_match.end()
        if class_start < last_class_end:
            continue
        class_code = csharp_code[class_start:class_end]
        output_code = translate_code(class_code, "c#", "java")
        java_code += f"{output_code}\n"
        last_class_end = class_end
    java_file = os.path.join(output_dir, os.path.splitext(os.path.basename(file_path))[0] + '_clas.java')
    try:
        with open(java_file, 'w') as f:
            f.write(java_code)
    except OSError as e:
        print(f"Error writing file: {e}")

