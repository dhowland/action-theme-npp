
import re
import sys
import json
import os.path

if len(sys.argv) != 4:
    print("usage: python stylers.py <stylers_template> <input_json> <output_xml>")
    sys.exit(1)

template_path = sys.argv[1]
input_path = sys.argv[2]
output_path = sys.argv[3]

with open(template_path) as f:
    template = f.read()

with open(input_path) as f:
    try:
        config = json.load(f)
    except json.decoder.JSONDecodeError as e:
        print(f'Error: input JSON: {str(e)}')
        sys.exit(1)

colors = config['colors']
theme = config['styles'].copy()
dirty = True
while dirty:
    dirty = False
    for key,val in theme.items():
        if m := re.match(r"#?([a-fA-F0-9]{6})", val):
            rgb = m.group(1)
            theme[key] = rgb
        elif m := re.match(r"\$([a-zA-Z_][a-zA-Z0-9_-]+)", val):
            var = m.group(1)
            if var in colors:
                theme[key] = colors[var]
                dirty = True
            elif var in theme:
                theme[key] = theme[var]
                dirty = True
            else:
                print(f'Error: variable {var} not found')
                sys.exit(1)
        else:
            print(f'Error: invalid color spec {val}')
            sys.exit(1)
theme.update(config['font'])

with open(output_path, 'w') as f:
    try:
        f.write(template.format(**theme))
    except KeyError as e:
        print(f'Error: style {str(e)} not found')
        sys.exit(1)

root,ext = os.path.splitext(output_path)
colors_path = root + '_colors.html'
with open(colors_path, 'w') as f:
    f.write('<html>\n')
    f.write('<body>\n')
    f.write('<table>\n')
    for key,val in theme.items():
        f.write(f'<tr><td>{key}</td><td bgcolor="{val}">{val}</td></tr>')
    f.write('</table>\n')
    f.write('</body>\n')
    f.write('</html>\n')