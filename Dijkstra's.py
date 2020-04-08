import queue

class Vertex:

    def __init__(self, ID):
        self.ID = ID
        self.pathDict = {}
    
    # path dictionary's
    # key store its nodeID
    # value store its weight
    def addPath(self, pathID, weight = 0):
        self.pathDict[pathID] = weight
    
    def getID(self):
        return self.ID

    def getWeight(self, pathID):
        return self.pathDict[pathID]

class Graph:

    def __init__(self):
        self.verticesDict = {}
        self.numOfVerticies = 0

    def addVertex(self, ID):
        self.numOfVerticies += 1
        newVertex = Vertex(ID)
        self.verticesDict[ID] = newVertex
        return newVertex

    def getVertex(self, ID):
        if ID in self.verticesDict:
            return self.verticesDict[ID]
        else:
            return None
    
    def addPath(self, fr, to, weight = 0):
        if fr not in self.verticesDict:
            print("from", fr, "does not exist")
            return
        if to not in self.verticesDict:
            print("to", to,"does not exist")
            return
        
        self.verticesDict[fr].addPath(to, weight)
    
    def getVertexCount(self):
        return self.numOfVerticies

def dijkstra(graph, numOfNodes, source):

    visited = [False]*numOfNodes

    dist = [2147480000]*numOfNodes
    dist[source] = 0

    pq = queue.PriorityQueue()
    pq.put((source, 0))

    while pq.qsize() > 0:
        vertex, minValue = pq.get()
        visited[vertex] = True
        
        for vertexID in graph.verticesDict:
            for pathID in graph.verticesDict[vertexID].pathDict:
                if visited[pathID]: continue
                newDist = dist[vertexID] + graph.getVertex(vertexID).getWeight(pathID)
                if newDist < dist[pathID]:
                    dist[pathID] = newDist
                    pq.put((pathID, newDist))

    for i in range(numOfNodes):
        print("from",source,"to",i,"shortest path is",dist[i])

    return dist


if __name__ == "__main__":
    graph = Graph()

    for i in range(5):
        graph.addVertex(i)

    graph.addPath(0, 1, 4)
    graph.addPath(0, 2, 1)

    graph.addPath(1, 3, 1)

    graph.addPath(2, 1, 2)
    graph.addPath(2, 3, 5)

    graph.addPath(3, 4, 3)

    for vertexID in graph.verticesDict:
        for pathID in graph.verticesDict[vertexID].pathDict:
            print(vertexID, pathID, end=" ")
            print(graph.getVertex(vertexID).getWeight(pathID))
    
    dijkstra(graph, graph.numOfVerticies, 0)
