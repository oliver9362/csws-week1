invite_list = ['Bob', 'Steve', 'John']
print("Please join me for dinner " +invite_list[0])
print("Please join me for dinner " +invite_list[1])
print("Please join me for dinner " +invite_list[2])

absent = invite_list.pop(1)
print("Unfortunately " +absent, "cannot make it")

invite_list.insert(1, 'Dan')
print("Please join me for dinner " +invite_list[0])
print("Please join me for dinner " +invite_list[1])
print("Please join me for dinner " +invite_list[2])