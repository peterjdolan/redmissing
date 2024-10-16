import argparse
import requests
import os
import sys
import time
from tqdm import tqdm

API_KEY = os.environ.get('REDACTED_API_KEY')
API_URL = 'https://redacted.ch/ajax.php'

def search_albums(query, api_key):
    params = {
        'action': 'browse',
        'searchstr': query
    }
    headers = {
        'Authorization': api_key
    }
    
    response = requests.get(API_URL, params=params, headers=headers)
    response.raise_for_status()
    
    results = response.json()['response']['results']
    return results

def format_result(result):
    artist = result.get('artist', 'Unknown Artist')
    album = result.get('groupName', 'Unknown Album')
    year = result.get('groupYear', 'Unknown Year')
    return f"{artist} - {album} ({year})"

def main():
    parser = argparse.ArgumentParser(description='Search Redacted for missing albums')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='File containing search queries, one per line (default: stdin)')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout,
                        help='File to write missing albums (default: stdout)')
    args = parser.parse_args()

    if not API_KEY:
        print("Error: REDACTED_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    queries = args.input.readlines()

    missing_albums = []

    for query in tqdm(queries, desc="Searching for missing albums", unit="album", file=sys.stderr):
        query = query.strip()
        if not query:
            continue
        
        try:
            results = search_albums(query, API_KEY)
            if not results:
                missing_albums.append(query)
        except requests.RequestException as e:
            print(f"Error searching for '{query}': {e}", file=sys.stderr)
        
        time.sleep(1)  # Rate limiting

    for album in missing_albums:
        args.output.write(f"{album}\n")

    print(f"\nSearch complete. {len(missing_albums)} missing albums written to output", file=sys.stderr)

if __name__ == '__main__':
    main()