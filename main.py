import re

def regex_query_tool():
    print("Welcome to the Regex Query Tool!")

    while True:
        regex_pattern = input("Enter a regular expression pattern (or 'exit' to quit): ")
        
        if regex_pattern.lower() == 'exit':
            print("Exiting the Regex Query Tool. Goodbye!")
            break

        try:
            regex = re.compile(regex_pattern)
        except re.error as e:
            print(f"Error: {e}")
            continue

        test_string = input("Enter a string to test the regular expression: ")

        if regex.match(test_string):
            print("Match found!")
        else:
            print("No match.")

if __name__ == "__main__":
    regex_query_tool()
