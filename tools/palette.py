
import sys
import os.path

# even spacing around RGB, with higher white balance, blues washed out
# r_vals = ('77', 'BB', 'FF')
# g_vals = ('77', 'BB', 'FF')
# b_vals = ('77', 'BB', 'FF')
# crude luminance balance that deepens blues
# r_vals = ('66', 'B3', 'FF')
# g_vals = ('55', 'AA', 'FF')
# b_vals = ('77', 'BB', 'FF')
# even spacing, but deeper
r_vals = ('55', 'AA', 'FF')
g_vals = ('55', 'AA', 'FF')
b_vals = ('55', 'AA', 'FF')


colors = {
    # 'dark'       : (0,0,0),
    'violet'     : (0,0,1),
    'indigo'     : (0,0,2),     # primary   (B)
    'blue'       : (0,1,2),
    'teal'       : (0,1,1),
    'hunter'     : (0,1,0),
    'green'      : (0,2,0),     # primary   (G)
    'aqua'       : (0,2,1),
    'cyan'       : (0,2,2),     # secondary (C)
    'sky'        : (1,2,2),
    'mint'       : (1,2,1),
    'lime'       : (1,2,0),
    'olive'      : (1,1,0),
    # 'gray'       : (1,1,1),
    'periwinkle' : (1,1,2),
    'purple'     : (1,0,2),
    'plum'       : (1,0,1),
    'rose'       : (1,0,0),
    'red'        : (2,0,0),     # primary   (R)
    'pink'       : (2,0,1),
    'magenta'    : (2,0,2),     # secondary (M)
    'mauve'      : (2,1,2),
    'coral'      : (2,1,1),
    'orange'     : (2,1,0),
    'yellow'     : (2,2,0),     # secondary (Y)
    'cream'      : (2,2,1),
    # 'light'      : (2,2,2),
}

def luminance(r, g, b):
    def norm(v):
        v = int(v, 16)
        return pow((v/0xff), 2.2)
    return (0.2126 * norm(r) + 0.7152 * norm(g) + 0.0722 * norm(b))

if len(sys.argv) != 2:
    print("usage: python palette.py <output_path>")
    sys.exit(1)

output_path = os.path.join(sys.argv[1], 'palette.html')

with open(output_path, 'w') as f:
    f.write('<html>\n')
    f.write('<body>\n')
    
    # f.write('<table>\n')
    # f.write('<tr><td>R/GB</td>')
    # for v in r_vals:
        # f.write(f'<td>{v}</td>')
    # f.write('</tr>\n')
    # for g in g_vals:
        # bv = reversed(b_vals) if g == g_vals[1] else b_vals
        # for b in bv:
            # f.write(f'<tr><td>{g}{b}</td>')
            # for r in r_vals:
                # f.write(f'<td bgcolor="{r}{g}{b}">{r}{g}{b}</td>')
            # f.write('</tr>\n')
    # f.write('</table>\n')
    
    f.write('<table>')
    for color in colors:
        ri,gi,bi = colors[color]
        r,g,b = (r_vals[ri], g_vals[gi], b_vals[bi])
        y = luminance(r, g, b)
        f.write(f'<tr><td>{y:.2f}</td><td bgcolor="{r}{g}{b}">"{color}":"#{r}{g}{b}",</td></tr>\n')
    f.write('</table>\n')
    
    f.write('</body>\n')
    f.write('</html>\n')
