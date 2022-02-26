import torch 
import torch.nn as nn 

class Kobert(nn.Module):
    """
    Base kobert model. 
    """
    def __init__(self, config):
        super.__init__()
        assert "kobert_path" in config.keys(),  "Kobert directory must be specified!"
        self.kobert = torch.load(config.get("kobert_path"))

    def forward(self, input_dict, **kwargs):
        sentence_embedding, pooled_embedding = self.kobert(input_dict)
        return sentence_embedding

    def predict(self, input):
        raise NotImplementedError()


class KobertForClassification(Kobert):
    def __init__(self, config):
        super.__init__()

    def forward(self, input_dict, **kwargs):
        sentence_emgedding = super.forward(input_dict, **kwargs)
        output = self.forward_from_bert_output(sentence_emgedding)
        return output

    def forward_from_bert_output(self, sentence_embedding):
        output = sentence_embedding
        # Do something...

        return output
        
    def predict(self, input):
        
        return None 