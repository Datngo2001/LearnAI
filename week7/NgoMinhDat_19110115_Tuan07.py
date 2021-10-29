# The following code implements A* search to solve the path finding problem in a 10x10 maze.
# However, it has some BUGS leading to infinite loops and nonoptimal solutions!
'''
DEBUG the code to make it work with the maze map given in the exercise.
Hint: You might want to print the current_node and the closed_list (explored set) for each loop
      to check if the current_node is in the closed_list.
'''


from PySide2 import QtWidgets
from NgoMinhDat_19110115_Tuan07_GUI import Ui_MainWindow
from PySide2.QtWidgets import *


class Node():
    """A node class for A* search"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # PATH-COST to the node
        self.h = 0  # heuristic to the goal: straight-line distance hueristic
        self.f = 0  # evaluation function f(n) = g(n) + h(n)

    def __eq__(self, other):
        return self.position == other.position


''' DEBUG THE FOLLOWING FUNCTION '''


def astar(maze, start, end):
    """Returns a list of tuples as a solution from "start" to "end" state in "maze" map using A* search.
    See lecture slide for the A* algorithm."""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []    # frontier queue
    closed_list = []  # explored set

    # Add the start node
    open_list.append(start_node)

    loop = 0
    f = open("log.txt", "a")

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Check if we found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Expansion: Generate children
        children = []
        # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            isInClosed = False
            for closed_child in closed_list:
                if child is closed_child:
                    isInClose = True
                    break
            if(isInClosed):
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **
                       2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            isInOpenButHigherPathCost = False
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    isInOpenButHigherPathCost = True
                    break
            if(isInOpenButHigherPathCost):
                continue

            # Add the child to the open list
            open_list.append(child)

        f.write("\nLoop" + str(loop) + "=============================\n")
        f.write("\nExpand:" + str(current_node.position))
        f.write("\nProntier:\n")
        for prontier in open_list:
            f.write(str(prontier.position) +
                    ": h=" + str(prontier.h) + "\n")

        loop = loop + 1

    f.close()


def findBtn(ui, row, col):
    for btn in ui.btnSet:
        if(btn[0] == "btn_" + str(row) + str(col)):
            return QPushButton(btn[1])


if __name__ == '__main__':

    ''' CHANGE THE BELOW VARIABLE TO REFLECT TO THE MAZE MAP IN THE EXERCISE '''
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],  # 1: obstacle position
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

    start = (0, 0)
    goal = (8, 9)

    path = astar(maze, start, goal)
    # print(path)

    # Prepare UI
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    for row in range(0, len(maze)):
        for col in range(0, len(maze)):
            btn = findBtn(ui, row, col)
            if(maze[row][col] == 1):
                btn.setStyleSheet(u"background-color: rgb(0, 0, 0);")

    for step in path:
        btn = findBtn(ui, step[0], step[1])
        btn.setStyleSheet(u"background-color: rgb(51, 153, 255);")

    btn = findBtn(ui, start[0], start[1])
    btn.setStyleSheet(u"background-color: rgb(85, 255, 127);")
    btn = findBtn(ui, goal[0], goal[1])
    btn.setStyleSheet(u"background-color: rgb(255, 0, 0);")

    MainWindow.show()
    sys.exit(app.exec_())
