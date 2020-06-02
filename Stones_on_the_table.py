count=0
n = int(input())
chr = input()
for i in range(n-1):
    if (chr[i]==chr[i+1]):
        count+=1

print(count)