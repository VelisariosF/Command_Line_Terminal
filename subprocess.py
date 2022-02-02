from typing import Optional
import sys
import typer 
import FilesHelper
app = typer.Typer()


@app.command()
def hello(name: Optional[str] = typer.Argument(None)):
     if not(name is None):
        typer.echo(f"Hello {name}")
       

@app.command()
def goodbye(name: Optional[str] = typer.Argument(None)):
    if not(name is None):
        typer.echo(f"Goodbye {name}")
   
@app.command()
def q():
    typer.Abort()

    

if __name__=="__main__":
     app()
 