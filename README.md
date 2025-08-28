# MCP PowerShell Toolkit

A Python package that provides PowerShell command execution capabilities via the MCP (Model Context Protocol).

## Features

- Execute PowerShell commands from Python
- Cross-platform support (Windows, Linux, macOS)
- UTF-8 encoding support for international characters
- Built-in PowerShell version detection
- Configurable timeout settings
- Error handling and detailed output

## Installation

```bash
pip install powershell-mcp
```

## Usage

### As an MCP Server

```bash
python -m mcp_powershell
```

### As a Python Package

```python
from mcp_powershell import powershell_command, get_powershell_info

# Execute a PowerShell command
result = powershell_command("Get-Process | Select-Object -First 5")
print(result)

# Get PowerShell system information
info = get_powershell_info()
print(info)
```

### Available Functions

- `powershell_command(command, timeout=30, encoding='utf-8')`: Execute any PowerShell command
- `get_powershell_info()`: Get PowerShell version and system information

## Examples

```python
# List all files in current directory
result = powershell_command("Get-ChildItem")

# Get system information
result = powershell_command("Get-ComputerInfo")

# Execute with custom timeout
result = powershell_command("Start-Sleep -Seconds 10", timeout=5)  # Will timeout
```

## Requirements

- Python 3.8 or higher
- PowerShell (automatically detected)
- MCP library

## License

MIT License