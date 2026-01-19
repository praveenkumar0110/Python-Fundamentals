fake_site = {
    "A01": ["A01.0", "A01.1", "A01.2"],
    "A01.0": ["A01.01", "A01.02"],
    "A01.1": [],
    "A01.2": [],
    "A01.01": [],
    "A01.02": []
}

def scrape(code, depth=0):
    indent = "  " * depth
    print(f"{indent}Scraping code: {code}")

    children = fake_site.get(code, [])

    # Leaf node (no children)
    if not children:
        print(f"{indent}No more subcodes for {code}. Returning.")
        return {
            "code": code,
            "subcodes": []
        }

    print(f"{indent}Found {len(children)} children → {children}")

    # Build node
    node = {
        "code": code,
        "subcodes": []
    }

    # Recursion for each child
    for child in children:
        print(f"{indent}Going inside → {child}")
        child_node = scrape(child, depth + 1)
        node["subcodes"].append(child_node)

    print(f"{indent}Finished scraping code: {code}")
    return node


result = scrape("A01")
print("\nFinal Tree Structure:")
print(result)
