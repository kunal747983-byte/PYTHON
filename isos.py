def isos(n):
    for i in range(1,n, 2):
        # print(" "*(int((n-i-1)/2))+'*'*i)
        # print(" "*(int((n-i-1)/2))+ '*' +" "*(int((n-i-1)/2))+ '*'+" "*(int((n-i-1)/2)))
        print(" "*((n-i)//2)+'*'*(i)+(i-1)*" ")
l = 20
isos(l)        
# print("      *")
# print("     **")
# print("    ***")
# print("   ****")
# print("  *****")
# print(" ******")
# print("*******")