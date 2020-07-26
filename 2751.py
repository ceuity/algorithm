n = int(input())
num_list = []
for i in range(n):
    num_list.append(i)
print("\n".join(map(str, sorted(num_list))))