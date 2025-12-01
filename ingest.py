import requests
import time
#
# Basic request helpers for interacting with the Mod.io Baldur's Gate 3 API.
# All higher-level processing, version-diffing, and export logic has been
# intentionally removed so this module focuses purely on HTTP requests.

API_KEY = "36ac348c7596cbe7c2d5bef33e32f487"
BASE_URL = "https://u-39690756.modapi.io/v1/games/@baldursgate3/mods"

def fetch_mod_files(game_id, mod_id, files_cache, platform_status=None):
    """Fetch all modfiles for a specific mod to determine version differences."""
    cache_key = f"{mod_id}_{platform_status or 'default'}"
    
    # Check cache first
    if cache_key in files_cache:
        return files_cache[cache_key]
    
    url = f"https://u-39690756.modapi.io/v1/games/{game_id}/mods/{mod_id}/files"
    params = {
        'api_key': API_KEY,
        '_limit': 100,
        '_sort': '-date_added'  # Newest first
    }
    
    if platform_status:
        params['platform_status'] = platform_status
    
    try:
        response = requests.get(url, params=params, timeout=30)
        
        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 60))
            print(f"Rate limit hit fetching files. Sleeping for {retry_after} seconds...")
            time.sleep(retry_after + 1)
            return fetch_mod_files(game_id, mod_id, files_cache, platform_status)  # Retry
            
        response.raise_for_status()
        data = response.json()
        files = data.get('data', [])
        
        print(f"  Fetched {len(files)} files for mod {mod_id} with platform_status={platform_status}")
        
        # Cache the result
        files_cache[cache_key] = files
        
        # Rate limit
        time.sleep(0.2)
        
        return files
        
    except Exception as e:
        print(f"Error fetching files for mod {mod_id} with platform_status={platform_status}: {e}")
        return []

def fetch_mods():
    mods = []
    offset = 0
    limit = 100
    
    print("Starting ingestion...")
    
    while True:
        print(f"Fetching offset {offset}...")
        params = {
            'api_key': API_KEY,
            '_limit': limit,
            '_offset': offset,
            '_sort': '-date_updated',
            'platforms': 'ps5'
        }
        
        try:
            response = requests.get(BASE_URL, params=params, timeout=30)
            
            if response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 60))
                print(f"Rate limit hit. Sleeping for {retry_after} seconds...")
                time.sleep(retry_after + 1)
                continue
                
            response.raise_for_status()
            data = response.json()
            
            page_mods = data.get('data', [])
            if not page_mods:
                break
                
            mods.extend(page_mods)
            
            if len(page_mods) < limit:
                break
                
            offset += limit
            # Rate limit: 60 req/min = 1 req/sec for user keys. 
            # We use 0.1s here to be faster for small batches, relying on 429 handling if we hit limits.
            time.sleep(0.1) 
            
        except Exception as e:
            print(f"Error fetching data: {e}")
            break
            
    return mods

