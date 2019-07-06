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

def depthFirstSearch(problem):
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
    from game import Directions
    from util import Stack
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    
    visited = [None] # list of states (each state is a position in this case)
    stack = Stack() # contains pairs. each pair's first elem is a list of actions. second elem is state
    stack.push([[], problem.getStartState()])

    while (not stack.isEmpty()):
        top = stack.pop() # this is the top of the stack
        actions = top[0]
        state = top[1]
        if (state not in visited):
            if problem.isGoalState(state):
                return actions    
            visited.append(state)           
            for child in problem.getSuccessors(state):               
                tempActions = actions[:]
                tempActions.append(child[1])
                stack.push([tempActions, child[0]])
    return None
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Queue
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    
    visited = [None] # list of states (each state is a position in this case)
    queue = Queue() # contains pairs. each pair's first elem is a list of actions. second elem is state
    queue.push([[], problem.getStartState()])


    while (not queue.isEmpty()):
        top = queue.pop() # this is the top of the stack
        #print("@@@@@TOP: ", top)
        actions = top[0]
        state = top[1]
        #print("@@@@@@STATE: ", state)
        
           # print("@@@@@@ENTERETED LOOP")
        if problem.isGoalState(state):
         #   print("@@@@ACTIONS: ", actions)
            return actions
        
        visited.append(state)
        
        for child in problem.getSuccessors(state): #returns (nextstate, actions, cost)
            childAction = child[1]
            childState = child[0]
            if (childState not in visited):
                visited.append(childState)
               # print ("@@@@@@STATE: ", child)
                #if (child[0] not in visited):
                tempActions = actions[:]
               # print("!!!!!!!TYPE ", type(tempActions))
                tempActions.append(childAction)
                queue.push([tempActions, child[0]])
    return None
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import PriorityQueue
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    
    visited = [None] # list of states (each state is a position in this case)
    pq = PriorityQueue() # contains pairs. each pair's first elem is a list of actions. second elem is state
    pq.push([[], problem.getStartState()], 0)


    while (not pq.isEmpty()):
        top = pq.pop() # this is the top of the stack
        actions = top[0]
        state = top[1]
        if (state not in visited):
            if problem.isGoalState(state):
                return actions
            
            visited.append(state)
            
            for child in problem.getSuccessors(state):           
                tempActions = actions[:]
                tempActions.append(child[1])
                costOfActions = problem.getCostOfActions(tempActions)
                pq.push([tempActions, child[0]], costOfActions)
    return None
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import PriorityQueue
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    
    visited = [None] # list of states (each state is a position in this case)
    pq = PriorityQueue() # contains pairs. each pair's first elem is a list of actions. second elem is state
    pq.push([[], problem.getStartState()], 0)

    while (not pq.isEmpty()):
        top = pq.pop() # this is the top of the stack
        actions = top[0]
        state = top[1]
        if (state not in visited):
            if problem.isGoalState(state):
                return actions
            
            visited.append(state)
            
            for child in problem.getSuccessors(state):
            
                tempActions = actions[:]
                tempActions.append(child[1])
                totalCostOfActions = problem.getCostOfActions(tempActions) + heuristic(child[0], problem)
                pq.push([tempActions, child[0]], totalCostOfActions)
    return None
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
