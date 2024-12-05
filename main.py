import os
import subprocess
import sys
import time
import requests
import asyncio
from rich.console import Console

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def check_internet():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def install_requirements():
    requirements = [
        "aiohttp",
        "rich",
        "Pillow==9.0.0", 
        "beautifulsoup4"
    ]
    for package in requirements:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            console.print(f"[bold green]Successfully installed {package}[/bold green]")
        except subprocess.CalledProcessError:
            console.print(f"[bold red]Failed to install {package}[/bold red]")
            sys.exit(1)

def main():
    clear_screen()
    console.print("[bold blue]Starting Script...[/bold blue]")
    
    # تحقق من الاتصال بالإنترنت
    if not check_internet():
        console.print("[bold red]No internet connection. Please check your connection and try again.[/bold red]")
        sys.exit(1)
    
    console.print("[bold green]Internet connection is available.[/bold green]")
    
    # التحقق من وجود المكتبات المطلوبة
    console.print("[bold blue]Checking required libraries...[/bold blue]")
    try:
        import aiohttp
        import rich
        import PIL
        from bs4 import BeautifulSoup
        console.print("[bold green]All required libraries are installed.[/bold green]")
    except ImportError:
        console.print("[bold yellow]Missing some libraries. Installing now...[/bold yellow]")
        install_requirements()


    console.print("[bold green]All requirements are met. Starting the script...[/bold green]")
    

    try:
        import main_script
        asyncio.run(main_script.main_menu())  
    except ImportError:
        console.print("[bold red]Failed to import the main script. Please check the script structure.[/bold red]")

if __name__ == "__main__":
    main()
