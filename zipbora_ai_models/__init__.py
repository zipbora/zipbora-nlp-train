
# =====================================================
def get_model_by_tag(tag:str):
    assert tag in TAGS.keys(), f"{tag} is not in, TAGS"
    tag = TAGS[tag]
    config = generate_config_by_tag(tag)
    model = generate_model_with_config(tag, config)
    return model

# =====================================================
TAGS = ["KBC1"]

def generate_config_by_tag(tag):
    import json 
    if tag == "C1":
        config = json.load("C1.config")

    else:
        raise ValueError("Not Implemented TAG!")

    return config


def generate_model_with_config(tag, config):
    if tag[:3] == "KBC":
        from zipbora_ai_models.model.kobert.modeling_kobert import KobertForClassification
        return KobertForClassification(config)
    
    else:
        ValueError("Generating model is failed...")

