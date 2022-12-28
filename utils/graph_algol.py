from pyvis.network import Network
import os
# Node Class
class iVertex:   #Graph Node
    
    def __init__(self,name):
        self.name=name 
        self.adjacents={}
        
    def add_adjacents(self, node, weight=0):
        if node not in self.adjacents.values():
            self.adjacents[node]=weight 
            
    # def add_node(self, name):
    #     return iVertex(name)
    
    def __str__(self):
        
        return f"{self.name} connects to {[node.name for node in self.adjacents]}"

#Graph Class - for making and manipulting graphs from nodes
class iGraph:
    
    def __init__(self):
        self.num=0
        self.graphnodes={}
        self.dfs_path=[]
        self.visited=set()
        
    def add_node(self,name):
        node=iVertex(name)
        self.graphnodes[name]=node
        return node
    
    #delete an item from Lagos
    def disconnect_route(self, nfrom, nto):
        # get the from nodes and its adjacent nodes (to nodes) e.g. a ->{b,c,d}
        from_route=self.graphnodes.get(nfrom)
        if from_route:
            from_adjs=from_route.adjacents

         
        # get the to node and pop out the to node from the from nodes adjacent nodes above e.g. remove b from {b,c,d}
        to_route=self.graphnodes.get(nto)
        if to_route in from_adjs:
            from_adjs.pop(to_route)

    def delete_graph_route(self,route):
            
                # delete all occurent of route in graph
            for from_route in self.graphnodes:
    #             print(f'FROM {from_route} ---> {route} graph.disconnect_route({from_route}, {route}) ')
                self.disconnect_route(from_route, route)
            
            # delete the 
            if route in self.graphnodes:
                route_node=self.graphnodes.get(route)
    #             print('ROUTE TO DELETE', route_node)
                # del route_node
                self.graphnodes.pop(route)
                
                



    
            
    def connect(self, nFrom, nTo, weight=0):
        if nFrom not in self.graphnodes:
            self.add_node(nFrom)
        if nTo not in self.graphnodes:
            self.add_node(nTo)
        self.graphnodes[nFrom].adjacents[self.graphnodes[nTo]]= weight
        
        
    def all_nodes(self):
        return [obj for obj in self.graphnodes]
    
    def node(self, name):
        return  [obj.name for obj in self.graphnodes[name].adjacents]
    
    
    # uses self.graphnodes dictionary containing objects to convert 
    # result to dictionary:list or dictionary:set  or string dictionary result
    def graphdict(self, use_set=True, stringify=False):
        # return the graphical representation of the node
        if use_set:
            graph_path = { key:set([i.name for i in node.adjacents]) for key,node in self.graphnodes.items()}
        else:
            graph_path = { key:[i.name for i in node.adjacents] for key,node in self.graphnodes.items()}
        
        if stringify:
            for key,value in graph_path.items():
                print(key,":",value)
             
        else:
            return graph_path

    
    def weights(self, name):
        print( f"{10} connects to {self.node(name)}")
        print("*"*30)
    
    def dfs(self,graph, root):
        if root not in self.visited:
            self.dfs_path.append(root)
            self.visited.add(root)
            if graph.get(root):
                for neigbhour in graph[root]:
                    self.dfs(graph,neigbhour)
            else:
                print()
                print("THIS NODE DOESN'T EXIST")


# draw a graph diagram
def make_diag(graphdict):
    net= Network(directed=True)
    allnodes=set()
    for key,connected in graphdict.items():
        net.add_node(key, label=key)
        allnodes.add(key)
        for cnode in connected:
            
            if cnode not in allnodes:
                net.add_node(cnode, label=cnode)
                allnodes.add(cnode)
            net.add_edge(key, cnode, weight=20)
    
    net.show('templates/diagrams/nodeshow.html')
    
#Convert a List generated from DFS routes to a diagra       
def make_dfs_diag(dfs):
    
    net2= Network(directed=True)
    total_path=len(dfs)
    net2.add_nodes(dfs)
    for idx in range(total_path):
        try:
            net2.add_edge(dfs[idx],dfs[idx+1])
        except:
            break
    net2.show('templates/diagrams/dfs_show.html') 

  
    

# graph=iGraph()

 
# graph.connect("Lagos", "Abia",5983)
# graph.connect("Lagos", "Anambra",1000)
# graph.connect("Lagos", "Kano",1230)
# graph.connect("Rivers","Lagos",1500)
# graph.connect("Rivers","Abia",2900)
# graph.connect("Sokoto","Lagos",170)
# graph.connect("Bayelsa", "Abia",2020)
# graph.connect("Rivers", "Anambra",2020)
# graph.connect("Abia", "Kaduna",1010)
# graph.connect("Bayelsa", "Kano",2020)
# graph.connect("AbiAA", "Anambra",2020)
 

# os.system('cls')
# print('GRAPHNODES: ',graph.graphnodes) 
# print()
# print('GRAPH DICTS: ',graph.graphdict(stringify=True)) 
# print()
# print('Delete Abia from Lagos route')
# graph.disconnect_route('Lagos','Abia')
# # graph.disconnect_route('Rivers','Lagos')
# print('GRAPH DICTS: ',graph.graphdict(stringify=True)) 
# print()
# print('Remove Anambra Completely from the Graph')
# graph.delete_graph_route("Anambra")
# print('GRAPH DICTS: ',graph.graphdict(stringify=True)) 



# graph

# graph.cmd_graph_input()
# print("================= OUTPUT =======================")
# print(graph.all_nodes())

# print(graph.graphdict())
# print(graph.graphdict(stringify=True))
# print(graph.all_nodes())
# print("================= outputs 2 =====================")
# print(graph.all_nodes())
# print(graph.graphdict())
# print('GRAPH NODE',graph.graphnodes)
# print("*"*30) 

#get a node and all its connections
# print(graph.graphnodes["Rivers"])

 





            
graph1={
    'A':set(['B','C','D']),
    'B':set(['E','F']),
    'C':set(),
    'D':set(['G','H']),
    'E':set(),
    'F':set(['I','J']),
    'G':set(['K']),
    'H':set(),
    'I':set(),
    'J':set(),
    'K':set(),
}
    
# graph2={
#     'A': set(['B','C']),
#     'B': set(['A','C','D']),
#     'C': set(['A','F']),
#     'D': set(['B']),
#     'E': set(['B','F']),
#     'F': set(['C','E']),
# }
# graph3={
#     'A':['B','C','D'],
#     'B':['E'],
#     'C':['D','E'],
#     'D':[],
#     'E':[],
# }


 

# Depth First Search Algorithm

# visited=set()
# dfs_path=[]
# def dfs2(visited, graph, root):
#     if root not in visited:
#         dfs_path.append(root)
#         visited.add(root)
    
#         for neigbhour in graph[root]:
#             dfs2(visited,graph,neigbhour)
    # return dfs_path



      
    
# graph_to_print= graph.graphdict()

# dfs2(visited, graph_to_print, 'A') 
# graph.dfs22(graph_to_print, 'Lagos') 
# print()
# print('DFS PATH -->',dfs_path)      
# print('DFS PATH -->',graph.dfs_path)      
# print('DFS PATH -->',dfs2(visited, graph_to_print, 'A'))      
   
# make_diag(graph_to_print)  
# make_dfs_diag(dfs_path)  
# print(graph.graphdict())            

    
 
    
    
 
                  

# make_diag(graph3)  
# # print(graph.graphdict())  

# print()
# # Depth First Search
# print("*"*40)


# dfs2(visited, graph3, 'A') 
# print()
# print('DFS PATH',dfs_path)   
        
    

                          
                
            

 