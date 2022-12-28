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

 
#### Go to my github folder where the codes are stored  [Here](https://github.com/emmanuelbakare/Graph_DFS_DSA) and copy the code by clicking on the Green “ <> Code” button and copy this link as shown in the drop down that shows.         https://github.com/emmanuelbakare/Graph_DFS_DSA.git 


#### Go back to virtual environment and type this command. This will copy the codes in the git repository to your local computer and will set up git on  Note that the code will be copied to a folder named graphproj. You can optionally remove the 
 
```bash 
git clone https://github.com/emmanuelbakare/Graph_DFS_DSA.git  graphdsa

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

 
#### If you didn’t get any error. Go to your browser to  browse http://127.0.0.1:8000/graphs/ to see your application

#### click on any of the **groups list** To see all the connections associated with it

#### click on the ***Full graph diagram** to see the graph diagram in another window

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
> cd utils
```
>  the name of the file to execute is **cmd_view.py** located inside folder utils. Now run the code
```bash
python cmd_view.py
```
> The video explains how to use it.



