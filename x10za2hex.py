import subprocess
import sys
import re
from rich.console import Console
from rich.table import Table

def assemble_to_hex(assembly_code):
    """
    Assembles Xtensa assembly and extracts hex encoding.
    Displays output in an auto-expanding table format.
    """
    console = Console()
    table = Table(expand=False)
    table.add_column("Instruction", style="bold purple", justify="left")
    table.add_column("Hex Code", style="bold green", justify="center")
    
    # Write assembly code to file
    with open("input.S", "w") as f:
        f.write(".section .text\n.global main\nmain:\n    " + assembly_code + "\n")
    
    try:
        # Assemble the input
        subprocess.run(["xtensa-esp32-elf-as", "-o", "output.o", "input.S"], check=True)
        
        # Extract hex encoding using objdump
        objdump_output = subprocess.run(
            ["xtensa-esp32-elf-objdump", "-d", "output.o"], capture_output=True, text=True
        ).stdout
        
        # Improved regex to handle both `l32i` and `l32i.n`
        matches = re.findall(r"^\s*([0-9a-f]+):\s+([0-9a-f\s]+)\s+([a-zA-Z0-9._]+)(?:\s+(.*))?$", objdump_output, re.MULTILINE)
        
        if matches:
            for match in matches:
                address, hex_code, mnemonic, operands = match
                formatted_instruction = f"{mnemonic} {operands.strip() if operands else ''}".strip()
                table.add_row(formatted_instruction, hex_code.upper().strip())
            console.print(table)
        else:
            console.print("[red]Error: Failed to parse objdump output.[/red]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error during assembly: {e}[/red]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python xtensa_to_hex.py '<assembly instruction>'")
        sys.exit(1)
    
    assembly_code = sys.argv[1]
    assemble_to_hex(assembly_code)
