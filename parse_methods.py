import re
import os
import openai 
from delete_comments import remove_comments

def translate_code(input_code,selected_source,selected_target):
        openai.api_key=os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f'Translate this code:\n\n{input_code}\n\n from {selected_source} to {selected_target}',
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.2
        )

        translated_code = response.choices[0].text.strip()

        return translated_code
def java_parser_meth(java_file_path, output_dir):
    remove_comments(java_file_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(java_file_path, 'r') as f:
        java_code = f.read()

    csharp_code = ""

    method_pattern = re.compile(r"(public|private|protected)?\s+(static\s+)?([a-zA-Z0-9_]+|\s*)\s*(\w+)\s*\([^\)]*\)\s*({|\s*throws)")

    last_method_end = 0

    def find_method_end(code, start_index):
        depth = 1
        i = start_index
        while depth > 0 and i < len(code):
            if code[i] == '{':
                depth += 1
            elif code[i] == '}':
                depth -= 1
            i += 1
        return i

    for method_match in method_pattern.finditer(java_code):
        method_name = method_match.group(4)
        method_start = method_match.start()
        method_end = find_method_end(java_code, method_match.end())

        method_code = java_code[method_start:method_end]
        output_code = translate_code(method_code,"java","c#")
        csharp_code += output_code + "\n"

    csharp_file = os.path.join(output_dir, os.path.splitext(os.path.basename(java_file_path))[0] + '_meth.cs')

    try:
        with open(csharp_file, 'w') as f:
            f.write(csharp_code)
    except OSError as e:
        print(f"Error writing file: {e}")


def csharp_parser_meth(csharp_file_path, output_dir):
    remove_comments(csharp_file_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(csharp_file_path, 'r') as f:
        csharp_code = f.read()

    java_code = ""

    method_pattern = re.compile(r"(public|private|protected)?\s+(static\s+)?(async\s+)?[\w\<\>\[\],]+\s+([\w\[\]]+|[\w\[\]]+\s*\([\w\s\[\],]*\))\s*\(([^\)]*)\)\s*(:\s*base\([^\)]*\))?\s*({|\s*throws)")

    last_method_end = 0

    def find_method_end(code, start_index):
        depth = 1
        i = start_index
        while depth > 0 and i < len(code):
            if code[i] == '{':
                depth += 1
            elif code[i] == '}':
                depth -= 1
            i += 1
        return i

    for method_match in method_pattern.finditer(csharp_code):
        method_name = method_match.group(4)
        method_start = method_match.start()
        method_end = find_method_end(csharp_code, method_match.end())

        method_code = csharp_code[method_start:method_end]
        output_code = translate_code(method_code,"c#","java")
        java_code += output_code + "\n"

    java_file = os.path.join(output_dir, os.path.splitext(os.path.basename(csharp_file_path))[0] + '_meth.java')

    try:
        with open(java_file, 'w') as f:
            f.write(java_code)
    except OSError as e:
        print(f"Error writing file: {e}")
