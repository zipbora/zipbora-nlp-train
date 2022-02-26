from multiprocessing.sharedctypes import Value
from zipbora_ai_models.utils.tokenizer.monologg_kobert import  KoBertTokenizer

def get_tokenizer(name):
    if name in ["roomai/kobert", "roomai/kobert-distil", "roomai/kobert-lm"]:
        vocab_file = KoBertTokenizer.pretrained_vocab_files_map['vocab_file'][name]
        vocab_txt = KoBertTokenizer.pretrained_vocab_files_map['vocab_txt'][name]
        return KoBertTokenizer(vocab_file=vocab_file, vocab_txt=vocab_txt)
    
    else:
        raise ValueError("[Error] Not implemented model type!")