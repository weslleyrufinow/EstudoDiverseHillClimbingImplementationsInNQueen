import random 
import copy

def get_queensidxs(board):
    q = []
    for j in range(len(board[0])):
        c = -1
        for k in range(len(board[0])):
            if board[j][k] == 1:
                c = k
                break
        q.append(c)
    return q

class NQueen:

    def __init__(self, n=8):
        assert n > 3
        self.n = n
        self.board = []
        for i in range(n):
            self.board.append([0] * n)
            j = random.randint(0, n-1)
            self.board[i][j] = 1

    def __str__(self):
        out = []
        for l in self.board:
            nl = ",".join([str(s) for s in l])
            out.append(nl)
        return "\n".join(out)

    def __getitem__(self, idx):
        l, c = idx
        return self.board[l][c]

    def deepcopy(self):
        return copy.deepcopy(self) 

    def attacks(self):
        queens = get_queensidxs(self.board)
        h = 0
        for i in range(self.n):
            for j  in range(self.n):
                if i != j:
                    c1 = queens[i]
                    c2 = queens[j]
                    h +=  1 if ( (c1 == c2) or (abs(c2 - c1) == abs(i - j)) )else 0
        return h

    def moveTo(self, j, i):
        queens = get_queensidxs(self.board)
        p = queens[i]
        tmp = self.board[i][j]
        self.board[i][j] = self.board[i][p]
        self.board[i][p] = tmp

       
