import re
import openai
import os
from delete_comments import remove_comments
def translate_code(input_code,selected_source,selected_target):
        openai.api_key=os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f"Translate this importation:\n\n{input_code}\n\n from {selected_source} to {selected_target}",
            max_tokens=300,
            n=1,
            stop=None,
            temperature=1
        )
        translated_code = response.choices[0].text.strip()
        return translated_code
def java_parser_imports(file_path, output_dir_path):
    dir_path = os.path.dirname(file_path)
    remove_comments(dir_path)

    filename = os.path.basename(file_path)
    if filename.endswith(".java"):
        base_name = filename[:-5]  # remove .java extension
        output_file_path = os.path.join(output_dir_path, f"{base_name}_impo.cs")

        with open(file_path, 'r') as java_file, open(output_file_path, 'w') as output_file:
            java_code = java_file.read()

            imports = re.findall(r'^import\s+([\w\.]+);\s*$', java_code, re.MULTILINE)

            for i in imports:
                i = "using " + i + ";"
                i2 = translate_code(i, "java", "c#")
                output_file.write(i2 + "\n")

                
#java_parser_imports(r"C:\Users\IRezgui\Desktop\django_fin\javacode\Personne.java",r"C:\Users\IRezgui\Desktop\django_fin\javacode")
def csharp_parser_imports(file_path, output_dir_path):
    dir_path = os.path.dirname(file_path)
    remove_comments(dir_path)

    filename = os.path.basename(file_path)
    if filename.endswith(".cs"):
        base_name = filename[:-3]  # remove .cs extension
        output_file_path = os.path.join(output_dir_path, f"{base_name}_impo.java")

        with open(file_path, 'r') as csharp_file, open(output_file_path, 'w') as output_file:
            csharp_code = csharp_file.read()

            # Capture using statements in C#
            usings = re.findall(r'^(?:\s*)using\s+([\w\.]+);\s*$', csharp_code, re.MULTILINE)
                

            for u in usings:
                u = "using " + u + ";"
                u2 = translate_code(u, "c#", "java")
                output_file.write(u2 + "\n")


#csharp_parser_imports(r"C:\Users\IRezgui\Desktop\django_fin\javacode\Personne_impo.cs",r"C:\Users\IRezgui\Desktop\django_fin\javacode")