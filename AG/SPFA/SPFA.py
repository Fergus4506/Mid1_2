# queue<int> q;
# 源点s入队;
# while(队列非空){
#     取出队首元素;
#     for(u的所有邻接边u->v){
#         if(d[u]+dis<d[v])
#         {
#             d[v]=d[u]+dis;
#             if(v当前不在队列)
#             {
#                 v入队；
#                 if(v入队次数大于n-1){
#                     说明有可达负环,return;
#                 }
#             }
#         }
#     }
# }

import queue

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
 
    # 从这个顶点添加一个连接到另一个
    def add_neighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
 
    def __str__(self):
        return str(self.id) + ' connectedTo ' + str([x for x in self.connectedTo])
 
    # 返回邻接表中的所有的项点
    def get_connections(self):
        return self.connectedTo.keys()
 
    def get_id(self):
        return self.id
 
    # 返回从这个顶点到作为参数顶点的边的权重
    def get_weight(self, nbr):
        return self.connectedTo[nbr]
 
 
class Graph:
    def __init__(self, num=None):
        self.vertList = {}
        self.numVertices = 0
        if num is not None:
            [self.add_vertex(i+1) for i in range(num)]
 
    def add_vertex(self, key):
        self.numVertices += 1
        v = Vertex(key)
        self.vertList[key] = v
        return v
 
    def get_vertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
 
    def __contains__(self, item):
        return item in self.vertList
 
    def add_edge(self, u, v, w = float('inf')):
        if u not in self.vertList:
            self.add_vertex(u)
        if v not in self.vertList:
            self.add_vertex(v)
        self.vertList[u].add_neighbor(self.vertList[v].get_id(), w)
 
    def get_vertices(self):
        return self.vertList.keys()
 
    def __iter__(self):
        return iter(self.vertList.values())
    
def spfa(graph, src):
    if graph is None:
        return None
    dis = [float('inf') if i != src else 0 for i in range(graph.numVertices + 1)]
    # 表示结点i是否在队列中
    book = [False for i in range(graph.numVertices + 1)]
    que = queue.Queue()
    que.put(graph.get_vertex(src))
    while not que.empty():
        u = que.get()
        u_id = u.get_id()
        con = [nei for nei in u.get_connections()]
        for c in con:
            if dis[c] > dis[u_id] + u.get_weight(c):
                dis[c] = dis[u_id] + u.get_weight(c)
 
                if not book[c]:
                    # 如果当前访问结点没有在队列中，就入队
                    que.put(graph.get_vertex(c))
                    book[c] = True
 
        # 出队
        book[u_id] = False
 
    return dis[1:]
 
 
if __name__ == '__main__':
    graph = Graph(5)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 5, 10)
    graph.add_edge(2, 3, 3)
    graph.add_edge(2, 5, 7)
    graph.add_edge(3, 4, 4)
    graph.add_edge(4, 5, 5)
    graph.add_edge(5, 3, 6)
 
    print(spfa(graph, 1))