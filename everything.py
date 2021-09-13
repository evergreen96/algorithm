def calc(board):
    n = len(board)
    m = len(board[0])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                cnt+=1
    return cnt


def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    for who, x1,y1, x2,y2, vol in skill:
        if who==1:#attack
            for a in range(x1, n):
                for b in range(y1, m):
                    board[a][b] -= vol
            
            for a in range(x2+1, n):
                for b in range(y2+1, n):
                    board[a][b] -= vol
            
            for a in range(x1, n):
                for b in range(y2+1, m):
                    board[a][b] += vol
            
            for a in range(x2+1, n):
                for b in range(y1, m):
                    board[a][b] += vol
        else:
            for a in range(x1, n):
                for b in range(y1, m):
                    board[a][b] += vol
            
            for a in range(x2+1, n):
                for b in range(y2+1, n):
                    board[a][b] += vol
            
            for a in range(x1, n):
                for b in range(y2+1, m):
                    board[a][b] -= vol
            
            for a in range(x2+1, n):
                for b in range(y1, m):
                    board[a][b] -= vol
    print(board)
    return calc(board)


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],	
[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))