import requests
from bs4 import BeautifulSoup
import time
import random

_USER_AGENTS = [
    # Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    # Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Mozilla/5.0 (X11; Linux i686; rv:107.0) Gecko/20100101 Firefox/107.0",
    # Edge
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46",
    # Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
]

def _send_request(url, max_retries=3):
    """
    Internal helper to send a request with retries and exponential backoff.
    """
    for attempt in range(max_retries):
        try:
            # Add a small random delay to mimic human behavior
            time.sleep(random.uniform(1, 3))

            headers = {"User-Agent": random.choice(_USER_AGENTS)}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                return response
            elif response.status_code == 429:
                print(f"Rate limit exceeded (429). Retrying in {2 ** attempt} seconds...")
                time.sleep(2 ** attempt)
            else:
                print(f"Failed to fetch data. HTTP Status code: {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {2 ** attempt} seconds...")
                time.sleep(2 ** attempt)
            else:
                return None
    print("Max retries reached. Failed to fetch data.")
    return None


def google_scholar_search(query: str, num_results=5):
    """
    Function to search Google Scholar using a simple keyword query.

    Parameters:
    query (str): The search query (e.g., paper title or author).
    num_results (int): The number of results to retrieve.

    Returns:
    list: A list of dictionaries containing search results.
    """
    # Prepare the search URL
    search_url = f"https://scholar.google.com/scholar?q={query.replace(' ', '+')}"

    # Send the GET request to Google Scholar
    response = _send_request(search_url)
    if not response:
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the articles in the search results
    results = []
    count = 0

    # Find the results on the page
    for item in soup.find_all('div', class_='gs_ri'):
        if count >= num_results:
            break

        title_tag = item.find('h3', class_='gs_rt')
        title = title_tag.get_text() if title_tag else 'No title available'

        link = title_tag.find('a')['href'] if title_tag and title_tag.find('a') else 'No link available'

        authors_tag = item.find('div', class_='gs_a')
        authors = authors_tag.get_text() if authors_tag else 'No authors available'

        abstract_tag = item.find('div', class_='gs_rs')
        abstract = abstract_tag.get_text() if abstract_tag else 'No abstract available'

        result_data = {
            'Title': title,
            'Authors': authors,
            'Abstract': abstract,
            'URL': link
        }
        results.append(result_data)
        count += 1

    return results

def advanced_google_scholar_search(query:str, author=None, year_range=None, num_results=5):
    """
    Function to search Google Scholar using advanced search filters (e.g., author, year range).

    Parameters:
    query (str): The search query (e.g., paper title or topic).
    author (str): The author's name to filter the results (default is None).
    year_range (tuple): A tuple (start_year, end_year) to filter the results by publication year (default is None).
    num_results (int): The number of results to retrieve.

    Returns:
    list: A list of dictionaries containing search results.
    """
    # Prepare the advanced search URL
    search_url = "https://scholar.google.com/scholar?"
    
    # Build the search query
    search_params = {'q': query.replace(' ', '+')}
    if author:
        search_params['as_auth'] = author
    if year_range:
        start_year, end_year = year_range
        search_params['as_ylo'] = start_year  # Start year
        search_params['as_yhi'] = end_year  # End year
    
    # Encode the search parameters into the URL
    search_url += '&'.join([f"{key}={value}" for key, value in search_params.items()])

    # Send the GET request to Google Scholar
    response = _send_request(search_url)
    if not response:
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the articles in the search results
    results = []
    count = 0

    # Find the results on the page
    for item in soup.find_all('div', class_='gs_ri'):
        if count >= num_results:
            break

        title_tag = item.find('h3', class_='gs_rt')
        title = title_tag.get_text() if title_tag else 'No title available'

        link = title_tag.find('a')['href'] if title_tag and title_tag.find('a') else 'No link available'

        authors_tag = item.find('div', class_='gs_a')
        authors = authors_tag.get_text() if authors_tag else 'No authors available'

        abstract_tag = item.find('div', class_='gs_rs')
        abstract = abstract_tag.get_text() if abstract_tag else 'No abstract available'

        result_data = {
            'Title': title,
            'Authors': authors,
            'Abstract': abstract,
            'URL': link
        }
        results.append(result_data)
        count += 1

    return results


