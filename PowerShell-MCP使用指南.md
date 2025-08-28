# PowerShell MCP 极简指南

## 🚀 使用 uvx 安装 (推荐)

### 1. 安装 python后

```bash
pip install powershell-mcp
```


### 2. Claude Desktop 配置

创建或编辑配置文件：
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

添加配置：
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

### 3. 重启 Claude Desktop

完事儿！重启 Claude Desktop 即可使用 PowerShell 功能。

**版本：1.0.5**

## 🎯 使用示例

在 Claude 中直接说：
- "列出当前目录的文件"
- "检查系统信息"
- "查看正在运行的进程"

无需额外配置，开箱即用！