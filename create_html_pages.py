#!/usr/bin/env python3
import os
import re

# Define the project weeks
weeks = {
    'week01': {
        'title': 'Week 1: Reverse Engineering',
        'subtitle': 'Learning to think about embedded systems and decisions'
    },
    'week03': {
        'title': 'Week 3: Selfie & Identity',
        'subtitle': 'Digital self-representation in networked spaces'
    },
    'week04': {
        'title': 'Week 4: Comic & Storytelling',
        'subtitle': 'Narrative structures and visual meaning-making'
    },
    'week06': {
        'title': 'Week 6: Text & Distant Reading',
        'subtitle': 'Computational analysis and textual patterns'
    },
    'week07': {
        'title': 'Week 7: Mapping AI Worlds',
        'subtitle': 'Critical infrastructure mapping and power analysis'
    },
    'week08': {
        'title': 'Week 8: Networks of Knowledge & Power',
        'subtitle': 'Understanding systems, structures, and control'
    },
    'week09': {
        'title': 'Week 9: Bots & Generators',
        'subtitle': 'Creative systems and algorithmic curation'
    },
    'week10': {
        'title': 'Week 10: Games & Play',
        'subtitle': 'Interactive narrative and procedural rhetoric'
    },
    'week11': {
        'title': 'Week 11: AI & Labor',
        'subtitle': 'Automation, work, and human costs'
    },
    'week12': {
        'title': 'Week 12: AI & Ecology',
        'subtitle': 'Environmental dimensions of computation'
    },
    'week13': {
        'title': 'Week 13: Futures of AI & Humanity',
        'subtitle': 'Speculating on possible futures'
    },
    'text-analysis': {
        'title': 'Text Analysis: How Machines Read',
        'subtitle': 'Comparing computational and AI approaches to textual meaning'
    }
}

def markdown_to_html_content(md_content):
    """Convert basic markdown formatting to HTML"""
    # Convert headers
    md_content = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', md_content, flags=re.MULTILINE)
    
    # Convert bold
    md_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', md_content)
    md_content = re.sub(r'__(.*?)__', r'<strong>\1</strong>', md_content)
    
    # Convert italic
    md_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', md_content)
    md_content = re.sub(r'_(.*?)_', r'<em>\1</em>', md_content)
    
    # Convert links
    md_content = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', md_content)
    
    # Convert images
    md_content = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1" />', md_content)
    
    # Convert blockquotes
    md_content = re.sub(r'> (.*?)$', r'<blockquote>\1</blockquote>', md_content, flags=re.MULTILINE)
    
    # Convert code blocks
    md_content = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', md_content, flags=re.DOTALL)
    
    # Convert inline code
    md_content = re.sub(r'`(.*?)`', r'<code>\1</code>', md_content)
    
    # Wrap paragraphs
    lines = md_content.split('\n')
    result = []
    in_block = False
    current_block = []
    
    for line in lines:
        line = line.strip()
        if line.startswith('<h') or line.startswith('<pre') or line.startswith('<blockquote'):
            if current_block:
                result.append('<p>' + ' '.join(current_block) + '</p>')
                current_block = []
            result.append(line)
            in_block = True
        elif line.startswith('-') or line.startswith('•'):
            if current_block:
                result.append('<p>' + ' '.join(current_block) + '</p>')
                current_block = []
            # Handle lists
            if not in_block or not result[-1].startswith('<ul'):
                result.append('<ul>')
            result.append('<li>' + line[1:].strip() + '</li>')
        elif line == '':
            if current_block:
                result.append('<p>' + ' '.join(current_block) + '</p>')
                current_block = []
            in_block = False
        else:
            if not line.startswith('<'):
                current_block.append(line)
            else:
                if current_block:
                    result.append('<p>' + ' '.join(current_block) + '</p>')
                    current_block = []
                result.append(line)
    
    if current_block:
        result.append('<p>' + ' '.join(current_block) + '</p>')
    
    return '\n    '.join(result)

def read_markdown(filename):
    """Read markdown file"""
    path = f'/Users/hungly/Documents/GitHub/DH101/DH101/makes/{filename}.md'
    if os.path.exists(path):
        with open(path, 'r') as f:
            return f.read()
    return ''

def create_html_page(week_id, title, subtitle):
    """Create HTML page for a week"""
    md_content = read_markdown(week_id)
    # For now, just parse the first part to avoid complexity
    content_lines = md_content.split('\n')[1:]  # Skip first header
    content = '\n'.join(content_lines)
    
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
        
        <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #ecf0f1;">
          <a href="index.html" class="btn" style="display: inline-block;">← Back to All Work</a>
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
    
    # Write to file
    output_path = f'/Users/hungly/Documents/GitHub/DH101/DH101/docs/{week_id}.html'
    with open(output_path, 'w') as f:
        f.write(html)
    print(f'Created {output_path}')

# Create all pages
for week_id, meta in weeks.items():
    create_html_page(week_id, meta['title'], meta['subtitle'])

print('All HTML pages created!')
