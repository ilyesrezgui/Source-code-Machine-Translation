import os
import re
from calc_tokens import number_tokens
import openai 
from delete_comments import remove_comments,remove_comments_plsql
from decompose import decomposing
from construct import csharp_construct,java_construct
from deleter import delete

def translate_my_code(input_code,selected_source,selected_target):
        openai.api_key=os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f'Translate from {selected_source} to {selected_target}: \n\n{input_code}\n\n and add the needed imports',
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0.2
        )
        translated_code = response.choices[0].text.strip()
        return translated_code
def trans(repo_path ,target_repo,selected_source,selected_target):
    # Loop over all files in the repository
    if selected_source=="java" or selected_source=="c#":
        remove_comments(repo_path)
    elif selected_source=="plsql":
        remove_comments_plsql(repo_path)
    for subdir, dirs, files in os.walk(repo_path):
        for file in files:
            # Check if file is a Java file
            if file.endswith(".java") and selected_source=="java":
                path=os.path.join(subdir, file)
                # Open the file and read its contents
                with open(path, "r") as f:
                    contents = f.read()
                    if number_tokens(contents)<2000:
                        translated=translate_my_code(contents,selected_source,selected_target)
                        if selected_target=="c#":
                            new_filename = os.path.splitext(file)[0] + "_combined.cs"
                        elif selected_target=="sql":
                            new_filename = os.path.splitext(file)[0] + "_combined.sql"
                        with open(os.path.join(target_repo, new_filename), "w") as f:
                            f.write(translated)
                    else:
                        decomposing(path,target_repo,"java","c#")
                        csharp_construct(target_repo)
                        delete(target_repo)
                # Create a new file with the combined contents
                
                    
            elif file.endswith(".cs") and selected_source=="c#":
                # Open the file and read its contents
                with open(os.path.join(subdir, file), "r") as f:
                    contents = f.read()
                    if number_tokens(contents)<2000:
                        translated=translate_my_code(contents,selected_source,selected_target)
                        if selected_target=="java":
                            new_filename = os.path.splitext(file)[0] + "_combined.java"
                        elif selected_target=="plsql":
                            new_filename = os.path.splitext(file)[0] + "_combined.sql"
                        with open(os.path.join(target_repo, new_filename), "w") as f:
                            f.write(translated)
                    else:
                        decomposing(path,target_repo,"c#","java")
                        java_construct(target_repo)
                        delete(target_repo)
                # Create a new file with the combined contents
                

            elif file.endswith(".sql") and selected_source=="plsql":
                # Open the file and read its contents
                with open(os.path.join(subdir, file), "r") as f:
                    contents = f.read()
                    if number_tokens(contents)<2000:
                        translated=translate_my_code(contents,selected_source,selected_target)
                    else:
                        pass
                # Create a new file with the combined contents
                if selected_target=="java":
                    new_filename = os.path.splitext(file)[0] + "_combined.java"
                elif selected_target=="c#":
                    new_filename = os.path.splitext(file)[0] + "_combined.cs"
                with open(os.path.join(target_repo, new_filename),"w") as f:
                    f.write(translated)
            
