import yaml, json, requests
from time import sleep

def get_citation_count_s2(doi):
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
    params = {"fields": "citationCount"}
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, params=params, headers=headers)
    resp.raise_for_status()
    return resp.json().get("citationCount", 0)

def main():
    with open("_data/dois.yml", "r") as f:
        dois = yaml.safe_load(f)

    ss_data = {}
    for doi in dois:
        try:
            count = get_citation_count_s2(doi)
            ss_data[doi] = count
        except Exception as e:
            print(f"[!] {doi} 抓取失败：{e}")
            ss_data[doi] = None
        sleep(1)

    with open("_data/ss_data.json", "w") as f:
        json.dump(ss_data, f, indent=2, ensure_ascii=False)
    print("✅ _data/ss_data.json 更新完毕")

if __name__ == "__main__":
    main()