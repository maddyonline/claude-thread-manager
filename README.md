# Claude Thread Manager (ct)

A stateless thread management wrapper for Claude CLI that provides persistent conversation context using environment variables.

## Features

✅ **Environment-driven threads** - Set `THREAD_ID` to manage conversation context  
✅ **Auto-detects claude/claudee** - Works with your existing aliases  
✅ **Stateless operation** - No state files, pure environment-based  
✅ **Smart session selection** - Finds the best session to resume  
✅ **Graceful fallback** - Works without THREAD_ID as normal claude  

## Installation

### Quick Installation with uv (Recommended)

```bash
# Install directly from the repository
uv tool install git+https://github.com/maddyonline/claude-thread-manager

# Or run without installation
uvx --from git+https://github.com/maddyonline/claude-thread-manager ct -p "your message"
```

### Traditional Installation

```bash
# With pip
pip install git+https://github.com/maddyonline/claude-thread-manager

# From source
git clone https://github.com/maddyonline/claude-thread-manager
cd claude-thread-manager
pip install -e .
```

## Usage

### Method 1: Using the installed command
```bash
export THREAD_ID="my-feature"
ct -p "help me implement authentication"
ct -p "now add tests"
```

### Method 2: Create an alias for seamless integration
Add to your shell config (`.bashrc`, `.zshrc`, etc.):
```bash
alias claude='ct'
# Or if you prefer your existing claudee alias:
alias claudee='ct'
```

Then use normally:
```bash
export THREAD_ID="my-feature"
claude -p "your message"
```

### Method 3: Without THREAD_ID (falls back to normal claude)
```bash
ct -p "this runs normal claude"
```

## How It Works

1. **Environment-based**: Uses `THREAD_ID` environment variable for thread isolation
2. **Workspace per thread**: Each thread runs from `~/.workspace/$THREAD_ID`
3. **Smart session detection**: Automatically finds and resumes the latest valid session
4. **Command detection**: Auto-detects whether to use `claude` or `claudee`

## Examples

```bash
# Feature development thread
export THREAD_ID="auth-feature"
ct -p "help me implement JWT authentication"
ct -p "now add password reset functionality"

# Bug investigation thread  
export THREAD_ID="memory-leak-bug"
ct -p "analyze this memory leak in the app"

# Quick one-off without thread
unset THREAD_ID
ct -p "what is 2+2"

# Using with alias
alias claude='ct'
export THREAD_ID="my-project"
claude -p "help me debug this issue"
```

## Requirements

- Python 3.8+
- Claude CLI installed and accessible
- No additional dependencies