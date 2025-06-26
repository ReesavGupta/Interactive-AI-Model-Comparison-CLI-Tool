#!/usr/bin/env python3
"""
Cleanup script to remove cached models and temporary files.
Run this to minimize repository size before committing.
"""

import os
import shutil
import sys
from pathlib import Path

def remove_directory(path):
    """Safely remove a directory if it exists."""
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            print(f"✅ Removed: {path}")
            return True
        except Exception as e:
            print(f"❌ Failed to remove {path}: {e}")
            return False
    else:
        print(f"⚠️  Not found: {path}")
        return True

def remove_file(path):
    """Safely remove a file if it exists."""
    if os.path.exists(path):
        try:
            os.remove(path)
            print(f"✅ Removed: {path}")
            return True
        except Exception as e:
            print(f"❌ Failed to remove {path}: {e}")
            return False
    else:
        print(f"⚠️  Not found: {path}")
        return True

def get_directory_size(path):
    """Get the total size of a directory in MB."""
    if not os.path.exists(path):
        return 0
    
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(filepath)
            except (OSError, FileNotFoundError):
                pass
    return total_size / (1024 * 1024)  # Convert to MB

def main():
    print("🧹 Cleaning up repository...")
    print("=" * 50)
    
    # Directories to clean
    cache_dirs = [
        ".cache",
        "cache",
        "__pycache__",
        ".venv",
        "transformers_cache",
        os.path.expanduser("~/.cache/huggingface"),
    ]
    
    # Files to clean
    temp_files = [
        ".env",
        "*.log",
        "*.tmp",
    ]
    
    total_freed = 0
    
    # Remove cache directories
    for cache_dir in cache_dirs:
        size_before = get_directory_size(cache_dir)
        if remove_directory(cache_dir):
            total_freed += size_before
    
    # Remove Python cache files
    for root, dirs, files in os.walk("."):
        for dir_name in dirs[:]:  # Use slice to avoid modification during iteration
            if dir_name == "__pycache__":
                cache_path = os.path.join(root, dir_name)
                size_before = get_directory_size(cache_path)
                if remove_directory(cache_path):
                    total_freed += size_before
                dirs.remove(dir_name)  # Don't recurse into removed directory
    
    print("=" * 50)
    print(f"🎉 Cleanup complete! Freed approximately {total_freed:.1f} MB")
    print("\n📝 Repository is now minimal and ready for Git!")
    print("\n💡 Tips:")
    print("   - Models will be downloaded again on first use")
    print("   - Add your .env file with API keys before running")
    print("   - Use 'git status' to see what files are tracked")

if __name__ == "__main__":
    main()
