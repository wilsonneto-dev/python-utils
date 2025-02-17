import os
import markdown
import pdfkit 

dir_list = os.listdir()
mds = []

for file in dir_list:
    if file.endswith('.md'):
        mds.append(file)

for md in mds:
    print(f'Converting {md}...')
    f = open(md, 'r', encoding="utf-8")
    html = markdown.markdown(f.read())
    with open(f'./out/{md}.html', 'w+') as f:
        f.write(html)
    pdfkit.from_string(html, f'./out/{md}.pdf')
    print(f'Done. Saved in ./out/{md}.pdf')
