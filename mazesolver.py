import sys


class Graph:
    def __init__(self):
        self.V = 0
        self.start = (0, 0)
        self.end = (0, 0)

    def create_matrix_from_file(self):
        counter = 0
        lst_g = []
        with open(sys.argv[2], 'r') as f:
            contents = f.read()
            lst = contents.split("\n")
            lst_g = lst
            counter = len(lst)
            self.V = counter
            self.end = (self.V - 1, self.V - 1)
        f.close()

        self.adj_matrix = [
            [
              0 for i in range(self.V)
            ] for j in range(self.V)
        ]
        ele_list = []
        for ele in lst_g:
            lst3 = ele.split()
            for e in lst3:
                ele_list.append(e)

        for i in range(self.V):
            for j in range(self.V):
                self.adj_matrix[i][j] = int(ele_list.pop(0))

    def get_path(self, v):
        left_move = (v[0], v[1]-1)
        right_move = (v[0], v[1]+1)
        up_move = (v[0] - 1, v[1])
        down_move = (v[0] + 1, v[1])
        lst = []
        lst.append(left_move)
        lst.append(right_move)
        lst.append(up_move)
        lst.append(down_move)
        possible_next = []

        for move in lst:
            if move[0] >= 0 and move[1] >= 0 and move[0] < self.V and move[1] < self.V:
                if self.adj_matrix[move[0]][move[1]] == 1 and move not in self.visited:
                    possible_next.append(move)

        maxm = -1
        next_move = (0, 0)
        for move in possible_next:
            if move[1] >= maxm:
                maxm = move[1]
                next_move = move
        return next_move

    def maze_solver(self):
        self.visited = []
        queue = []
        queue.append(self.start)
        self.visited.append(self.start)
        while queue:
            v = queue.pop()
            if v == self.end:
                break

            next_index = self.get_path(v)
            if next_index != (0, 0) and next_index is not None:
                queue.append(next_index)
                self.visited.append(next_index)
        if self.visited[-1] != self.end:
            print("Path is not present")
            return -1
        else:
            print("Path is present")
        return 1

    def write_maze_matrix(self):
        w = open(sys.argv[4], "w")
        contents = ""
        if self.visited[-1] != self.end:
            w.write("-1")
            w.close()
            return -1
        path_matrix = [
            [
                0 for i in range(self.V)
            ] for j in range(self.V)
        ]

        for path in self.visited:
            path_matrix[path[0]][path[1]] = 1

        for i in range(self.V):
            for j in range(self.V):
                contents = contents+str(path_matrix[i][j]) + " "
            contents = contents + "\n"
        w.write(contents)
        w.close()


g = Graph()


g.create_matrix_from_file()

flag = g.maze_solver()
g.write_maze_matrix()
