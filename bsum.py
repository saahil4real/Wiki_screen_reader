text_example = "Cross-Site Request Forgery basically allows you to force an unwanted action onto the victim. For example, you send a link to someone who is currently logged into their bank account. When that person accesses your link, it automatically transfers money out of their account into your account.This happens when there is no verification process to check that the user went through the appropriate steps to transfer money. What I mean is that in order to transfer money, a user needs to login, go to their transfer payment page, select the recipient and then transfer the money. When these appropriate steps are taken, a CSRF token is generated on each and every page as you progress through the application. Additionally the previous token is verified before the next step can process. You can think of this as a tracking system if any of those tokens are empty or wrong, the transaction does not process.There are many complex ways to test this, but the easiest way to manually run these tests is through proxying traffic. I will go through the process of making a transaction as described above and see if I can replay it. However, in the replay, my goal is to get the same end result without having to go through all of the steps, which proves that there is a CSRF vulnerability."

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

tokens_input = tokenizer.encode("summarize: "+text_example, return_tensors='pt', max_length=512, truncation=True)
ids = model.generate(tokens_input, min_length=80, max_length=120)
summary = tokenizer.decode(ids[0], skip_special_tokens=True)

print(summary)