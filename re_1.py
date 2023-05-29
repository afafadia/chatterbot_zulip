import re

pattern = r"\b(?:documents?\b|case\sdetails?\b|patents?\b\sdetails?\b|inventors?\b|claims?\b|recent|projects?\b)\b"

test_string = "document and case detail and patents details and inventors and claims and projects"
result = re.match(pattern, test_string)

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")
