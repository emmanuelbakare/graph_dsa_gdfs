from  graph_algol import iGraph, make_diag, make_dfs_diag
from utilities import PrintColor as color, heading 
import os, msvcrt


 
# this get input from users and manage validation

def disconnect_route_interface():
    while True:
        print()
        nFrom=input("Enter Start Node Value: ")  
        if len(nFrom.strip())==0:
            print('should exit')
            return False
        nTo=input("Enter End Node Value: ") 
        
        graph.disconnect_route(nFrom,nTo) 
        print(f"Route {nFrom} to {nTo} disconnected")

def delete_route_interface():
    while True:
        print()
        node_name=input("Enter Node to Remove: ")
        
        if len(node_name.strip())==0 or node_name=="exit()":
            return False
        
        graph.delete_graph_route(node_name)
        print(f'{node_name} completely deleted from the graph')

# CMD Interface for connecting two graph node together and add a weight (distance) to it    
def connect_graph():
    while True:
        print()
        nFrom=input("Enter Start Node Value: ")  
        if len(nFrom.strip())==0:
            print('should exit')
            return False
        nTo=input("Enter End Node Value: ")  
        nWeight=input("Enter The Weight In between ")  
        
        if type(nFrom) != type(nTo):
            print('Start and End Node must be same type')
            continue
        
         
            
        graph.connect(nFrom,nTo,nWeight)
    
# CMD interface menu for adding new nodes
def cmd_add_node():
        while True:
            node_name=input("Enter a Node Name: ")
            
            if len(node_name.strip())==0 or node_name=="exit()":
                return False
            node=graph.add_node(node_name)
            
# CMD interface for Depth First Search    
def dfs_interface():
    root=input("Enter Root Node (Where to start from): ")
    
    if len(root.strip())==0 or root=="exit()":
        return False
    
    #initialize dfs storages
    graph.dfs_path=[]
    graph.visited=set()
    graph.dfs(graph.graphdict(), root)
    make_dfs_diag(graph.dfs_path)




# Main Menu for Command Line (CMD) Interface
def menu_interface():
        actions=['Add Nodes','Print All Nodes','Connect Nodes',
                 'Show Connections','Disconnect Nodes','Delete Node',
                 'Show Diagram','Depth First Search',
                 'Exit']
        
        while True:
            os.system('cls')
            heading("Main Menu")
            for num, action in enumerate(actions,1):
                print(num, action)
           
            try:
                action = int(input("What do you want to do (Enter Number): "))
            except:
                print()
                color.red("YOU MUST ENTER A NUMBER")
                print()
                print("Press any key to continue")
                msvcrt.getch() # this pulse the program until a key is pressed
            
            match action:
                case 1:
                    heading("Generate Node")
                    cmd_add_node()
                case 2:
                    heading("Pring All Nodes")
                    print(graph.all_nodes())
                    color.green('press any key to continue')
                    msvcrt.getch()
                case 3:
                    heading("CONNECT NODES TOGETHER")
                    connect_graph()
                case 4:
                    heading("Show Connected Nodes")
                    graph.graphdict(stringify=True)
                    color.green('press any key to continue')
                    msvcrt.getch()
                case 5:
                    heading("Disconnect Routes")
                    disconnect_route_interface()
                case 6:
                    heading("Delete Graph Route/Node")
                    delete_route_interface()
                case 7:
                    heading("Show Graph Diagram")
                    print('Brows output at file:///C:/env-graphdsa/graphdsa/templates/diagrams/nodeshow.html')
                    make_diag(graph.graphdict())
                    color.green('press any key to continue')
                    msvcrt.getch()
                case 8:
                    heading("Depth First Search")
                    print('Brows output at file:///C:/env-graphdsa/graphdsa/templates/diagrams/dfs_show.html')
                    dfs_interface()
                    color.green('press any key to continue')
                    msvcrt.getch()
              
                case 9:
                    print("Exiting program...")
                    return False
                case _:
                    
                    print("******* YOUR INPUT IS INVALID******")
                    
                    
           
        
         

graph=iGraph()
graph.connect("Lagos", "Abia",5983)
graph.connect("Lagos", "Anambra",1000)
graph.connect("Lagos", "Kano",1230)
graph.connect("Rivers","Lagos",1500)
graph.connect("Rivers","Abia",2900)
graph.connect("Sokoto","Lagos",170)
graph.connect("Bayelsa", "Abia",2020)
graph.connect("Rivers", "Anambra",2020)
graph.connect("Abia", "Kaduna",1010)
graph.connect("Bayelsa", "Kano",2020)
graph.connect("Abuja", "Anambra",2020)
graph.connect("Abuja", "Lagos",7620)
graph.connect("Abuja", "Nasarawa",9806)
graph.connect("Dutse Alhaji", "Anambra",906)
graph.connect("Dutse Alhaji", "Kaduna",906)
graph.connect("Sokoto", "Lokoja",900)
graph.connect("Lokoja", "Nasarawa",1900)
graph.connect("Lokoja", "Minna",1900)
menu_interface()
# connect_graph()
# get_input("What are you selling? ", int)