#!/usr/bin/env python3
import argparse
import sys
from commands.cache import clean_cache
from commands.logs import clean_logs
from commands.xcode import clean_xcode
from commands.trash import clean_trash
from commands.bigfiles import find_bigfiles
from commands.duplicates import find_duplicates
from commands.status import show_status
from commands.scan import scan_system

def main():
    parser = argparse.ArgumentParser(prog='maccleaner', description='Mac CLI Cleanup Utility')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    subparsers.add_parser('scan', help='Scan system for cleanable files')
    subparsers.add_parser('status', help='Show disk usage status')
    
    clean_parser = subparsers.add_parser('clean', help='Clean specified category')
    clean_parser.add_argument('category', choices=['cache', 'logs', 'xcode', 'trash', 'all'],
                            help='Category to clean')
    clean_parser.add_argument('-f', '--force', action='store_true', help='Skip confirmation')
    
    subparsers.add_parser('bigfiles', help='Find large files')
    subparsers.add_parser('duplicates', help='Find duplicate files')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    commands = {
        'scan': lambda: scan_system(),
        'status': lambda: show_status(),
        'clean': lambda: handle_clean(args),
        'bigfiles': lambda: find_bigfiles(),
        'duplicates': lambda: find_duplicates(),
    }
    
    commands[args.command]()

def handle_clean(args):
    categories = {
        'cache': clean_cache,
        'logs': clean_logs,
        'xcode': clean_xcode,
        'trash': clean_trash,
    }
    
    if args.category == 'all':
        for cmd in categories.values():
            cmd(force=args.force)
    else:
        categories[args.category](force=args.force)

if __name__ == '__main__':
    main()
