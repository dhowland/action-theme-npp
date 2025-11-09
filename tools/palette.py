
import sys
import os.path

# even spacing around RGB, with higher white balance, blues washed out
# r_vals = ('77', 'BB', 'FF')
# g_vals = ('77', 'BB', 'FF')
# b_vals = ('77', 'BB', 'FF')
# crude luminance balance that deepens blues
r_vals = ('66', 'B3', 'FF')
g_vals = ('55', 'AA', 'FF')
b_vals = ('77', 'BB', 'FF')

# 12 color wheel (primary, secondary, tertiary)
colors = {
    'pink'   : (2,0,1),
    'red'    : (2,0,0),     # primary   (R)
    'orange' : (2,1,0),
    'yellow' : (2,2,0),     # secondary (Y)
    'mint'   : (1,2,0),
    'green'  : (0,2,0),     # primary   (G)
    'aqua'   : (0,2,1),
    'cyan'   : (0,2,2),     # secondary (C)
    'blue'   : (0,1,2),
    'indigo' : (0,0,2),     # primary   (B)
    'purple' : (1,0,2),
    'magenta': (2,0,2),     # secondary (M)
}

if len(sys.argv) != 2:
    print("usage: python palette.py <output_path>")
    sys.exit(1)

output_path = os.path.join(sys.argv[1], 'palette.html')

with open(output_path, 'w') as f:
    f.write('<html>\n')
    f.write('<body>\n')
    
    f.write('<table>\n')
    f.write('<tr><td>R/GB</td>')
    for v in r_vals:
        f.write(f'<td>{v}</td>')
    f.write('</tr>\n')
    for g in g_vals:
        for b in b_vals:
            f.write(f'<tr><td>{g}{b}</td>')
            for r in r_vals:
                f.write(f'<td bgcolor="{r}{g}{b}">{r}{g}{b}</td>')
            f.write('</tr>\n')
    f.write('</table>\n')
    
    f.write('<table>')
    for color in colors:
        ri,gi,bi = colors[color]
        r,g,b = (r_vals[ri], g_vals[gi], b_vals[bi])
        f.write(f'<tr><td bgcolor="{r}{g}{b}">"{color}":"#{r}{g}{b}",</td></tr>\n')
    f.write('</table>\n')
    
    f.write('</body>\n')
    f.write('</html>\n')
