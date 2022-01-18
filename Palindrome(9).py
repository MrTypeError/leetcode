x=int(input("Enter the Number : "))
dupX=x
temp=0
while dupX is True:
    remander=dupX%10
    temp=(temp*10)+remander
    dupX=dupX/10
if x==temp:
    print("palindrome Number ")
else:
    print("Not a palindrome Number")


