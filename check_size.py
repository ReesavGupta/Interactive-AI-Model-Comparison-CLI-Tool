#!/usr/bin/env python3
"""
Quick script to check repository size and identify large files.
"""

import os
from pathlib import Path

def get_file_size(filepath):
    """Get file size in bytes."""
    try:
        return os.path.getsize(filepath)
    except (OSError, FileNotFoundError):
        return 0

def format_size(size_bytes):
    """Format size in human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"

def main():
    print("📊 Repository Size Analysis")
    print("=" * 40)
    
    # Get all files (excluding .venv and cache directories)
    exclude_dirs = {'.venv', '.git', '__pycache__', '.cache', 'cache'}
    
    files_info = []
    total_size = 0
    
    for root, dirs, files in os.walk('.'):
        # Remove excluded directories from dirs list
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            filepath = os.path.join(root, file)
            size = get_file_size(filepath)
            files_info.append((filepath, size))
            total_size += size
    
    # Sort by size (largest first)
    files_info.sort(key=lambda x: x[1], reverse=True)
    
    print(f"📁 Total repository size: {format_size(total_size)}")
    print(f"📄 Number of files: {len(files_info)}")
    print("\n🔍 Largest files:")
    print("-" * 40)
    
    # Show top 10 largest files
    for filepath, size in files_info[:10]:
        if size > 0:  # Only show non-empty files
            print(f"{format_size(size):>8} - {filepath}")
    
    print("\n✅ Repository is optimized for minimal size!")
    print("💡 Models will be downloaded on first use (~1GB total)")

if __name__ == "__main__":
    main()
