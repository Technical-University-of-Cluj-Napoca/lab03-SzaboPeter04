from utils import *
from collections import deque
from queue import PriorityQueue
from grid import Grid
from spot import Spot

def _pos(s:Spot)->tuple[int,int]:
    if hasattr(s,"get_pos"):
        return s.get_pos()
    return (s.row,s.col)

def _reconstruct_path(came_from:dict[tuple[int,int],tuple[int, int]],current_rc:tuple[int,int],grid:Grid,draw:callable)->None:
    while current_rc in came_from:
        current_rc=came_from[current_rc]
        r,c=current_rc
        grid.grid[r][c].make_path()
        draw()

def bfs(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    """
    Breadth-First Search (BFS) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    start_r,start_c=_pos(start)
    end_r,end_c=_pos(end)
    q=deque([(start_r,start_c)])
    visited:set[tuple[int,int]]={(start_r,start_c)}
    parent:dict[tuple[int,int],tuple[int,int]]={}
    start.make_open()
    while q:
        pygame.event.pump()
        r,c=q.popleft()
        current=grid.grid[r][c]
        if current==end:
            _reconstruct_path(parent,(end_r,end_c),grid,draw)
            end.make_end()
            start.make_start()
            return True
        for neighbor in current.neighbors:
            if not(neighbor.is_barrier()):
                neigh_r,neigh_c=_pos(neighbor)
                if (neigh_r,neigh_c) not in visited:
                    visited.add((neigh_r,neigh_c))
                    parent[(neigh_r,neigh_c)]=(r,c)
                    neighbor.make_open()
                    q.append((neigh_r,neigh_c))
        if current not in (start,end):
            current.make_closed()
        draw()
    return False

def dfs(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    """
    Depdth-First Search (DFS) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    start_r,start_c=_pos(start)
    end_r,end_c=_pos(end)
    q=deque([(start_r,start_c)])
    stack:list[tuple[int,int]]=[(start_r,start_c)]
    visited:set[tuple[int,int]]={(start_r,start_c)}
    parent:dict[tuple[int,int],tuple[int,int]]={}
    start.make_open()
    while stack:
        pygame.event.pump()
        r,c=stack.pop()
        current=grid.grid[r][c]
        if current==end:
            _reconstruct_path(parent,(end_r,end_c),grid,draw)
            end.make_end()
            start.make_start()
            return True
        if current not in (start,end):
            current.make_closed()
        for neighbor in current.neighbors:
            if not(neighbor.is_barrier()):
                neigh_r,neigh_c=_pos(neighbor)
                if (neigh_r,neigh_c) not in visited:
                    visited.add((neigh_r,neigh_c))
                    parent[(neigh_r,neigh_c)]=(r,c)
                    neighbor.make_open()
                    stack.append((neigh_r,neigh_c))
        draw()
    return False

def h_manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    """
    Heuristic function for A* algorithm: uses the Manhattan distance between two points.
    Args:
        p1 (tuple[int, int]): The first point (x1, y1).
        p2 (tuple[int, int]): The second point (x2, y2).
    Returns:
        float: The Manhattan distance between p1 and p2.
    """
    pass

def h_euclidian_distance(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    """
    Heuristic function for A* algorithm: uses the Euclidian distance between two points.
    Args:
        p1 (tuple[int, int]): The first point (x1, y1).
        p2 (tuple[int, int]): The second point (x2, y2).
    Returns:
        float: The Manhattan distance between p1 and p2.
    """
    pass


def astar(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    """
    A* Pathfinding Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
   # neiig

# and the others algorithms...
# ▢ Depth-Limited Search (DLS)
# ▢ Uninformed Cost Search (UCS)
# ▢ Greedy Search
# ▢ Iterative Deepening Search/Iterative Deepening Depth-First Search (IDS/IDDFS)
# ▢ Iterative Deepening A* (IDA)
# Assume that each edge (graph weight) equalss