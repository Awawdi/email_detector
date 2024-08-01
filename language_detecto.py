import re
import sys

def detect_language(source_code):
    c_pattern = r'(?s).*(#\\s*include\\s*(<\\s*[\\w/]+(\\.\\w+)?\\s*>|\"[\\w/]+(\\.\\w+)?\"\\s*))(?s).*'
    java_pattern = r'(?s).*(^(public\\s+|private\\s+|protected\\s+)*.*\\w+\\(.*?\\)\\s*\\{|import\\s+[\\w\\.\\*]+;)(?s).*'
    python_pattern = r'(?s).*(^print\\s\".*\"$|^#\\s.*$|def\\s.*$|^if\\s[^()]+:)(?s).*'
    
    # Check for each language pattern
    if java_pattern.search(source_code):
        return "Java"
    elif c_pattern.search(source_code):
        return "C"
    elif python_pattern.search(source_code):
        return "Python"
 

if __name__ == "__main__":
   
    source_code = ''.join(sys.stdin.readlines())
    # Detect language
    language = detect_language(source_code)
    print(language)
