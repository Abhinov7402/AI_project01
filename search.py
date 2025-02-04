# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # To initialize the stack which acts as fringe
    stack = util.Stack()
    # To initialize the visited set to keep track of visited states
    visited = set()
    # To initialize the path to keep track of the path from the start state to the current state
    path = []
    # To push the start state into the stack with an empty path list as the path from the start state until the start state is empty 
    stack.push((problem.getStartState(), []))
    # To loop until the stack is empty (Last In First Out) 
    while not stack.isEmpty():
        # To pop the state and path from the stack to get the current state and path
        state, path = stack.pop()
        # To check if the state is the goal state so that the path can be returned 
        if problem.isGoalState(state):
            return path
        # To check if the state is visited so that the state can be skipped
        if state in visited:
            continue
        # To add the state to the visited set so that the state is not visited again
        visited.add(state)
        # To get the successors of the state 
        successors = problem.getSuccessors(state)
        # To loop through the successors 
        for successor in successors:
            # To get the successor state, action, and cost 
            successor_state, action, cost = successor
            # To push the successor state and path into the stack 
            stack.push((successor_state, path + [action]))
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # To initialize the queue which acts as fringe 
    queue = util.Queue()
    # To initialize the visited set to keep track of visited states 
    visited = set()
    # To initialize the path to keep track of the path from the start state to the current state 
    path = []
    # To push the start state into the queue with an empty path list as the path from the start state until the start state is empty
    queue.push((problem.getStartState(), []))
    # To loop until the queue is empty (First In First Out)
    while not queue.isEmpty():
        # To pop the state and path from the queue to get the current state and path
        state, path = queue.pop()
        # To check if the state is the goal state so that the path can be returned
        if problem.isGoalState(state):
            return path
        # To check if the state is visited so that the state can be skipped
        if state in visited:
            continue
        # To add the state to the visited set so that the state is not visited again
        visited.add(state)
        # To get the successors of the state 
        successors = problem.getSuccessors(state)
        # To loop through the successors 
        for successor in successors:
            # To get the successor state, action, and cost 
            successor_state, action, cost = successor
            # To push the successor state and path into the queue 
            queue.push((successor_state, path + [action]))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # To initialize the priority queue to keep track of the states with the least total cost
    priority_queue = util.PriorityQueue()
    # To initialize the visited set to keep track of visited states 
    visited = set()
    # To initialize the path to keep track of the path from the start state to the current state 
    path = []
    # To push the start state into the priority queue with an empty path list as the path from the start state until the start state is empty
    priority_queue.push((problem.getStartState(), []), 0)
    # To loop until the priority queue is empty 
    while not priority_queue.isEmpty():
        # To pop the state and path from the priority queue to get the current state and path
        state, path = priority_queue.pop()
        # To check if the state is the goal state so that the path can be returned
        if problem.isGoalState(state):
            return path
        # To check if the state is visited so that the state can be skipped 
        if state in visited:
            continue
        # To add the state to the visited set so that the state is not visited again 
        visited.add(state)
        # To get the successors of the state 
        successors = problem.getSuccessors(state)
        # To loop through the successors 
        for successor in successors:
            # To get the successor state, action, and cost 
            successor_state, action, cost = successor
            # To push the successor state and path into the priority queue along with the cost of the actions 
            priority_queue.push((successor_state, path + [action]), problem.getCostOfActions(path + [action]))
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    

    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # To initialize the priority queue to keep track of the states with the lowest combined cost and heuristic
    priority_queue = util.PriorityQueue()
    # To initialize the visited set to keep track of visited states 
    visited = set()
    # To initialize the path to keep track of the path from the start state to the current state
    path = []
    # To push the start state into the priority queue with an empty path list as the path from the start state until the start state is empty
    priority_queue.push((problem.getStartState(), []), 0)
    # To loop until the priority queue is empty 
    while not priority_queue.isEmpty():
        # To pop the state and path from the priority queue to get the current state and path
        state, path = priority_queue.pop()
        # To check if the state is the goal state so that the path can be returned
        if problem.isGoalState(state):
            return path
        # To check if the state is visited so that the state can be skipped
        if state in visited:
            continue
        # To add the state to the visited set so that the state is not visited again
        visited.add(state)
        # To get the successors of the state 
        successors = problem.getSuccessors(state)
        # To loop through the successors 
        for successor in successors:
            # To get the successor state, action, and cost 
            successor_state, action, cost = successor
            # To push the successor state and path into the priority queue 
            priority_queue.push((successor_state, path + [action]), problem.getCostOfActions(path + [action]) + heuristic(successor_state, problem))
    return []

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
