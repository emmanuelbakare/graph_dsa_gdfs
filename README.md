# Graph_DFS_DSA

#### Graph Algorithm Structure with graphical display and Database for storing Different Graph model

# Graph Data Structure Installation Instruction

#### Install Python  -  Watch the Video Below


[![Install Python](http://i3.ytimg.com/vi/wHr8Oas_9Vk/hqdefault.jpg)]
(https://www.youtube.com/watch?v=wHr8Oas_9Vk&list=PLDTpj08jsReiCqkiTFNzXpwPNKG4Todcs&index=3)

 
#### Make a virtual Environment in python. Run these command on your command prompt
 
```bash 
    python -m venv env-graphdsa 
```

 
#### Change Directory into the newly create Python virtual environment folder. Activate the Virtual Environment. Use these 2 commands to do that
 
```bash
cd env-graphdsa
Scripts\activate

``` 

 
#### Go to my github folder where the codes are stored  [Here](https://github.com/emmanuelbakare/graph_dsa_gdfs) and copy the code by clicking on the Green “ <> Code” button and copy this link as shown in the drop down that shows.         https://github.com/emmanuelbakare/graph_dsa_gdfs.git 


#### Go back to virtual environment and type this command. This will copy the codes in the git repository to your local computer and will set up git on  Note that the code will be copied to a folder named graphproj. You can optionally remove the 
 
```bash 
git clone https://github.com/emmanuelbakare/graph_dsa_gdfs.git  graphdsa

```

 
#### Navigate to the project file (graphdsa) and download all the requirements that will make it work. Use these commands. Make sure you are in the virtual environment as explained in 3 above before installing the requirements. Make sure you are on the internet to be able to download all the requirements
 
```bash 
pip install -r requirements.txt
cd graphdsa
```
 
 
#### Now activate the webserver that will make you be able to browse your application
 
```bash 
python manage.py runserver
```

 
#### If you didn’t get any error. Go to your browser to  browse http://127.0.0.1:8000/ to see your application

#### Click on the **Admin Page** link to see your admin page.
> admin Login username: admin password: pass123

From the admin page, you can add new graph.


#### click on the ***Grahp Dashboard** link to see the graph dashboard

#### click the ***Depth First Search** button to see the depth first search of the graph - using the first item as the root.
 
# Running the Command Line Interface Version

#### Ensure you are in your python virtual environment as stipulated above. Below are steps to get there.
1. Open a command line interface on windows
1. navigate to the folder where your virtual folder is  and activate it.
1. go to your python project folder and run Visual Studio code IDE from there. You can also use any other IDE you want.
> below are the steps (Leave out the > sign in your typing)
```bash
> cd\env-graphdsa  
> scripts\activate
> cd graphdsa
```
>  the name of the file to execute is **cmd_view.py** located inside folder utils. Now run the code
```bash
python utils\cmd_view.py
```
> after running this commands on the command line terminal, you are taken to the program

![Graph DFS Interface](https://github.com/emmanuelbakare/graph_dsa_gdfs/blob/main/media/CMD_main_menu.JPG)

> Please not that menu item 7 (Show Diagram) have to be selected every time you make a change to your graph structure so that the system will regenerate a new version of the graph. If you do not do this, you will be seeing the old graph you implemented.
> The video explains how to use it.




