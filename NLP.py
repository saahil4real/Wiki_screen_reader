from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

document = '''Purana Qila (lit.\u2009'Old Fort') is one of the oldest forts in Delhi, India.
Built by the second Mughal Emperor Humayun and Surid Sultan Sher Shah, it is thought by many to be located on the site of the ancient city of Indraprastha. The fort formed the inner citadel of the city of Dinpanah. 
It is located near the expansive Pragati Maidan exhibition ground and is separated from the Dhyanchand Stadium by the Mathura Road, Delhi.'''
# Object of automatic summarization.
auto_abstractor = AutoAbstractor()
# Set tokenizer.
auto_abstractor.tokenizable_doc = SimpleTokenizer()
# Set delimiter for making a list of sentence.
auto_abstractor.delimiter_list = [".", "/n"]
# Object of abstracting and filtering document.
abstractable_doc = TopNRankAbstractor()
# Summarize document.
result_dict = auto_abstractor.summarize(document, abstractable_doc)
print(result_dict['summarize_result'])