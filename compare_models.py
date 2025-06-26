import typer
import questionary
from rich.console import Console
from rich.panel import Panel

from models import openai_handler, hf_handler, registry
from utils.token_utils import token_summary

app = typer.Typer()
console = Console()

def compare (): 
    console.print("Comparing models...")
    console.rule("[bold blue] moodel comparision CLI")
    
    prompt = questionary.text("Enter your prompt: ").ask()

    if not prompt :
        console.print("[red] no prompt entered. exiting ...")
        return typer.Exit()

    comparison_mode = questionary.select(
        "Select comparison mode:",
        choices = [
            "By type (base, instruct, fine tuned)",
            "All models (cross-type comparison)"
        ]
    ).ask()

    if comparison_mode == "By type (base, instruct, fine tuned)":
        # Original type-based filtering
        model_type = questionary.select(
            "select your model type:",
            choices = ["base", "instruct", "fine tuned"]
        ).ask()

        all_models = {
            name : meta for name, meta in registry.registry.items()
            if meta["type"] == model_type
        }

        if not all_models:
            console.print("[red]No models of that type found.")
            raise typer.Exit()

        console.print(f"[dim]Available {model_type} models: {list(all_models.keys())}")
    else:
        # Cross-type comparison - show all models
        all_models = registry.registry
        console.print(f"[dim]All available models: {list(all_models.keys())}")

    # If only one model available, auto-select it
    if len(all_models) == 1:
        selected_models = list(all_models.keys())
        console.print(f"[green]Auto-selected the only available model: {selected_models[0]}")
    else:
        # Create choices with type information for cross-type mode
        if comparison_mode == "All models (cross-type comparison)":
            choices = [f"{name} ({meta['type']} - {meta['source']})" for name, meta in all_models.items()]
            choice_to_model = {f"{name} ({meta['type']} - {meta['source']})": name for name, meta in all_models.items()}
        else:
            choices = list(all_models.keys())
            choice_to_model = {name: name for name in choices}

        selected_choices = questionary.checkbox(
            "Select models to compare (use SPACE to select, ENTER to confirm):",
            choices=choices
        ).ask()

        if not selected_choices:
            console.print("[red]No models selected. Please run the command again and select at least one model.")
            raise typer.Exit()

        # Convert back to model names
        selected_models = [choice_to_model[choice] for choice in selected_choices]
    
    console.print(f"\n[bold green]Running comparison...\n")


    for model_name in selected_models:
        source = registry.registry[model_name]["source"]

        try:
            # Dispatch to appropriate handler
            if source == "openai":
                response = openai_handler.query_openai(prompt, model_name)
            elif source == "hf":
                response = hf_handler.query_local_models(prompt, model_name)
            else:
                console.print(f"[red]Unknown source for model: {model_name}")
                continue

            # Display result
            console.print(Panel.fit(
                f"[bold cyan]{model_name}[/bold cyan]\n\n{response['response']}\n\n"
                f"[dim]Tokens used: {token_summary(response)}",
                title=f"[green]{source.upper()}",
                border_style="blue"
            ))
        except Exception as e:
            # Display error but continue with other models
            console.print(Panel.fit(
                f"[bold cyan]{model_name}[/bold cyan]\n\n[red]Error: {str(e)}[/red]",
                title=f"[red]{source.upper()} - ERROR",
                border_style="red"
            ))



if __name__ == "__main__":
    compare()