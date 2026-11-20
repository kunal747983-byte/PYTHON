def isos(n):
    for i in range(1,n, 2):
        print(" "*(int((n-i-1)/2))+'*'*i)

l = 20
isos(l)        
# print("      *")
# print("     **")
# print("    ***")
# print("   ****")
# print("  *****")
# print(" ******")
# print("*******")