while True:
    boat_capacity = int(input("Input boat capacity (>0):"))
    if boat_capacity > 0: 
        break

while True:
    initial_cannibals = int(input("Input initial cannibals (>0):"))
    if initial_cannibals >0:
        break

while True:
    initial_missionaries = int(input("Input initial cannibals (>0):"))
    if initial_missionaries >0:
        break

class State(object):
    def __init__(self, m, c, b = 0):
        super(State, self)
        self.m = m
        self.c = c
        self.b = b

    def valid_state(s):
        for j in range(2):
            if s.m[j] > 0 and s.m[j] < s.c[j]:
                return False
        return True
    def __str__(self):
        return f"(m = {self.m}, c = {self.c})"

    def next_states(self, visited):
        l = {self}

        for i in range(min(boat_capacity, self.m[self.b])+1):
            m_next = [self.m[0], self.m[1]]


            if i > 0:
                b_next = 1 if self.b == 0 else 0
            else:
                b_next = self.b

            m_next[b_next] = self.m[b_next] + i
            m_next[self.b] = self.m[self.b] - i
            
            for j in range(max(0,self.c[self.b] - m_next[self.b]), min(boat_capacity, m_next[b_next] - self.c[b_next],self.c[self.b])+1):
                c_next = [self.c[0], self.c[1]]
                
                if j > 0 or i > 0:
                    b_next = 1 if self.b == 0 else 0

                    c_next[b_next] = self.c[b_next] + j
                    c_next[self.b] = self.c[self.b] - j
                    l.add(State(m_next,c_next,b_next))

        return {state for state in l - visited}


def is_goal_state(s):
    return s.c[0] == s.m[0] == 0

initial_state = State(m = [initial_missionaries, 0], c = [initial_cannibals, 0])

def BFS_with_path(initial_state):
    parent_dict = {initial_state: None}
    visited = {initial_state}
    queue = [initial_state]
    while queue:
        state = queue.pop(0)
        if is_goal_state(state):
            return reconstruct_path(parent_dict, state)
        for next_state in state.next_states(visited):
            parent_dict[next_state] = state
            visited.add(next_state)
            queue.append(next_state)
    return []

def reconstruct_path(parent_dict, state):
    path = [state]
    while parent_dict[state] is not None:
        state = parent_dict[state]
        path.append(state)
    path.reverse()
    return path

print([str(s) for s in BFS_with_path(initial_state)])

