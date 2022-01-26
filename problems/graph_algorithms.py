#--- YouTube Video 
# ----- https://youtu.be/tWVWeAqZ0WU




import json

class Graph:
    
    def __init__(self):
        self.nodes = {}
        
    def __repr__(self):
        return json.dumps(self.nodes)
        
    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.setdefault(node,[])
        return self
    
    def addEdge(self, node, adjacentNode):
        if adjacentNode not in self.nodes:
            self.addNode(adjacentNode)
        self.nodes[node].append(adjacentNode)
    
    def delNode(self, node, adjacentNodes = []):
        del self.nodes[node]
        
    def addEdges(self, node, adjacentNodes = []):
        self.addNode(node)
        for adjacentNode in adjacentNodes:
            self.addEdge(node, adjacentNode)
        return self
    
    def bfs(self, node):
        
        if node not in self.nodes:
            print("Unknown node")
            return None
        
        q = list()
        q.append(node)
        
        l= list()
        
        while q:
            n = q.pop(0)
            l.append(n)
            e = self.nodes[n]
            for a in e:
                q.append(a)
                
        return l    
    
    
    def dfsRec(self, node):

        print(node)
        for n in self.nodes[node]:
            self.dfsRec(n)
    
    
    def dfs(self, node):
        
        if node not in self.nodes:
            print("Unknown node")
            return None
        
        q = list()
        q.append(node)
        
        l= list()
        
        while q:
            n = q.pop()
            l.append(n)
            e = self.nodes[n]
            for a in e:
                q.append(a)
                
        return l
    
    
    def dRec(self, node):
        
        print(node)
        for a in self.nodes[node]:
            self.dRec(a)
            
            
    def hasPathBfs(self, src, des):
        
        l = [src]
        
        while l:
            s = l.pop(0)
            print(src)
            if (s == des):
                return True
            else:
                l.extend(self.nodes[s])
                
        return False

    def hasPathDfs(self, src, des):
        
        l = [src]
        
        while l:
            s = l.pop()
            print(src)
            if (s == des):
                return True
            else:
                l.extend(self.nodes[s])
                
        return False


    def hasPathBfs(self, src, des):
        
        visited = set()
        l = [src]
        while l:
            
            currentNode = l.pop(0)
            print(currentNode)
            
            if currentNode in visited:
                print("Visited", currentNode)
                continue
                
            if (currentNode == des):
                return True
            
            adjacentNodes = self.nodes[currentNode]
            l.extend(adjacentNodes)
            visited.add(currentNode)
            
        return False
            

    def hasPathRec(self, src, des, visited = set() ):
        
        print("checking1", src, visited)
        
        if (src == des):
            return True  
        
        if (src in visited):
            print("VISITED", src, visited)
            return False
        else:
            visited.add(src)
        
        for node in self.nodes[src]:
            if (self.hasPathRec(node, des, visited)):
                return True
        
        return False
    

# g [h,k]
# h [g]

# g,k
#   [h,k]
#     h,k
#       [g]
#         g,k
    
#     k,k
    
    
#     def edgesToGraph(self, edges, undirected = True):
        
#         for a, b in edges:
#             self.addNode(a)
#             self.addEdge(a,b)
#             if undirected:
#                 self.addEdge(b,a)
                
#         return self
    
    
    def edgeListtoAdjacencyList(self, edgeList, undirected = True):
        
        for edge in edgeList:
            a, b = edge
            if (a not in  self.nodes):
                self.nodes[a] = []
            if (b not in self.nodes):
                self.nodes[b] = []
            self.nodes[a].append(b)
            if (undirected):
                self.nodes[b].append(a)
            
    def bfs(self, node, visited = set()):
        l = [node]
        # visited = set()
        while l:
            currentNode = l.pop(0)
            if currentNode in visited:
                continue
            print(currentNode)
            visited.add(currentNode)
            adjacentNodes = self.nodes[currentNode]
            l.extend(adjacentNodes)
            
    def dfsIter(self, node, visited = set()):
        
        l = [node]
        while l:
            currentNode = l.pop()
            if currentNode not in visited:
                print(currentNode)
                l.extend(self.nodes[currentNode])
                visited.add(currentNode)
                
    def dfsRec(self, node, visited = set()):
        
        if (node not in visited):
            print(node)
            visited.add(node)
            for adjacent in self.nodes[node]:
                self.dfsRec(adjacent, visited)
                
            
    def countConnectComponents(self):
        
        count = 0
        visited = set()
        for node in self.nodes:
            if (node not in visited):
                print("countConnectComponents", node)
                # self.dfsIter(node, visited)
                self.dfsRec(node, visited)
                # self.bfs(node, visited)
                
                count += 1
            
        print(count)
        return count
        
    
    
    def bfs(self, node, visited = set()):
        
        m = float('-inf')
        l = [node]
        while l :
            currNode = l.pop(0)
            if currNode not in visited:
                m = max(currNode,m)
                visited.add(currNode)
                adjacentNodes = self.nodes[node] 
                l.extend(adjacentNodes)
        # print("inner", node, m)
        return m
            
        
        
    def getMax(self):
        
        visited = set()
        global m
        m = float('-inf')
        
        for node in self.nodes:
            if node not in visited:
                m = max(m,self.bfs(node, visited))
                # print(node, m)
                
        print(m)
        return(m)
    
    def getComponentCount(self, node, visited = set()):
        
        count = 0
        l = [node]
        
        while l:
            currNode = l.pop(0)
            if currNode not in visited:
                adjacentNodes = self.nodes[currNode]
                l.extend(adjacentNodes)
                visited.add(currNode)
                count +=1
                
        print("count for node", node, count)
        return count
    
    
    def getComponentCountRec(self, node, visited= set()):
        
        print(node)
        visited.add(node)
        count = 1
        for a in self.nodes[node]:
            if a not in visited:
                count += self.getComponentCount(a, visited)

        return count
        

    def getLargestComponentCount(self):
        
        largestComponentCount = 0
        visited = set()
        
        for node in self.nodes:
            if not node in visited:
                # largestComponentCount = max(largestComponentCount, self.getComponentCount(node, visited))
                largestComponentCount = max(largestComponentCount, self.getComponentCountRec(node, visited))
                
        print("largestComponentCount", largestComponentCount)
        return largestComponentCount

    def findShortestPath(self, src, des):
        
        visited = set()
        l = [(src,0)]
        while l:
            (currNode,count) = l.pop(0)
            if currNode not in visited:
                if currNode == des:
                    return count
                visited.add(currNode)
                adjacentNodes = self.nodes[currNode]
                for eachAdjacentNode in adjacentNodes:
                    l.append((eachAdjacentNode, count+1))
        return -1
        
        # 1 - 2- 3
        # |
        # 4   7
        # |   |
        # 5 - 6
        # |
        # 8
        
