# PowerShell MCP服务器

一个基于MCP（Model Context Protocol）协议的PowerShell命令执行服务器，让AI助手能够直接调用和控制PowerShell，实现强大的系统管理能力。

## 项目简介

### 💡 开发背景
在日常开发和系统管理工作中，我们经常需要让AI助手执行系统命令来获取信息或进行配置。但是传统的AI工具往往只能提供文本建议，无法直接执行命令。这个MCP服务器的诞生就是为了解决这个问题！

### 🎯 核心功能
- **直接执行PowerShell命令**：AI助手可以实时执行任何PowerShell命令
- **智能系统检测**：自动识别PowerShell版本和系统环境
- **UTF-8国际化支持**：完美处理中文和其他国际字符
- **安全超时控制**：防止长时间运行的命令影响系统
- **详细错误处理**：提供完整的错误信息和调试支持

### 🔥 独特优势
- **零配置启动**：安装即可使用，无需复杂配置
- **MCP协议兼容**：与Claude Desktop、Cursor等主流AI客户端无缝集成
- **实时输出**：命令执行结果实时返回，无需等待
- **权限控制**：基于运行环境的权限管理，安全可靠

## 部署指南

### 🚀 环境要求
- **Python**: 3.8或更高版本
- **PowerShell**: 系统自动检测
- **网络**: 需要PyPI访问权限（用于安装依赖）

### 📦 安装方式

#### 方式1：pip安装（推荐）
```bash
pip install powershell-mcp
```

#### 方式2：uvx快速启动
```bash
# 安装uv（如果尚未安装）
pip install uv

# 直接运行
uvx powershell-mcp
```

### ⚙️ 客户端配置

#### Claude Desktop配置
创建或编辑配置文件：
```json
{
  "mcpServers": {
    "powershell": {
      "command": "uvx",
      "args": ["powershell-mcp"]
    }
  }
}
```

配置文件路径：
- **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### 🔧 验证安装

#### 命令行测试
```bash
# 测试PowerShell信息获取
powershell-mcp get_powershell_info

# 测试命令执行
powershell-mcp powershell_command "Get-Date"
```

#### Python测试
```python
from mcp_powershell import powershell_command, get_powershell_info

# 测试系统信息
print(get_powershell_info())

# 测试命令执行
result = powershell_command("Get-Process | Select-Object -First 3")
print(result)
```

## 使用示例

### 📊 系统信息获取示例

#### 获取PowerShell详细信息
```bash
$ powershell-mcp get_powershell_info
```

**输出示例**：
```json
{
  "powershell_version": "7.4.1",
  "platform": "Windows",
  "architecture": "64-bit",
  "execution_policy": "RemoteSigned",
  "ps_version_table": {
    "PSVersion": "7.4.1",
    "PSEdition": "Core",
    "OS": "Microsoft Windows 10.0.22631"
  }
}
```

### ⚡ 命令执行示例

#### 查看系统进程
```bash
$ powershell-mcp powershell_command "Get-Process | Select-Object Name, CPU, ID -First 5"
```

**输出示例**：
```
Name          CPU    ID
----          ---    --
chrome      12.34  1234
vscode       5.67  5678
explorer     2.89  4321
powershell   1.23  8765
teams        8.90  3456
```

#### 文件系统操作
```bash
# 查看当前目录文件
$ powershell-mcp powershell_command "Get-ChildItem | Select-Object Name, Length, LastWriteTime"

# 创建新目录
$ powershell-mcp powershell_command "New-Item -ItemType Directory -Path 'test_folder' -Force"

# 获取磁盘空间
$ powershell-mcp powershell_command "Get-PSDrive C | Select-Object Name, Used, Free, @{Name='PercentFree';Expression={[math]::Round(($_.Free/$_.Used)*100,2)}}"
```

#### 网络信息查询
```bash
# 查看网络配置
$ powershell-mcp powershell_command "Get-NetIPAddress | Where-Object {$_.AddressFamily -eq 'IPv4'} | Select-Object IPAddress, InterfaceAlias"

# 测试网络连接
$ powershell-mcp powershell_command "Test-Connection -ComputerName google.com -Count 2 | Select-Object Address, ResponseTime"
```

### 🎯 实际应用场景

#### 场景1：系统监控
```bash
# 检查系统性能
$ powershell-mcp powershell_command "Get-Counter '\Processor(_Total)\% Processor Time' | Select-Object -ExpandProperty CounterSamples"
```

#### 场景2：文件批量处理
```bash
# 批量重命名文件
$ powershell-mcp powershell_command "Get-ChildItem *.txt | Rename-Item -NewName {$_.Name -replace '.txt', '_backup.txt'}"
```

#### 场景3：服务管理
```bash
# 查看服务状态
$ powershell-mcp powershell_command "Get-Service | Where-Object {$_.Status -eq 'Running'} | Select-Object Name, Status"

# 重启服务
$ powershell-mcp powershell_command "Restart-Service -Name 'Spooler' -Force"
```

### 🖼️ 效果展示

#### Claude Desktop集成效果
当在Claude Desktop中配置完成后，你可以这样对话：

**用户**: "帮我查看一下当前系统的内存使用情况"

**Claude**: 我将使用PowerShell来检查您的系统内存...
```
Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory
```

**结果**: 
```
TotalVisibleMemorySize FreePhysicalMemory
--------------------- ------------------
               16384              10240
```

您的系统总内存为16GB，当前可用内存约10GB。

#### Cursor集成效果
在Cursor中可以直接让AI执行PowerShell命令：

**用户**: "显示当前目录下的所有Python文件"

**AI**: 执行命令...
```
Get-ChildItem -Filter *.py | Select-Object Name, Length, LastWriteTime
```

**结果**:
```
Name              Length LastWriteTime
----              ------ -------------
main.py             1024 2024-01-15 10:30
utils.py            2048 2024-01-15 09:15
config.py            512 2024-01-15 08:45
```

## 🎉 快速开始

1. **立即安装**：`pip install powershell-mcp`
2. **配置客户端**：按照上面的配置指南设置你的AI客户端
3. **开始体验**：让AI帮你管理系统，享受智能化的操作体验！

---

**💡 小贴士**：建议先在测试环境中熟悉功能，再在生产环境中使用。所有命令都支持超时设置，确保系统安全！
