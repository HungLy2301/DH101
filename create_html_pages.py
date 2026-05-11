#!/usr/bin/env python3
import os
import re

BASE_DIR = '/Users/hungly/Documents/GitHub/DH101/DH101'
MAKES_DIR = os.path.join(BASE_DIR, 'makes')
REFLECTIONS_DIR = os.path.join(BASE_DIR, 'reflections')
DOCS_DIR = os.path.join(BASE_DIR, 'docs')

weeks = {
    'week01': {'title': 'Week 1: Reverse Engineering', 'subtitle': 'Learning to think about embedded systems and decisions'},
    'week02': {'title': 'Week 2: AI & Identity', 'subtitle': 'Exploring AI-generated representations of personal identity'},
    'week03': {'title': 'Week 3: Selfie & Identity', 'subtitle': 'Digital self-representation in networked spaces'},
    'week04': {'title': 'Week 4: Comic & Storytelling', 'subtitle': 'Narrative structures and visual meaning-making'},
    'week05': {'title': 'Text Analysis: How Machines Read', 'subtitle': 'Comparing computational and AI approaches to textual meaning'},
    'week06': {'title': 'Week 6: Text & Distant Reading', 'subtitle': 'Computational analysis and textual patterns'},
    'week07': {'title': 'Week 7: Mapping AI Worlds', 'subtitle': 'Critical infrastructure mapping and power analysis'},
    'week08': {'title': 'Week 8: Networks of Knowledge & Power', 'subtitle': 'Understanding systems, structures, and control'},
    'week09': {'title': 'Week 9: Bots & Generators', 'subtitle': 'Creative systems and algorithmic curation'},
    'week10': {'title': 'Week 10: Games & Play', 'subtitle': 'Interactive narrative and procedural rhetoric'},
    'week11': {'title': 'Week 11: AI & Labor', 'subtitle': 'Automation, work, and human costs'},
    'week12': {'title': 'Week 12: AI & Ecology', 'subtitle': 'Environmental dimensions of computation'},
    'week13': {'title': 'Week 13: Futures of AI & Humanity', 'subtitle': 'Speculating on possible futures'},
}


def markdown_to_html_content(md_content):
    md_content = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', md_content, flags=re.MULTILINE)

    md_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', md_content)
    md_content = re.sub(r'__(.*?)__', r'<strong>\1</strong>', md_content)
    md_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', md_content)
    md_content = re.sub(r'_(.*?)_', r'<em>\1</em>', md_content)

    md_content = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1" />', md_content)
    md_content = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', md_content)

    md_content = re.sub(r'> (.*?)$', r'<blockquote>\1</blockquote>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', md_content, flags=re.DOTALL)
    md_content = re.sub(r'`(.*?)`', r'<code>\1</code>', md_content)

    lines = md_content.split('\n')
    result = []
    in_list = False
    current_block = []

    for line in lines:
        line = line.strip()
        if line.startswith('<h') or line.startswith('<pre') or line.startswith('<blockquote'):
            if current_block:
                result.append('<p>' + ' '.join(current_block) + '</p>')
                current_block = []
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(line)
        elif re.match(r'^[-*+] ', line):
            if current_block:
                result.append('<p>' + ' '.join(current_block) + '</p>')
                current_block = []
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append('<li>' + line[2:].strip() + '</li>')
        elif line == '':
            if current_block:
                result.append('<p>' + ' '.join(current_block) + '</p>')
                current_block = []
            if in_list:
                result.append('</ul>')
                in_list = False
        else:
            current_block.append(line)

    if current_block:
        result.append('<p>' + ' '.join(current_block) + '</p>')
    if in_list:
        result.append('</ul>')

    return '\n    '.join(result)


def read_markdown(filename, folder='makes'):
    path = os.path.join(BASE_DIR, folder, f'{filename}.md')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ''


def create_html_page(page_id, title, subtitle, folder='makes', output_filename=None):
    if output_filename is None:
        output_filename = f'{page_id}.html'
    md_content = read_markdown(page_id, folder)
    if not md_content:
        content = ''
    else:
        lines = md_content.splitlines()
        if lines and lines[0].startswith('# '):
            lines = lines[1:]
        content = markdown_to_html_content('\n'.join(lines)).strip()

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Hung Ly</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="index.html" class="logo">Hung Ly</a>
      <ul class="nav-links">
        <li><a href="index.html">Work</a></li>
        <li><a href="reflections.html">Reflections</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="#footer">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <div class="breadcrumb">
      <a href="index.html">Work</a>
      <span>/</span>
      <span>{title}</span>
    </div>

    <div class="content-container">
      <article>
        <h1>{title}</h1>
        <p style="color: #7f8c8d; font-size: 1.05rem; margin-bottom: 2rem;">{subtitle}</p>
        <div style="background: #ecf0f1; padding: 1.5rem; border-radius: 8px; margin: 2rem 0;">
          {content}
        </div>
        <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #ecf0f1; display: flex; gap: 1rem; flex-wrap: wrap;">
          <a href="index.html" class="btn">← Back to All Work</a>
          <a href="reflections.html" class="btn btn-secondary">Reflections</a>
        </div>
      </article>
    </div>
  </main>

  <footer id="footer">
    <div class="footer-content">
      <div class="social-links">
        <a href="https://github.com/hungly2301" target="_blank">GitHub</a>
        <a href="mailto:your-email@example.com">Email</a>
        <a href="https://twitter.com" target="_blank">Twitter</a>
      </div>
      <p class="footer-text">
        © 2026 Hung Ly. All work created as part of DH101: Digital Humanities course.
      </p>
    </div>
  </footer>
