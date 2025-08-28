# PowerShell MCP 本地配置指南

## 安装步骤

### 1. 安装包
```bash
pip install powershell-mcp
```

### 2. 配置 Claude Desktop

找到 Claude Desktop 的配置文件：
- **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### 3. 添加配置

在配置文件中添加以下内容：

```json
{
  "mcpServers": {
    "powershell": {
      "command": "python",
      "args": ["-m", "mcp_powershell"],
      "env": {}
    }
  }
}
```

### 4. 验证安装

重启 Claude Desktop 后，可以通过以下方式验证：
1. 询问 Claude "你能执行PowerShell命令吗？"
2. 或者直接测试："帮我列出当前目录的文件"

## 高级配置

### 指定Python路径（如果需要）
```json
{
  "mcpServers": {
    "powershell": {
      "command": "C:\\Users\\你的用户名\\AppData\\Local\\Programs\\Python\\Python39\\python.exe",
      "args": ["-m", "mcp_powershell"],
      "env": {}
    }
  }
}
```

### 开发模式（本地源码）
```json
{
  "mcpServers": {
    "powershell": {
      "command": "python",
      "args": ["-m", "mcp_powershell"],
      "cwd": "D:\\MCP\\powershell\\source-code",
      "env": {}
    }
  }
}
```

## 故障排除

### 常见问题
1. **找不到python**: 检查Python是否在PATH中
2. **权限问题**: 以管理员身份运行Claude Desktop
3. **路径问题**: 使用绝对路径指定python可执行文件

### 测试命令
```bash
python -m mcp_powershell --help
```