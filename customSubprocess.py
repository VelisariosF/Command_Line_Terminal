from typing import Optional
import sys
import typer 
import os
import re
import FilesHelper
app = typer.Typer()


@app.command()
def chd(path : str):
    
    os.chdir(FilesHelper.loadCurrentPath())
    print(f"Cur os path: {os.getcwd()}")
    currentDir = FilesHelper.loadCurrentPath()
    
    if(path == ".."):
        cdlist = re.split(r'\\', currentDir)
        path = FilesHelper.constructPreviousPathFromList(cdlist)
       
        os.chdir(path)
        print(os.getcwd())
        FilesHelper.saveCurrentPath(os.getcwd())
    else:
        os.chdir(path)
    
    

        




## method to list the files in directory
@app.command()
def lD(path : Optional[str] = typer.Argument(FilesHelper.loadCurrentPath())):
    dir_list = []
    dir_list = os.listdir(path)
    for dir in dir_list:
           print(dir)
  

@app.command()
def q():
    typer.Abort()


##--------  Example commands ---------##
@app.command()
def hello(name: Optional[str] = typer.Argument(None)):
     if not(name is None):
        typer.echo(f"Hello {name}")
       

@app.command()
def goodbye(name: Optional[str] = typer.Argument(None)):
    if not(name is None):
        typer.echo(f"Goodbye {name}")

        

    

if __name__=="__main__":
     app()
 