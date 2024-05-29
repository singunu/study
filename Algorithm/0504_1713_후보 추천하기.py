# N = int(input())
# recommend = int(input())
# student = list(map(int,input().split()))
# frame = {}
# recommend_cnt = {}
# idx = 0
# while recommend:
#     if len(frame) == N and student[idx] not in frame:
#         min_reco = 0
#         min_idx = 0
#         for j in range(3):
#             if frame[j] == recommend_cnt[frame[j]]:
#                 if min_reco >= recommend_cnt[frame[j]]:
#                     min_reco = recommend_cnt[frame[j]]
#                     min_idx = frame[j]
#
#         frame.pop(min_idx)
#         recommend_cnt[min_idx] = 0
#
#     if student[idx] in frame:
#         recommend_cnt[idx] += 1
#     else:
#         frame.append(student[idx])
#         recommend_cnt[idx] += 1
#     recommend -= 1
#     idx += 1
#
# frame.sort()
# for i in frame:
#     print(i, end=' ')




N = int(input())
total_recommendations = int(input())
recommendations = list(map(int, input().split()))

frame = {}
recommend_cnt = {}

for idx, student in enumerate(recommendations):
    if student in frame:
        recommend_cnt[student] += 1
    else:
        if len(frame) < N:
            frame[student] = idx
            recommend_cnt[student] = 1
        else:
            min_student = min(frame, key=lambda x: (recommend_cnt[x], frame[x]))
            del frame[min_student]
            recommend_cnt.pop(min_student)
            frame[student] = idx
            recommend_cnt[student] = 1

frame_sorted = sorted(frame.keys())

for student in frame_sorted:
    print(student, end=' ')