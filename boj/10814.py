from operator import itemgetter

if __name__ == "__main__":
    n = int(input())
    member_list = []
    age = 0
    name = ""
    for i in range(n):
        age, name = input().split()
        member_list.append([int(age), name])
    sort_member_list = sorted(member_list, key=itemgetter(0))
    for j in sort_member_list:
        print(j[0],j[1])
