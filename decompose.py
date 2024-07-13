from parse_class import java_parser_cls,csharp_parser_cls
from parse_variables import java_parser_var,csharp_parser_var
from parse_packages import java_parser_pkg,csharp_parser_pkg
from parse_methods import java_parser_meth,csharp_parser_meth
from parse_imports import java_parser_imports,csharp_parser_imports


def decomposing(src_file,target_repo,src_lang,target_lang):
    if src_lang.lower()=="java" and target_lang.lower()=="c#":
        java_parser_cls(src_file,target_repo)
        java_parser_imports(src_file,target_repo)
        java_parser_var(src_file,target_repo)
        java_parser_pkg(src_file,target_repo)
        java_parser_meth(src_file,target_repo)
    elif src_lang.lower()=="c#" and target_lang.lower()=="java":
        csharp_parser_meth(src_file,target_repo)
        csharp_parser_imports(src_file,target_repo)
        csharp_parser_cls(src_file,target_repo)
        csharp_parser_pkg(src_file,target_repo)
        csharp_parser_var(src_file,target_repo)

