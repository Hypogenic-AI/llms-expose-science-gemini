
import requests
import xml.etree.ElementTree as ET
import argparse
import time
from tqdm import tqdm

def fetch_arxiv_abstracts(query, max_results=1000):
    """
    Fetches abstracts from the arXiv API.
    """
    url = 'http://export.arxiv.org/api/query'
    papers = []
    start = 0
    batch_size = 100

    with tqdm(total=max_results, desc="Fetching arXiv abstracts") as pbar:
        while start < max_results:
            params = {
                'search_query': query,
                'start': start,
                'max_results': min(batch_size, max_results - start),
                'sortBy': 'submittedDate',
                'sortOrder': 'descending'
            }
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                
                root = ET.fromstring(response.content)
                entries = root.findall('{http://www.w3.org/2005/Atom}entry')
                
                if not entries:
                    break

                for entry in entries:
                    title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
                    summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
                    papers.append({'title': title, 'abstract': summary})
                    pbar.update(1)

                start += len(entries)
                time.sleep(3) # Be nice to the API

            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                break
            except ET.ParseError as e:
                print(f"Failed to parse XML: {e}")
                break

    return papers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fetch paper abstracts from arXiv.")
    parser.add_argument("--query", type=str, required=True, help="Search query for arXiv.")
    parser.add_argument("--max_results", type=int, default=500, help="Maximum number of abstracts to fetch.")
    parser.add_argument("--output_file", type=str, required=True, help="Path to save the output JSON file.")
    
    args = parser.parse_args()

    print(f"Fetching {args.max_results} abstracts for query: '{args.query}'")
    abstracts = fetch_arxiv_abstracts(args.query, args.max_results)

    if abstracts:
        import pandas as pd
        df = pd.DataFrame(abstracts)
        df.to_json(args.output_file, orient='records', lines=True)
        print(f"Successfully saved {len(abstracts)} abstracts to {args.output_file}")
    else:
        print("No abstracts fetched.")
