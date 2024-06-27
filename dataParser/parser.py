from html.parser import HTMLParser
import re
import csv


class HTMLTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.despace_re = re.compile(r'\s+')
        self.current_row = []
        self.table_data = []  # Initialize table_data here
        self.in_cell = False

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.current_row = []  # Start a new row
        elif tag == "td" or tag == "th":
            self.in_cell = True

    def handle_endtag(self, tag):
        if tag == "td" or tag == "th":
            self.in_cell = False
        elif tag == "tr":
            self.table_data.append(self.current_row)  # End of a row

    def handle_data(self, data):
        if self.in_cell:
            clean_data = self.despace_re.sub(' ', data).strip()
            self.current_row.append(clean_data)


# Read the HTML file
with open('AsianMarket.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
parser = HTMLTableParser()
parser.feed(html_content)

# Write the parsed data to a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    for row in parser.table_data:
        csv_writer.writerow(row)

print("CSV file has been saved as 'output.csv'.")
