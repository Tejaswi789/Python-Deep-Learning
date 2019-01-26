p=input("enter the sentence..")
d=0
l=0

for c in p:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print('words')
print(len(p.split()))
print("Letters", l)
print("Digits", d)