g = Graph()
# g.nodes = {
#     "f" : ["g","i"],
#     "g" : ["h"],
#     "h" : [],
#     "i" : ["g", "k"],
#     "j" : ["i"],
#     "k" : []
# }
# g.addNode(1).addNode(2).addNode(3).addNode(4).addNode(5).addNode(6).addNode(7)
# print(g.nodes)
# g.addEdges(1,[2,4]).addEdges(2,[3]).addEdges(4,[5]).addEdges(5,[6]).addEdges(6,[7])
# g.addEdges(5,[8])
# print(g.nodes)

# print(g.bfs(1))
# print(g.dfs(1))

# g.dfsRec("f")

# g.dRec("f")


# print(g.hasPathBfs("f","l"))
# print(g.hasPathDfs("f","i"))
# print(g.hasPathRec("f","l", set()))
# print(g.hasPathRec("f","k", set()))

# edges = [
#     ["i", "j"],
#     ["k", "i"],
#     ["m", "k"],
#     ["k", "l"],
#     ["o", "n"]
# ]
# g.edgeListtoAdjacencyList(edges)
# print(g)
# print(g.hasPathBfs("i","l"))



# g.nodes = {
#     3: [],
#     4: [6],
#     6: [4,5,7,8],
#     8: [6],
#     7: [6],
#     5: [6],
#     1: [2],
#     2: [1],
#     8: [10],
#     4: [10],
#     10: []
# }

# print(g)

# g.countConnectComponents()
# g.bfs(6)
# g.getMax()
# print(g.getComponentCount(6))
# g.getLargestComponentCount()
# print(g.findShortestPath(4,3))



grid = [
    ['W','L','W','W','L','W'],
    ['W','L','W','W','W','W'],
    ['W','W','W','W','L','W'],
    ['W','W','W','L','L','W'],
    ['L','W','W','W','L','L'],
    ['L','L','W','W','W','W']
]

grid = [
    ['W','L','W','W','L','W'],
    ['W','L','W','W','W','W'],
    ['W','W','W','W','L','W'],
    ['W','W','W','L','L','W'],
    ['L','W','W','W','L','L'],
    ['L','L','W','W','W','W']
]



# traverse through each cell ...
# initiated counter for total connected components
# if cell is water - ignore / move on
# if cell is Land & not Visited - Do a BFS Search for connected components
#    once the BFS search for connnected components is over, increment count of connected components by 1
# Mark the visited cell so that we do not loop infinitely or redo calculations
# return the count of connected components


def getAdjacentCells(grid, node):
    rowLen = len(grid)
    colLen = len(grid[0])
    (r,c) = node
    
    adjacentLandCells = []
    for possibleAdjacentCell in [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]:
        (row,col) = possibleAdjacentCell
        if (row >=0 and row<=rowLen-1 and col>=0 and col<=colLen-1):
            if (grid[row][col] == 'L'):
                adjacentLandCells.append((row,col))
    
    return adjacentLandCells
    
    
def bfs(grid, node, visited = set()):
    
    l = [node]
    
    while l:
        currNode = l.pop(0)
        if currNode not in visited:
            visited.add(currNode)
            print(currNode)
            l.extend(getAdjacentCells(grid, currNode))
    
def getIslandCount(grid):
    
    rowLen = len(grid)
    colLen = len(grid[0])
    
    countOfConnectedComponents = 0
    visited = set()
    
    for r in range(rowLen):
        for c in range(colLen):
            if grid[r][c] == 'L' and (r,c) not in visited:
                countOfConnectedComponents += 1
                bfs(grid, (r,c), visited)
                
    return countOfConnectedComponents
            
# print(getAdjacentCells(grid, (4,5)))
print(getIslandCount(grid))

