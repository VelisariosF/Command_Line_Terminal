from typing import Optional
import sys
import typer 
import os
import FilesHelper
app = typer.Typer()


@app.command()
def chd(path : str):
    currentDir = os.getcwd()
    if(path == ".."):
        cdlist = os.getcwd().split("\\")
        path = FilesHelper.constructPreviousPathFromList(cdlist)
        print(f"The path is :  {path}")
        os.chdir(path)
        print(os.getcwd())

        




## method to list the files in directory
@app.command()
def lD(path : Optional[str] = typer.Argument(None)):
    dir_list = []
    if(path is None):
        dir_list = os.listdir(".")
    else:
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
 