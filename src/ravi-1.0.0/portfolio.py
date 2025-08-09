#!/usr/bin/env python
from time import sleep
from rich.console import Console
from rich.panel import Panel

console = Console()

def type_out(text, delay=0.03, style=None):
    for char in text:
        console.print(char, style=style, end="")
        sleep(delay)
    console.print("")

def main():
    console.clear()

    # 1. ASCII logo (once)
    ascii_art = """
    ____              _ __ __ _                
   / __ \\____ __   __(_) //_/(_)________ _____ 
  / /_/ / __ `/ | / / / ,<  / / ___/ __ `/ __ \\
 / _, _/ /_/ /| |/ / / /| |/ / /  / /_/ / / / /
/_/ |_|\\__,_/ |___/_/_/ |_/_/_/   \\__,_/_/ /_/ 
    """
    console.print(ascii_art, style="bold cyan")
    sleep(0.8)

    # 2. System Info (once)
    sys_info = [
        "[bold yellow]Name:[/bold yellow] [white]Ravi Kiran",
        "[bold yellow]Title:[/bold yellow] [white]AI & Full-Stack Developer",
        "[bold yellow]OS:[/bold yellow] [white]RaviLinux x86_64",
        "[bold yellow]Uptime:[/bold yellow] [white]22 years, coding nonstop",
        "[bold yellow]Packages:[/bold yellow] [white]500 (pacman, yay)",
        "[bold yellow]Languages:[/bold yellow] [white]Python, JavaScript, TypeScript, Golang, C++, Java, SQL",
        "[bold yellow]AI/ML:[/bold yellow] [white]PyTorch, Transformers, LangChain, LSTM, FAISS",
        "[bold yellow]Web:[/bold yellow] [white]React.js, Next.js, Node.js, Express.js, FastAPI, TailwindCSS"
    ]
    console.print(Panel("\n".join(sys_info), title="System Info", style="cyan"))
    sleep(0.8)

    # 3. Pacman simulation (once)
    console.print("\n$ pacman -S projects", style="bold green")
    sleep(0.5)
    type_out("resolving dependencies...", 0.02)
    type_out("looking for conflicting packages...", 0.02)
    sleep(0.3)

    installs = [
        "✔ installed autoquantx-1.0",
        "✔ installed voiceassist-ai-2.1",
        "✔ installed mern-ecommerce-3.5"
    ]
    for pkg in installs:
        type_out(pkg, 0.02, "green")
        sleep(0.3)
    type_out("(100%) All packages installed", 0.02)
    sleep(0.8)

    # 4. Projects (once)
    projects_text = """[bold]1.[/bold] AutoQuantX – LLM-Orchestrated Quant Trading
    - Parses strategies → structured configs & DAGs
    - Real-time data streaming with Kafka & Redis
    - Alpha signals using XGBoost, LSTM

[bold]2.[/bold] VoiceAssist AI – Modular Real-Time Voice Assistant
    - Go backend + Python microservices
    - React frontend with audio streaming

[bold]3.[/bold] MERN E-Commerce Platform
    - Auth, product management, payments
    """
    console.print(Panel(projects_text, title="Projects", style="magenta"))
    sleep(0.8)

    # 5. Contact (once)
    contact_text = """GitHub: https://github.com/RaviKiran752
LinkedIn: https://linkedin.com/in/ravi-kiran7/
Email: ravi742t7p@gmail.com"""
    console.print(Panel(contact_text, title="Contact", style="blue"))
    sleep(0.3)

    console.print("\n[bold green]Thanks for checking out the portfolio — type 'ravikiran --help' for more![/bold green]")

if __name__ == "__main__":
    main()
