#!/usr/bin/env python3
"""Claude Thread Manager CLI."""

import os
import sys
import subprocess
from pathlib import Path
from typing import Optional

def get_claude_command() -> str:
    """Detect which claude command to use (claude or claudee)."""
    # Check if claudee exists (user's alias with --dangerously-skip-permissions)
    if subprocess.run(["which", "claudee"], capture_output=True).returncode == 0:
        return "claudee"
    elif subprocess.run(["which", "claude"], capture_output=True).returncode == 0:
        return "claude"
    else:
        return "claude"  # Default fallback

def get_claude_project_dir(thread_id: str) -> Path:
    """Get the claude projects directory for a thread."""
    workspace_path = Path.home() / ".workspace" / thread_id
    # Convert path to claude projects format (replace / with - and . with -)
    escaped_path = str(workspace_path).replace("/", "-").replace(".", "-")
    return Path.home() / ".claude" / "projects" / escaped_path

def find_latest_session(thread_id: str) -> Optional[str]:
    """Find the latest session for a thread using heuristics."""
    project_dir = get_claude_project_dir(thread_id)
    
    if not project_dir.exists():
        return None
    
    # Find all session files
    session_files = list(project_dir.glob("*.jsonl"))
    if not session_files:
        return None
    
    # Filter out very small sessions (likely corrupted or incomplete)
    MIN_SESSION_SIZE = 500  # bytes
    valid_session_files = [f for f in session_files if f.stat().st_size >= MIN_SESSION_SIZE]
    
    if not valid_session_files:
        # If no valid sessions, fall back to all sessions
        valid_session_files = session_files
    
    # Sort by modification time (newest first), then by file size (largest first)
    valid_session_files.sort(key=lambda f: (f.stat().st_mtime, f.stat().st_size), reverse=True)
    
    # Return the session ID (filename without extension)
    return valid_session_files[0].stem

def ensure_workspace(thread_id: str) -> None:
    """Ensure workspace directory exists."""
    workspace_path = Path.home() / ".workspace" / thread_id
    workspace_path.mkdir(parents=True, exist_ok=True)

def main():
    """Main CLI entry point."""
    # Get thread ID from environment
    thread_id = os.environ.get('THREAD_ID')
    
    # Detect which claude command to use
    claude_cmd = get_claude_command()
    
    if not thread_id:
        # If no THREAD_ID, just run claude normally
        print("No THREAD_ID set - running claude directly without thread management")
        claude_args = [claude_cmd] + sys.argv[1:]
        try:
            result = subprocess.run(claude_args, check=False)
            sys.exit(result.returncode)
        except KeyboardInterrupt:
            sys.exit(130)
        except Exception as e:
            print(f"Error running claude: {e}")
            sys.exit(1)
    
    # Ensure workspace exists
    ensure_workspace(thread_id)
    workspace_path = Path.home() / ".workspace" / thread_id
    
    # Find existing session to resume
    latest_session = find_latest_session(thread_id)
    
    # Build claude command
    claude_args = [claude_cmd]
    if latest_session:
        claude_args.extend(["--resume", latest_session])
    
    # Add user's arguments
    claude_args.extend(sys.argv[1:])
    
    # Run claude from the thread workspace
    original_cwd = os.getcwd()
    try:
        os.chdir(workspace_path)
        result = subprocess.run(claude_args, check=False)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:
        print(f"Error running claude: {e}")
        sys.exit(1)
    finally:
        os.chdir(original_cwd)

if __name__ == "__main__":
    main()