#List of students who play cricket
C = [2, 5, 9, 12, 13, 15, 16, 17, 18, 19]
#List of students who play football
F = [2, 4, 5, 6, 7, 9, 13, 16]
#List of students who play hockey
H = [1, 2, 5, 9, 10, 11, 12, 13, 15]

# Write your code here
all_sports = [i for i in C if i in F and i in H]
cricket_and_football = [i for i in C if i in F and i not in H]
do_not_play_any = [i for i in range(1, 21) if (i in C and i in F and i not in H) or (i in F and i in H and i not in C) or (i in C and i in H and i not in F)]
two_sports = [i for i in range(1, 21) if i not in C and i not in F and i not in H]

# (Make sure your lists are sorted in ascending order before you print them out)
print(sorted(all_sports))
print(sorted(cricket_and_football))
print(sorted(do_not_play_any))
print(sorted(two_sports))
