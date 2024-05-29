import typer
import requests

app = typer.Typer() # Initialization of typer instance

base_url = 'http://localhost/' # default base url
default_output = '-' # default standard output

@app.command()
# setting stat method for client with basic parameters
def stat(
    # definition of arguments
    uuid: str,
    backend: str = typer.Option("grpc", help="Set a backend to be used, choices are grpc and rest. Default is gRPC."),
    base_url: str = typer.Option(base_url, help = "Set a base URL for a REST API server. Default is http://localhost/."),
    default_output: str = typer.Option(default_output, help= " Set the file where to store the output. Default is -, what's mean stdout to terminal.")
    ):
    """Display file stats."""
    if backend != "rest": # error if REST server not chosen
        typer.echo("Only REST backend is supported in this implementation.", err=True)
        raise typer.Exit(code=1)

    response = requests.get(f"{base_url}file/{uuid}/stat/") # GET method asking for status

    if response.status_code == 404:
        typer.echo(f"File not found.")
        raise typer.Exit()

    elif response.status_code == 200:
        metadata = response.json()

    else:
        typer.echo(f"Failed to retrieve file info. Status code: {response.status_code}")

    output_content = (
        f"Name: {metadata['name']}\n"
        f"Size: {metadata['size']} bytes\n"
        f"MIME Type: {metadata['mimetype']}\n"
        f"Created: {metadata['create_datetime']}\n"
                    )

    if default_output == "-":
        typer.echo(output_content)
    else:
        with open(default_output, "w") as f:
            f.write(output_content)

@app.command()
def read(
    # definition of arguments
    uuid: str,
    backend: str = typer.Option("grpc", help = "Set a backend to be used, choices are grpc and rest. Default is gRPC."),
    base_url: str = typer.Option(base_url, help = "Set a base URL for a REST API server. Default is http://localhost/."),
    default_output: str = typer.Option(default_output, help = " Set the file where to store the output. Default is -, what's mean stdout to terminal.")
    ):
    """Read content of file."""
    if backend != "rest": # error if REST server not chosen
        typer.echo("Only REST backend is supported in this implementation.", err = True)
        raise typer.Exit(code = 1)

    response = requests.get(f"{base_url}file/{uuid}/read/") # GET method asking for status

    if response.status_code == 404:
        typer.echo(f"File not found.")
        raise typer.Exit()

    elif response.status_code == 200:
        if default_output == "-":  # printing content to console
            typer.echo(response.content)
        else:  # writing content to file
            with open(default_output, "wb") as f:
                f.write(response.content)

if __name__ == "__main__":
    app()
