"""
MCP PowerShell Toolkit - A Python package for executing PowerShell commands via MCP
"""

__version__ = "1.0.0"
__author__ = "DataMaster"
__email__ = "your.email@example.com"
__description__ = "PowerShell MCP toolkit for executing PowerShell commands"

import subprocess
import json
import sys
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PowerShell Toolkit")

@mcp.tool()
def powershell_command(command: str, timeout: int = 30, encoding: str = 'utf-8'):
    """
    Execute PowerShell command and return the result.
    
    Args:
        command (str): PowerShell command to execute
        timeout (int): Command timeout in seconds (default: 30)
        encoding (str): Output encoding (default: utf-8)
        
    Returns:
        dict: Contains success status, output, and error information
    """
    try:
        # 检测系统和PowerShell版本
        powershell_executable = _get_powershell_executable()
        
        # 构建PowerShell命令，设置输出编码
        if sys.platform == "win32":
            # Windows系统，解决中文编码问题
            powershell_cmd = [
                powershell_executable,
                '-NoProfile',
                '-OutputFormat', 'Text',
                '-Command',
                f'[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; {command}'
            ]
        else:
            # 非Windows系统
            powershell_cmd = [
                powershell_executable,
                '-NoProfile',
                '-Command',
                command
            ]
        
        # 设置环境变量以支持UTF-8
        env = os.environ.copy()
        if sys.platform == "win32":
            env['PYTHONIOENCODING'] = 'utf-8'
        
        # 执行命令
        result = subprocess.run(
            powershell_cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding=encoding,
            errors='replace',  # 处理编码错误
            env=env
        )
        
        # 构建返回结果
        response = {
            "success": result.returncode == 0,
            "return_code": result.returncode,
            "stdout": result.stdout.strip() if result.stdout else "",
            "stderr": result.stderr.strip() if result.stderr else "",
            "command": command,
            "powershell_version": powershell_executable
        }
        
        # 格式化输出
        if response["success"]:
            if response["stdout"]:
                return f"✅ Command executed successfully:\n\n{response['stdout']}"
            else:
                return "✅ Command executed successfully (no output)"
        else:
            error_msg = response["stderr"] if response["stderr"] else "Unknown error"
            return f"❌ Command failed (Exit Code: {response['return_code']}):\n\n{error_msg}"
            
    except subprocess.TimeoutExpired:
        return f"⏰ Command timed out after {timeout} seconds"
    except FileNotFoundError:
        return f"❌ PowerShell not found. Please ensure PowerShell is installed and in PATH.\nTried: {powershell_executable}"
    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"

def _get_powershell_executable():
    """
    检测可用的PowerShell可执行文件
    """
    if sys.platform == "win32":
        # Windows系统，优先使用PowerShell 7，然后是Windows PowerShell
        candidates = [
            'pwsh',  # PowerShell 7+
            'powershell'  # Windows PowerShell 5.x
        ]
    else:
        # Linux/macOS系统
        candidates = [
            'pwsh',  # PowerShell Core
            'powershell'
        ]
    
    for candidate in candidates:
        try:
            subprocess.run([candidate, '-Version'], 
                         capture_output=True, 
                         timeout=5)
            return candidate
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    
    # 如果都找不到，返回默认值
    return 'powershell' if sys.platform == "win32" else 'pwsh'

@mcp.tool()
def get_powershell_info():
    """
    获取PowerShell版本和系统信息
    
    Returns:
        dict: PowerShell和系统信息
    """
    try:
        powershell_executable = _get_powershell_executable()
        
        # 获取PowerShell版本信息
        version_cmd = [
            powershell_executable,
            '-NoProfile',
            '-Command',
            '$PSVersionTable | ConvertTo-Json'
        ]
        
        result = subprocess.run(
            version_cmd,
            capture_output=True,
            text=True,
            timeout=10,
            encoding='utf-8',
            errors='replace'
        )
        
        if result.returncode == 0:
            try:
                version_info = json.loads(result.stdout)
                return f"✅ PowerShell Information:\n\n{json.dumps(version_info, indent=2, ensure_ascii=False)}"
            except json.JSONDecodeError:
                return f"✅ PowerShell Version (raw):\n\n{result.stdout}"
        else:
            return f"❌ Failed to get PowerShell version: {result.stderr}"
            
    except Exception as e:
        return f"❌ Error getting PowerShell info: {str(e)}"

def main():
    """Main entry point for the CLI"""
    mcp.run()

__all__ = ['main', 'mcp', 'powershell_command', 'get_powershell_info']