import re

def extract_tags_attributes(n, html_lines):
    # Regular expression to match HTML tags and their attributes
    tag_pattern = re.compile(r'<(\w+)(.*?)>')
    attribute_pattern = re.compile(r'(\w+)=["\']')  # Match attribute names followed by = and a quote
    tag_attributes = {}
    
    for line in html_lines:
        matches = tag_pattern.findall(line)
        for tag, attributes in matches:
            # Extract attribute names and ensure uniqueness
            attr_names = sorted(set(attribute_pattern.findall(attributes)))
            if tag in tag_attributes:
                tag_attributes[tag].update(attr_names)
            else:
                tag_attributes[tag] = set(attr_names)
    
    # Create sorted list of tag-attribute pairs
    sorted_tags = sorted(tag_attributes.keys())
    
    for tag in sorted_tags:
        attr_list = sorted(tag_attributes[tag])
        attr_str = ','.join(attr_list)
        print(f"{tag}:{attr_str}")
                
if __name__ == "__main__":
    # Sample input
    n = int(input())
    html_lines = [input().strip() for _ in range(n)]
    
    extract_tags_attributes(n, html_lines)
