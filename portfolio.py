#!/usr/bin/env python3

import sys
import time
import random
import shutil
from time import sleep
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.rule import Rule
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
from rich.align import Align
from rich import box
from rich.padding import Padding

# Initialize Console
console = Console()

# ─────────────────────────────────────────────
#  UTILITIES & ANIMATIONS
# ─────────────────────────────────────────────

def type_out(text, delay=0.018, style=None, end="\n"):
    for char in text:
        console.print(char, style=style, end="", highlight=False)
        sleep(delay)
    if end:
        console.print("", end=end)

def glitch_print(text, style="bold cyan", repeats=3, final_delay=0.04):
    glitch_chars = "▓░▒█▄▀■□▪▫"
    for _ in range(repeats):
        noise = "".join(
            random.choice(glitch_chars) if random.random() < 0.3 else c
            for c in text
        )
        console.print(f"\r{noise}", style="dim red", end="")
        sleep(0.04)
    sleep(0.1)
    console.print(f"\r{text}", style=style, end="", highlight=False)
    sleep(final_delay)
    console.print("")

def simulate_boot_sequence():
    lines = [
        ("BIOS v2.4.1 — RaviOS Kernel 6.9.0-arch1", "dim white"),
        ("Loading bootloader... [OK]", "dim green"),
        ("Mounting /dev/brain → /mnt/mind... [OK]", "dim green"),
        ("Starting systemd services:", "dim white"),
        ("  [  OK  ] Started coffee.service", "dim cyan"),
        ("  [  OK  ] Started llm-daemon.service", "dim cyan"),
        ("", None),
    ]
    for line, style in lines:
        if style:
            console.print(line, style=style)
        else:
            console.print("")
        sleep(0.05)

# ─────────────────────────────────────────────
#  CONTENT SECTIONS
# ─────────────────────────────────────────────

