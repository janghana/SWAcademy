N = int(input())
play_list = [input() for _ in range(N)]
play_list_runtime = [int(input()) for _ in range(N)]
M = int(input())
question_what_song = [int(input() ) for _ in range(M)]
play_list_dict = {}
prev = 0
for song, time in zip(play_list, play_list_runtime):
    play_list_dict[song] = [prev+1, time+prev]
    prev += time
print(play_list_dict)
for i in question_what_song:
    for j in play_list_dict:
        if i >= play_list_dict[j][0] and i<= play_list_dict[j][1]:
            print(j)
            break
