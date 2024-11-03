from jinja2 import Environment, FileSystemLoader
import json

# Load the data from the JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    
# Load the Jinja2 template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render the template with the data
html_output = template.render(data)

# Save the rendered HTML to a file
with open('report.html', 'w') as html_file:
    html_file.write(html_output)

print("HTML report generated successfully!")