def query_constraint_database(search_query: str = None) -> list:
    """
    Query the Constraint Database for physical laws, ecological limits,
    and experimental feasibility rules relevant to marine ecology.
    
    Parameters:
    search_query (str): Optional keyword to filter constraints.
    
    Returns:
    list: A list of relevant constraints.
    """
    import json
    import os
    db_path = os.path.join(os.path.dirname(__file__), "ConstraintDatabase.json")
    if not os.path.exists(db_path):
        return []
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            constraints = [data]
        elif isinstance(data, list):
            constraints = data
        else:
            constraints = []
        
        if search_query:
            query_lower = search_query.lower()
            filtered = []
            for c in constraints:
                text_to_check = f"{c.get('description', '')} {c.get('implication', '')} {c.get('layer', '')}".lower()
                if 'parameters' in c and isinstance(c['parameters'], dict):
                    text_to_check += f" {c['parameters'].get('species', '')}".lower()
                if query_lower in text_to_check:
                    filtered.append(c)
            return filtered
        return constraints
    except Exception as e:
        print(f"Error reading constraint database: {e}")
        return []


def add_constraint_to_database(
    constraint_id: str,
    layer: str,
    description: str,
    implication: str,
    parameters: dict = None,
    source: str = "PI Agent (auto-discovered)",
) -> dict:
    """
    Add a new ecological or physical constraint fact to the Constraint Database.

    Call this tool whenever a sub-agent discovers a new, well-sourced fact (e.g., a
    species tolerance limit, a depth threshold, or a chemical threshold) that is not
    already present in the database. The fact will be persisted for future agent runs.

    Parameters:
    constraint_id (str): A unique identifier following the pattern LAYER-TYPE-NNN
                         (e.g., "ECO-SALT-003"). Must not duplicate an existing ID.
    layer         (str): Constraint category, e.g. "Layer 2: Ecological Limits" or
                         "Layer 1: Physical Laws".
    description   (str): One-sentence description of the constraint.
    implication   (str): How this constraint limits experimental or simulation design.
    parameters    (dict): Optional key/value pairs with numeric thresholds or species names.
    source        (str): Citation or agent that discovered this fact.

    Returns:
    dict: {"status": "added"|"duplicate"|"error", "message": str}
    """
    import json, os

    db_path = os.path.join(os.path.dirname(__file__), "ConstraintDatabase.json")

    # Load existing database
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            constraints: list = json.load(f)
        if not isinstance(constraints, list):
            constraints = [constraints]
    except Exception as e:
        return {"status": "error", "message": f"Failed to read database: {e}"}

    # Check for duplicate IDs
    existing_ids = {c.get("constraint_id") for c in constraints}
    if constraint_id in existing_ids:
        return {
            "status": "duplicate",
            "message": f"Constraint '{constraint_id}' already exists in the database. No changes made.",
        }

    # Build new entry
    new_entry = {
        "constraint_id": constraint_id,
        "layer": layer,
        "description": description,
        "implication": implication,
        "source": source,
    }
    if parameters:
        new_entry["parameters"] = parameters

    # Persist
    constraints.append(new_entry)
    try:
        with open(db_path, "w", encoding="utf-8") as f:
            json.dump(constraints, f, indent=2, ensure_ascii=False)
    except Exception as e:
        return {"status": "error", "message": f"Failed to write database: {e}"}

    return {
        "status": "added",
        "message": f"Constraint '{constraint_id}' successfully added to the Constraint Database.",
    }

print(google_scholar_search("artificial reefs", num_results=1))