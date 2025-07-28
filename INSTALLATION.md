# Claude Thread Manager - Installation Guide

## Quick Installation with uv (Recommended)

### Option 1: Install as a tool with uv
```bash
# Install directly from the repository
uvx --from git+https://github.com/your-username/claude-thread-manager ct

# Or install locally for development
uv tool install --editable .
```

### Option 2: Use without installation
```bash
# Run directly with uvx
uvx --from . ct -p "your message"
```

## Traditional Installation

### With pip
```bash
pip install claude-thread-manager
```

### From source
```bash
git clone https://github.com/your-username/claude-thread-manager
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

## Features

✅ **Environment-driven threads** - Set `THREAD_ID` to manage conversation context  
✅ **Auto-detects claude/claudee** - Works with your existing aliases  
✅ **Stateless operation** - No state files, pure environment-based  
✅ **Smart session selection** - Finds the best session to resume  
✅ **Graceful fallback** - Works without THREAD_ID as normal claude  

## Examples

```bash
# Feature development thread
export THREAD_ID="auth-feature"
claude -p "help me implement JWT authentication"
claude -p "now add password reset functionality"

# Bug investigation thread  
export THREAD_ID="memory-leak-bug"
claude -p "analyze this memory leak in the app"

# Quick one-off without thread
unset THREAD_ID
claude -p "what is 2+2"
```