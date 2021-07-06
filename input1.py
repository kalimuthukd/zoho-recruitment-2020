# Python Program for input1

entered_text = input ("Enter the text :")
print(entered_text)
print(int(len(entered_text)/2))
count=int(len(entered_text)/2)


for i in range(11):
    if i == int(len(entered_text)/2):
        for j in range(i):
            count=i+j
            print (entered_text[count] ,end=' ')
    print()
