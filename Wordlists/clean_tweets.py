import re
import emoji
import sys
import os

def clean_tweet(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\.\S+', '', text)
    # Remove user mentions (@username)
    text = re.sub(r'@\w+', '', text)
    # Remove emojis
    text = emoji.replace_emoji(text, replace='')
    # Remove extra whitespace left behind
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def main():
    input_file = 'tweets.txt'
    output_file = 'cleaned_tweets.txt'

    # Use absolute paths based on the script location for safety
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, input_file)
    output_path = os.path.join(script_dir, output_file)

    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)

    print(f"Reading from {input_path}...")
    
    with open(input_path, 'r', encoding='utf-8') as f_in, \
         open(output_path, 'w', encoding='utf-8') as f_out:
        
        for line in f_in:
            cleaned_line = clean_tweet(line)
            if cleaned_line: # Avoid writing empty lines if they were just links/mentions
                f_out.write(cleaned_line + '\n')
                
    print(f"Cleaning complete! Saved to {output_path}")

if __name__ == '__main__':
    main()
