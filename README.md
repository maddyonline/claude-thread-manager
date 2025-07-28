# Claude Thread Manager (ct)

A stateless thread management wrapper for Claude CLI that provides persistent conversation context using environment variables.

## Features

✅ **Environment-driven threads** - Set `THREAD_ID` to manage conversation context  
✅ **Auto-detects claude/claudee** - Works with your existing aliases  
✅ **Stateless operation** - No state files, pure environment-based  
✅ **Smart session selection** - Finds the best session to resume  
✅ **Graceful fallback** - Works without THREAD_ID as normal claude  

## Quick Start

```bash
# Install with uv
uv tool install --from git+https://github.com/your-username/claude-thread-manager ct

# Use with threads
export THREAD_ID="my-feature"
ct -p "help me implement authentication"
ct -p "now add tests"  # Remembers context!

# Use without threads (normal claude)
unset THREAD_ID  
ct -p "what is 2+2"
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
```

## Installation

See [INSTALLATION.md](INSTALLATION.md) for detailed installation instructions.

## Requirements

- Python 3.8+
- Claude CLI installed and accessible
- No additional dependencies