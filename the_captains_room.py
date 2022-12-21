group_num = int(input())
room_list = input().split()

dict = {}

for room_num in room_list:
    if room_num in dict:
        dict[room_num] = dict.get(room_num) + 1
    else: 
        dict[room_num] = 1

for key,value in dict.items():
    if value == 1:
        print(key)