import nlpcloud
def paraphrase(sentences: str, strong: bool = True):
    client = nlpcloud.Client("fast-gpt-j", "73f199d873172c9cbfca7f04d636fa7b3ffff4dc", True)
    
    return client.summarization(sentences)['summary_text']