</body>
</html>'''

    output_path = os.path.join(DOCS_DIR, output_filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created {output_path}')


def create_reflections_page():
    files = sorted([f for f in os.listdir(REFLECTIONS_DIR) if f.endswith('.md')])
    entries = []
    for file_name in files:
        key = file_name.replace('.md', '')
        md_content = read_markdown(key, 'reflections')
        if not md_content:
            continue
        lines = md_content.splitlines()
        title = key
        body_lines = []
        began = False
        for line in lines:
            if line.startswith('# '):
                title = line.replace('# ', '').strip()
                began = True
                continue
            if not began:
                continue
            body_lines.append(line)
        content_html = markdown_to_html_content('\n'.join(body_lines)).strip()
        excerpt = ' '.join(re.sub(r'\s+', ' ', ' '.join(body_lines[:6])).split())
        if len(excerpt) > 180:
            excerpt = excerpt[:177].rstrip() + '...'
        entries.append({'id': key, 'title': title, 'content': content_html, 'excerpt': excerpt})

    entry_blocks = []
    for entry in entries:
        entry_blocks.append(f'''
        <article class="card reflection-card">
          <div class="card-header">
            <div class="card-title">{entry['title']}</div>
            <div class="card-date">Reflection</div>
          </div>
          <div class="card-body">
            <div class="card-description">{entry['excerpt']}</div>
            <div class="card-footer">
              <a href="#" class="btn" type="button">Read Entry</a>
            </div>
            <div class="reflection-content" style="display:none; margin-top:1rem;">{entry['content']}</div>
          </div>
        </article>
        ''')

    entry_blocks_str = ''.join(entry_blocks)
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reflections — AI Learning Diary | Hung Ly</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="index.html" class="logo">Hung Ly</a>
      <ul class="nav-links">
        <li><a href="index.html">Work</a></li>
        <li><a href="reflections.html">Reflections</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="#footer">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section class="about-section">
      <h1>Reflections</h1>
      <p>Diary entries from my DH101 journey: weekly reflections on AI, identity, labor, ecology, and the stories technology helps us tell.</p>
      <p>Search the diary, open entries to read more, and trace how my thinking about AI changed over the course.</p>
    </section>

    <section class="search-section">
      <input type="text" id="search-box" class="search-box" placeholder="Search reflections by keyword, week, or theme..." />
      <div class="search-info">Filter the diary entries as you read through the journey.</div>
    </section>

    <div id="no-results" class="no-results" style="display:none;">No reflections match your search. Try another keyword.</div>
    <div id="reflection-grid" class="grid">
''' + entry_blocks_str + '''
    </div>
  </main>

  <footer id="footer">
    <div class="footer-content">
      <div class="social-links">
        <a href="https://github.com/hungly2301" target="_blank">GitHub</a>
        <a href="mailto:your-email@example.com">Email</a>
        <a href="https://twitter.com" target="_blank">Twitter</a>
      </div>
      <p class="footer-text">© 2026 Hung Ly. Reflections on AI, learning, and digital humanities.</p>
    </div>
  </footer>

  <script>
    const searchBox = document.getElementById('search-box');
    const cards = Array.from(document.querySelectorAll('.reflection-card'));
    const noResults = document.getElementById('no-results');

    function updateVisibility(query) {
      let visible = 0;
      cards.forEach(card => {
        const title = card.querySelector('.card-title').textContent.toLowerCase();
        const content = card.querySelector('.reflection-content').textContent.toLowerCase();
        const match = title.includes(query) || content.includes(query);
        card.style.display = match ? 'flex' : 'none';
        if (match) visible += 1;
      });
      noResults.style.display = visible === 0 ? 'block' : 'none';
    }

    searchBox.addEventListener('input', event => {
      updateVisibility(event.target.value.toLowerCase().trim());
    });

    cards.forEach(card => {
      const button = card.querySelector('.btn');
      const content = card.querySelector('.reflection-content');
      button.addEventListener('click', event => {
        event.preventDefault();
        const isHidden = content.style.display === 'none';
        content.style.display = isHidden ? 'block' : 'none';
        button.textContent = isHidden ? 'Hide Entry' : 'Read Entry';
      });
    });
  </script>
</body>
</html>'''

    output_path = os.path.join(DOCS_DIR, 'reflections.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created {output_path}')


for week_id, meta in weeks.items():
    create_html_page(week_id, meta['title'], meta['subtitle'], folder='makes')

create_reflections_page()
print('All HTML pages created!')
