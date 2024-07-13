from fastapi import FastAPI
from translate_simple import translate_my_code
from calc_tokens import number_tokens
from decompose import decomposing
from construct import java_construct,csharp_construct
from deleter import delete
from lessthan2000 import trans
from nberrors import sum_errors_in_repository
from pre_analysis import analyze
import pandas as pd
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello ":"ilyes"}


@app.get("/translate_simple")
async def translate_api(input_code:str,selected_source:str,selected_target:str):
    translation= translate_my_code(input_code,selected_source,selected_target)
    return {"translation":translation}


@app.get("/calculate_tokens")
async def calculate_api(input_code:str):
    tokens= number_tokens(input_code)
    return {"number of tokens":tokens}

@app.get("/translator")
async def repo2000_translator_api(src_repo:str,target_repo:str,selected_source:str,selected_target:str):
    trans(src_repo,target_repo,selected_source,selected_target)
    return {"The translation process id done ! Check your target repo "+ target_repo}



@app.get("/analyzer")
async def analyzer(repo:str,target_repo:str,language:str):
    l,l2,l3,sum,sum2=sum_errors_in_repository(repo,target_repo,language)
    return {"nb_err_source":l,
           "nb_err_target":l2, 
           "files":l3,
           "sum_errors_source":sum,
           "sum_errors_target":sum2}


@app.get("/preanalyzer")
async def pre_analyzer(repo:str,language:str):
    p=analyze(repo,language)
    json_data = p.to_json(orient='records')
    # Return JSON response
    return json.loads(json_data)
