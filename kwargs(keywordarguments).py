# *args = parameter that packs all arguments into a dictionary. it is useful so 
# that function can accept a varying amount of keyword args.

def hello(**anything):
    print("hey",anything['first'],anything['last'],"hope you have a great day !")
    print("all K-V pairs are : ")
    for key,value in anything.items():
        print(value,end="\n")

hello(first="kishore",last="nair",title="idk",favorite="titties")