ASCII_LOGO = r"""
 ██████╗  █████╗ ██╗   ██╗██╗    ██╗  ██╗██╗██████╗  █████╗ ███╗   ██╗
 ██╔══██╗██╔══██╗██║   ██║██║    ██║ ██╔╝██║██╔══██╗██╔══██╗████╗  ██║
 ██████╔╝███████║██║   ██║██║    █████╔╝ ██║██████╔╝███████║██╔██╗ ██║
 ██╔══██╗██╔══██║╚██╗ ██╔╝██║    ██╔═██╗ ██║██╔══██╗██╔══██║██║╚██╗██║
 ██║  ██║██║  ██║ ╚████╔╝ ██║    ██║  ██╗██║██║  ██║██║  ██║██║ ╚████║
 ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

def show_header():
    glitch_print(ASCII_LOGO, style="bold cyan", repeats=2)
    tagline = "[ AI Engineer  ·  Full-Stack Developer  ·  Open-Source Hacker ]"
    console.print(Align.center(f"[bold white]{tagline}[/bold white]"))
    console.print(Align.center("[dim]ravi742t7p@gmail.com  ·  github.com/RaviKiran752[/dim]"))
    console.print(Rule(style="dim cyan"))

def show_system_info():
    logo_lines = [
        "[bold cyan]    ____              _ __ __ _    [/bold cyan]",
        "[bold cyan]   / __ \\____ __   __(_) //_/(_)  [/bold cyan]",
        "[bold cyan]  / /_/ / __ `/ | / / / ,<  / /   [/bold cyan]",
        "[bold cyan] / _, _/ /_/ /| |/ / / /| |/ /    [/bold cyan]",
        "[bold cyan]/_/ |_|\\__,_/ |___/_/_/ |_/_/     [/bold cyan]",
    ]
    info_lines = [
        "[bold yellow]os[/bold yellow]        [white]RaviOS x86_64[/white]",
        "[bold yellow]kernel[/bold yellow]    [white]6.9.0-AI-arch1[/white]",
        "[bold yellow]uptime[/bold yellow]    [white]22 years, still compiling[/white]",
        "[bold yellow]shell[/bold yellow]     [white]zsh + tmux + nvim[/white]",
        "[bold yellow]memory[/bold yellow]    [white]8 years CS + 400 LeetCode problems[/white]",
        "[bold yellow]cgpa[/bold yellow]      [white]7.68 / 10 — LPU[/white]",
    ]
    for logo, info in zip(logo_lines, info_lines):
        console.print(f"{logo}  {info}")
        sleep(0.02)

def show_experience():
    console.print(Panel(
        "[bold white]Software Engineering Intern — AI/ML & Computer Vision[/bold white]\n"
        "[dim cyan]Terafac Technologies Pvt. Ltd.  ·  Aug 2025 – Feb 2026[/dim cyan]\n\n"
        "[bold green]▸[/bold green] Engineered industrial automation workflows using deep learning & 3D geometry.\n"
        "[bold green]▸[/bold green] Built [cyan]raycasting pipelines[/cyan] for 3D reconstruction with < 1.5mm error margin.",
        border_style="cyan", box=box.ROUNDED, padding=(0, 2)
    ))

def show_projects():
    projects = [
        {"n": "AutoQuantX", "s": "LLM Quantitative Trading", "c": "magenta", "b": "LangChain + Kafka + Redis"},
        {"n": "VoiceAssist AI", "s": "Real-Time Voice Assistant", "c": "yellow", "b": "Golang + Whisper + gRPC"},
    ]
    for p in projects:
        console.print(Panel(f"[bold white]{p['n']}[/bold white] [dim]· {p['s']}[/dim]\n[dim]{p['b']}[/dim]", border_style=p['c']))

def show_skills():
    skills = {
        "Languages": ["Python", "JS/TS", "Go", "C++"],
        "AI/ML": ["PyTorch", "HuggingFace", "LangChain", "RAG"],
        "Infra": ["Docker", "GCP", "ROS2", "Redis"]
    }
    for category, items in skills.items():
        tags = "  ".join(f"[bold cyan][[/bold cyan]{i}[bold cyan]][/bold cyan]" for i in items)
        console.print(f"[bold white]{category:<12}[/bold white] {tags}")

def show_contact():
    table = Table(box=box.SIMPLE, show_header=False)
    table.add_row("📧", "Email", "ravi742t7p@gmail.com")
    table.add_row("🐙", "GitHub", "github.com/RaviKiran752")
    table.add_row("🌐", "Web", "ravi-portfolio-chi.vercel.app")
    console.print(table)

def show_help():
    help_table = Table(box=box.ROUNDED, border_style="dim cyan", title="[bold cyan]RaviOS Commands[/bold cyan]")
    help_table.add_column("Command", style="bold white")
    help_table.add_column("Action", style="dim")
    cmds = [
        ("neofetch", "Display system and tech info"),
        ("exp", "View professional experience"),
        ("ls projects", "List major projects"),
        ("skills", "Show technical stack"),
        ("contact", "Get contact info"),
        ("clear", "Clear the terminal"),
        ("exit", "Terminate RaviOS session")
    ]
    for c, a in cmds: help_table.add_row(c, a)
    console.print(help_table)

# ─────────────────────────────────────────────
#  INTERACTIVE ENGINE
# ─────────────────────────────────────────────

def main():
    console.clear()
    simulate_boot_sequence()
    show_header()
    
    # Map input strings to functions
    commands = {
        "neofetch": show_system_info,
        "system": show_system_info,
        "exp": show_experience,
        "projects": show_projects,
        "ls": show_projects,
        "skills": show_skills,
        "contact": show_contact,
        "help": show_help,
        "?": show_help
    }

    type_out("\n[!] System Ready. Type [bold cyan]'help'[/bold cyan] to begin.", style="dim green")

    while True:
        try:
            # Styled shell prompt
            prompt = Text.assemble(
                ("\n╭─ ", "dim cyan"),
                ("ravi@RaviOS", "bold green"),
                (" in ", "white"),
                ("~", "bold blue"),
                ("\n╰─", "dim cyan"),
                ("$ ", "bold white")
            )
            
            user_input = console.input(prompt).strip().lower()

            if user_input in ["exit", "quit", "shutdown"]:
                glitch_print("Shutting down RaviOS... Session terminated.", style="bold red")
                break
            elif user_input == "clear":
                console.clear()
                show_header()
            elif user_input in commands:
                with console.status("[bold cyan]Executing...", spinner="dots"):
                    sleep(0.4)
                    commands[user_input]()
            elif user_input == "":
                continue
            else:
                console.print(f"[red]Error:[/red] Command '{user_input}' not found. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            console.print("\n[dim]Use 'exit' to close the shell.[/dim]")
            continue

if __name__ == "__main__":
    main()
