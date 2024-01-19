from prototype_link_extracter import link_extractor
def_dict = link_extractor("https://en.wikipedia.org/wiki/Delhi")
for key,value in def_dict.items():
    print(key, " == " ,value)
    print()
    print()