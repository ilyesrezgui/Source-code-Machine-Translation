from transformers import GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
def number_tokens(input_text):
    res=len(tokenizer(input_text)['input_ids'])
    return res


