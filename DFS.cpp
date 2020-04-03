#include <iostream>
#include <list>

using namespace std;

class Graph
{
    private:
    // number of vertices
    int _vertices; 

    // pointer to adjacency list
    list<int> *adjacent;

    // DFS recursive helper function
    void _DFSHelper(int source, bool *visited);

    public:

    // constructor prototype
    Graph(int vertices);

    // method to add an edge
    void addEdge(int v, int w);

    // method for BFS traversal given a source "s"
    void DFS(int source);
};

Graph::Graph(int vertices)
{
    _vertices = vertices;
    adjacent = new list<int>[vertices];
}

// method to add edges
// v is vertex and w is it's adjacent
void Graph::addEdge(int v, int w)
{
    adjacent[v].push_back(w);
}

// this will visit all the nodes
void Graph::_DFSHelper(int s, bool *visited)
{
    // mark the current node as visited
    cout<<"Visiting node "<< s << endl;
    visited[s] = true;

    // go through all the adjacency list
    for (auto i = adjacent[s].begin(); i != adjacent[s].end(); i++) // (*adjacent) == adjacent[s]
    {
        // if not visited, travel through that vertex
        if(!visited[*i])
        {
            cout<<"going to vertex "<<*i<<" from vertex "<< s << endl;
            _DFSHelper(*i, visited);
        }
    }
    
}

// perform DFS given a starting vertex
void Graph::DFS(int s)
{
    // start with all vertices not visited
    bool *visited = new bool[_vertices];
    for (int i = 0; i < _vertices; i++)
    {
        visited[i] = false;
    }

    // beginning of recursive call
    _DFSHelper(s, visited);
}

int main()
{
    // create new graph
    Graph g(6);

    // create some edges and vertices
    // connections for vertex 0
    g.addEdge(0, 1);
    g.addEdge(0, 2);

    // connections for vertex 1
    g.addEdge(1, 0);
    g.addEdge(1, 3);
    g.addEdge(1, 4);

    // connections for vertex 2
    g.addEdge(2, 0);   
    g.addEdge(2, 4);

    // connections for vertex 3
    g.addEdge(3, 1);
    g.addEdge(3, 4);
    g.addEdge(3, 5);

    // connections for vertex 4
    g.addEdge(4, 1);
    g.addEdge(4, 2);
    g.addEdge(4, 3);
    g.addEdge(4, 5);

    //connections for vertex 5
    g.addEdge(5, 3);
    g.addEdge(5, 4);


    //perform dfs
    g.DFS(0);
    return 0;
}