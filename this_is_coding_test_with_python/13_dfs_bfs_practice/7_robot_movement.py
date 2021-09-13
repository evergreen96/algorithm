
from collections import deque

def get_next_pos(pos ,n, board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    next_pos = []
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for i in range(4):
        n_pos1_x, n_pos1_y, n_pos2_x, n_pos2_y = pos1_x + dx[i], pos1_y+dy[i], pos2_x+dx[i], + pos2_y+dy[i]
        if 0<= n_pos1_x < n and 0<= n_pos1_y < n and 0<= n_pos2_x < n and 0<= n_pos2_y < n and board[n_pos1_x][n_pos1_y]==0 and  board[n_pos2_x][n_pos2_y]==0:
            next_pos.append([ [n_pos1_x, n_pos1_y], [n_pos2_x, n_pos2_y] ])

    #가로 일경우
    if pos1_x== pos2_x:
        for i in [-1, 1]:
            if 0<=pos1_x+i<n and board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0:
                next_pos.append([ [pos1_x, pos1_y], [pos1_x+i, pos1_y] ])
                next_pos.append([ [pos2_x, pos2_y], [pos2_x+i, pos2_y] ])
    #세로 일경우
    if pos1_y==pos2_y:
        for i in [-1, 1]:
            if 0<=pos1_y+i<n and board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0:
                next_pos.append([ [pos1_x, pos1_y], [pos1_x, pos1_y+i] ])
                next_pos.append([ [pos2_x, pos2_y], [pos2_x, pos2_y+i] ])

    return next_pos


def solution(board):
    n = len(board)
    visited = set([(0, 0), (0, 1)])
    q = deque()
    q.append([ [[0, 0],[0, 1]], 0])
    while q:
        pos, now = q.popleft()
        if [n-1, n-1] in pos:
            return now
        
        for new_pos in get_next_pos(pos, n, board):
            vv = tuple(map(tuple, new_pos))
            if vv not in visited:
                q.append([ new_pos, now+1])
                visited.add(vv)

    return 0

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))