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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    closed = []
    fringe = [problem.getStartState()]
    routes = [[]]
    while len(fringe) != 0:
        node = fringe[0]
        path = routes[0]
        fringe = fringe[1:]
        routes = routes[1:]
        if problem.isGoalState(node):
            return path
        if not node in closed:
            closed.append(node)
            for child in problem.getSuccessors(node):
                fringe = [child[0]] + fringe
                routes = [path + [child[1]]] + routes
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    closed = []
    fringe = [problem.getStartState()]
    routes = [[]]
    while len(fringe) != 0:
        node = fringe[0]
        path = routes[0]
        fringe = fringe[1:]
        routes = routes[1:]
        if problem.isGoalState(node):
            return path
        if not node in closed:
            closed.append(node)
            for child in problem.getSuccessors(node):
                fringe = fringe + [child[0]]
                routes = routes + [path + [child[1]]]
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    closed = []
    fringe, routes, costs = util.PriorityQueue(), util.PriorityQueue(), util.PriorityQueue()
    fringe.push(problem.getStartState(), 0)
    routes.push([], 0)
    costs.push(0, 0)
    while not fringe.isEmpty():
        node, path, cost = fringe.pop(), routes.pop(), costs.pop()
        if problem.isGoalState(node):
            return path
        if not node in closed:
            closed.append(node)
            for child in problem.getSuccessors(node):
                costs.push(cost + child[2], cost + child[2])
                fringe.push(child[0], cost + child[2])
                routes.push(path + [child[1]], cost + child[2])
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
