import re
import sys

def extract_comments(source_code):
    # Define regular expressions for single-line and multi-line comments
    single_line_comment_pattern = r'//.*'
    multi_line_comment_pattern = r'/\*[\s\S]*?\*/'

    combined_pattern = rf'({single_line_comment_pattern})|({multi_line_comment_pattern})'
    
    comments = re.findall(combined_pattern, source_code)
    def normalize_multi_line_comment(comment):
        """
        Removes leading white spaces from each line of a multi-line comment.

        Parameters:
        comment (str): A multi-line comment as a string.

        Returns:
        str: The multi-line comment with leading white spaces removed.
        """
        # Split the comment into lines
        lines = comment.split('\n')
        # Strip leading white space from each line
        stripped_lines = [line.lstrip() for line in lines]
        # Join the lines back into a single string
        return '\n'.join(stripped_lines)

    # Process comments
    result_comments = []
    for single_line, multi_line in comments:
        if single_line:
            # Add single-line comments directly
            result_comments.append(single_line)
        elif multi_line:
            # Normalize and add multi-line comments
            result_comments.append(normalize_multi_line_comment(multi_line))

    # Join all comments into a single string separated by newlines
    return '\n'.join(result_comments)


# Input handling
file_path = 'input.txt'

    # Read the content of the file
with open(file_path, 'r') as file:
    source_code = file.read()
        
print(extract_comments(source_code))
