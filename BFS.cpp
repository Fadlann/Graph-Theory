#include<iostream>
#include<list>
#include<queue>

using namespace std;

class Graph
{
    private:
    int _vertices;
    list<int>* _adjacent;
    void _DFS(int source);

    public:
    Graph(int vertices);
    void BFS(int source);
    void addEdge(int v, int w);
};

Graph::Graph(int vertices)
{
    _vertices = vertices;
    // empty array of list with vertices elements
    _adjacent = new list<int>[vertices];
}

void Graph::addEdge(int v, int w)
{
    _adjacent[v].push_back(w);
}

void Graph::BFS(int source)
{
    queue<int> checkQueue;
    bool visited[_vertices];
    for (int i = 0; i < _vertices; i++)
    {
        visited[i] = false;
    }
    
    visited[source] = true;
    checkQueue.push(source);

    while(checkQueue.size() > 0)
    {
        source = checkQueue.front();
        checkQueue.pop();

        cout<<"checking the adjacency of vertex "<<source<<endl;
        for(auto i = _adjacent[source].begin(); i != _adjacent[source].end(); i++)
        {
            if(!visited[*i])
            {
                cout<<"visiting and enqueueing "<<*i<<" from "<<source<<endl;
                visited[*i] = true;
                checkQueue.push(*i);
            }
        }
    }
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


    //perform bfs
    g.BFS(2);

    return 0;
    return 0;
}