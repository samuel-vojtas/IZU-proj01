"""
    Project:        UCS algorithm with CLOSED
    Name:           proj01.py
    Author:         Samuel Vojtáš
    Login:          xvojta09
    Faculty:        VUT FIT
    Date:           March, 2021
"""

class State():
    """ Prices for operators """
    op_prices = [1, 2, 4, 5, 2, 4, 5, 4, 5, 5]

    def __init__(self, left_side, right_side, price, predecessor):
        self.left_side = left_side
        self.right_side = right_side
        self.price = price
        self.predecessor = predecessor

    @staticmethod
    def get_op_price(n):
        """ Returns a price for a given operator """
        if 1 <= n <= 10:
            return State.op_prices[n - 1]
        else:
            exit(1)

    def equals(self, other):
        """ Two states are the same if their left and right sides equal """
        return self.left_side == other.left_side and self.right_side == self.right_side

    def in_list(self, lst):
        """ Returns True if there is a state with the same left and right side (price does not have to be the same). """
        for item in lst:
            if self.equals(item):
                return True
        return False

    def __repr__(self):
        """ String representation of the state """
        return "["+ "".join(sorted(self.left_side)) + str(self.price) + "".join(sorted(self.right_side)) + "]"

    def operator(self, n):
        """ Operators are indexed from 1 to 10 """
        new = State(self.left_side.copy(), self.right_side.copy(), self.price + State.get_op_price(n), self)

        if n == 1:
            # A <-
            new.right_side.remove('*')
            new.right_side.remove('A')
            new.left_side.add('A')
            new.left_side.add('*')

        elif (n == 2):
            # B <-
            new.right_side.remove('*')
            new.right_side.remove('B')
            new.left_side.add('B')
            new.left_side.add('*')

        elif (n == 3):
            # C <-
            new.right_side.remove('*')
            new.right_side.remove('C')
            new.left_side.add('C')
            new.left_side.add('*')

        elif (n == 4):
            # D <-
            new.right_side.remove('*')
            new.right_side.remove('D')
            new.left_side.add('D')
            new.left_side.add('*')

        elif (n == 5):
            # AB ->
            new.left_side.remove('*')
            new.left_side.remove('A')
            new.left_side.remove('B')
            new.right_side.add('*')
            new.right_side.add('A')
            new.right_side.add('B')

        elif (n == 6):
            # AC ->
            new.left_side.remove('*')
            new.left_side.remove('A')
            new.left_side.remove('C')
            new.right_side.add('*')
            new.right_side.add('A')
            new.right_side.add('C')

        elif (n == 7):
            # AD ->
            new.left_side.remove('*')
            new.left_side.remove('A')
            new.left_side.remove('D')
            new.right_side.add('*')
            new.right_side.add('A')
            new.right_side.add('D')

        elif (n == 8):
            # BC ->
            new.left_side.remove('*')
            new.left_side.remove('B')
            new.left_side.remove('C')
            new.right_side.add('*')
            new.right_side.add('B')
            new.right_side.add('C')

        elif (n == 9):
            # BD ->
            new.left_side.remove('*')
            new.left_side.remove('B')
            new.left_side.remove('D')
            new.right_side.add('*')
            new.right_side.add('B')
            new.right_side.add('D')

        elif (n == 10):
            # CD ->
            new.left_side.remove('*')
            new.left_side.remove('C')
            new.left_side.remove('D')
            new.right_side.add('*')
            new.right_side.add('C')
            new.right_side.add('D')

        return new

    def is_applicable(self, n):
        """ Is operator n applicable? Are there requested people on the operator's side of bridge? """
        if (n == 1):
            # A <-
            return 'A' in self.right_side and '*' in self.right_side
        elif (n == 2):
            # B <-
            return 'B' in self.right_side and '*' in self.right_side
        elif (n == 3):
            # C <-
            return 'C' in self.right_side and '*' in self.right_side
        elif (n == 4):
            # D <-
            return 'D' in self.right_side and '*' in self.right_side
        elif (n == 5):
            # AB ->
            return 'A' in self.left_side and 'B' in self.left_side and '*' in self.left_side
        elif (n == 6):
            # AC ->
            return 'A' in self.left_side and 'C' in self.left_side and '*' in self.left_side
        elif (n == 7):
            # AD ->
            return 'A' in self.left_side and 'D' in self.left_side and '*' in self.left_side
        elif (n == 8):
            # BC ->
            return 'B' in self.left_side and 'C' in self.left_side and '*' in self.left_side
        elif (n == 9):
            # BD ->
            return 'B' in self.left_side and 'D' in self.left_side and '*' in self.left_side
        elif (n == 10):
            # CD ->
            return 'C' in self.left_side and 'D' in self.left_side and '*' in self.left_side
        else:
            return False

def goal_node(state):
    """ Returns True if state is a goal state => all items are on the right side of the bridge. """
    return {'A', 'B', 'C', 'D', '*'} == state.right_side

def expand(state):
    """ With increasing index from 1 to 10 applies operators to the state and returns the list of successors """
    expanded = []

    for idx in range(1, 11):
        if state.is_applicable(idx):
            new = state.operator(idx)
            expanded.append(new)
    return expanded

def extract_min_price(OPEN):
    """ Returns the first state with the lowest price from the OPEN """
    minimum = min(OPEN, key=lambda state: state.price)
    OPEN.remove(minimum)
    return minimum

def print_solution(goal_state):
    """ Prints steps to the goal state """
    print("\n\n")
    seq = []
    state = goal_state
    while state:
        seq.append(state)
        state = state.predecessor
    seq.reverse()

    idx = 0
    for item in seq:
        print("{}: {}".format(idx, item))
        idx += 1

def leave_only_best(lst):
    """ If there are multiple instances of same state (left and right side are the same, price can be different), leave only the one with the lowest price that is closes to the start of the list """
    for item1 in lst:
        for item2 in lst:
            if item1.equals(item2):
                # there are states with the same left and right side (price can be different) => leave only the one with better price
                if item1.price < item2.price:
                    lst.remove(item2)
                elif item1.price > item2.price:
                    lst.remove(item1)
                else:
                    # if price is the same => leave the one that is closer to the start of the array (with the lower index)
                    if lst.index(item1) < lst.index(item2):
                        lst.remove(item2)
                    elif lst.index(item1) > lst.index(item2):
                        lst.remove(item1)

def print_list(name, lst, step):
    if (name == "Open"):
        print("Step: " + str(step))
    print(name + ":")
    for idx in range(len(lst)):
        print(lst[idx], end='\t')
        if (idx % 5 == 4):
            print("")
    print("\n")

found = False

# all people are on the left side of the bridge
starting_state = State({'A', 'B', 'C', 'D', '*'}, set(), 0, None)

OPEN = []
CLOSED = []
OPEN.append(starting_state)

step = 0
while OPEN:
    print_list("Open", OPEN, step)
    print_list("Closed", CLOSED, step)

    node = extract_min_price(OPEN)
    
    if goal_node(node):
        found = True
        break

    successors = expand(node)

    for successor in successors:
        if not (successor.in_list(CLOSED)):
            OPEN.append(successor)
            leave_only_best(OPEN)

    CLOSED.append(node)
    step += 1

if found:
    print_solution(node)
else:
    print("No solution")

