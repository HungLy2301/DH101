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

NAV_HTML = '''
  <header>
    <nav>
      <a href="index.html" class="logo">Hung Ly</a>
      <ul class="nav-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About Me</a></li>
        <li><a href="my-ai-journey.html">My AI Journey</a></li>
        <li><a href="sustainability-accessibility.html">Sustainability + Accessibility</a></li>
        <li><a href="design-ai-usage.html">Design & AI Usage</a></li>
        <li><a href="ethics.html">Ethics</a></li>
      </ul>
    </nav>
  </header>
'''

PAGE_FOOTER = '''
  </main>

  <footer id="footer">
    <div class="footer-content">
      <div class="social-links">
        <a href="https://github.com/hungly2301" target="_blank">GitHub</a>
        <a href="mailto:ly_h1@denison.edu">Email</a>
        <a href="https://www.linkedin.com/in/hung-ly-seniorconsultant/" target="_blank">LinkedIn</a>
      </div>
      <p class="footer-text">
        © 2026 Hung Ly · DH 101: Critical Making in the Age of AI · Denison University
      </p>
    </div>
  </footer>
</body>
</html>'''


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


def render_page(title, body_html, page_class=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Hung Ly</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body class="{page_class}">
{NAV_HTML}
  <main>
{body_html}
{PAGE_FOOTER}
'''


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

    body_html = f'''
    <section class="breadcrumb">
      <a href="my-ai-journey.html">My AI Journey</a>
      <span>/</span>
      <span>{title}</span>
    </section>

    <section class="content-section">
      <div class="content-container">
        <article>
          <h1>{title}</h1>
          <p class="page-subtitle">{subtitle}</p>
          <div class="page-body">
            {content}
          </div>
          <div class="page-actions">
            <a href="my-ai-journey.html" class="btn">← Back to My AI Journey</a>
            <a href="final-reflection.html" class="btn btn-secondary">Final Reflection</a>
          </div>
        </article>
      </div>
    </section>
    '''

    html = render_page(title, body_html, page_class='project-page')
    output_path = os.path.join(DOCS_DIR, output_filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created {output_path}')


def extract_reflection_excerpt(md_content):
    lines = md_content.splitlines()
    excerpt_lines = []
    started = False
    for line in lines:
        if line.startswith('# '):
            started = True
            continue
        if not started or line.strip() == '' or line.startswith('>'):
            continue
        excerpt_lines.append(line.strip())
        if len(' '.join(excerpt_lines).split()) >= 40:
            break
    return markdown_to_html_content(' '.join(excerpt_lines)).strip()


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
        excerpt = extract_reflection_excerpt(md_content)
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
              <a href="#" class="btn" type="button">Hide Entry</a>
            </div>
            <div class="reflection-content" style="display:block; margin-top:1rem;">{entry['content']}</div>
          </div>
        </article>
        ''')

    entry_blocks_str = ''.join(entry_blocks)
    body_html = '''
    <section class="about-section">
      <h1>Reflections</h1>
      <p>Diary entries from my DH101 journey: weekly reflections on AI, identity, labor, ecology, and the stories technology helps us tell.</p>
      <p>Search the diary, open entries to read more, and trace how my thinking about AI changed over the course.</p>
    </section>

    <section class="search-section">
      <input type="text" id="search-box" class="search-box" placeholder="Search reflections by keyword, week, or theme..." aria-label="Search reflections" />
      <div class="search-info">Filter the diary entries as you read through the journey.</div>
    </section>

    <div id="no-results" class="no-results" style="display:none;">No reflections match your search. Try another keyword.</div>
    <div id="reflection-grid" class="grid">
{entry_blocks_str}
    </div>

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
    '''
    body_html = body_html.replace('{entry_blocks_str}', entry_blocks_str)

    html = render_page('Reflections — AI Learning Diary', body_html, page_class='reflections-page')
    output_path = os.path.join(DOCS_DIR, 'reflections.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created {output_path}')


def get_journey_projects():
    return [
        {'id': 'week01', 'title': 'Hidden Systems: Reverse Engineering AI Interfaces', 'label': 'Make 1', 'description': 'A systems-based investigation into how AI image tools hide data, labor, and design decisions.', 'link': 'week01.html'},
        {'id': 'week02', 'title': 'Portraits of AI Identity', 'label': 'Make 2', 'description': 'AI-generated portrait imagery used to explore how identity is constructed through appearance and symbolic cues.', 'link': 'week02.html'},
        {'id': 'week03', 'title': 'Selfie & Networked Identity', 'label': 'Make 3', 'description': 'A critical look at digital self-portraits and what they say about representation and agency online.', 'link': 'week03.html'},
        {'id': 'week04', 'title': 'Comics & Storytelling in AI', 'label': 'Make 4', 'description': 'A comic-based project that experiments with narrative, authorship, and the meaning-making power of visual stories.', 'link': 'week04.html'},
        {'id': 'week05', 'title': 'How Machines Read: Voyant vs GPT', 'label': 'Make 5', 'description': 'A comparison of quantitative and interpretive machine reading applied to Sojourner Truth’s speech.', 'link': 'week05.html'},
        {'id': 'week06', 'title': 'Distant Reading and Text Patterns', 'label': 'Make 6', 'description': 'An exploration of distant reading techniques and how they reveal hidden patterns in text.', 'link': 'week06.html'},
        {'id': 'week07', 'title': 'Mapping AI Worlds', 'label': 'Make 7', 'description': 'A critical map of AI infrastructure, labor, and the global politics that shape these systems.', 'link': 'week07.html'},
        {'id': 'week08', 'title': 'Networks of Knowledge & Power', 'label': 'Make 8', 'description': 'A network diagram showing how data, platforms, and corporate power connect in digital systems.', 'link': 'week08.html'},
        {'id': 'week09', 'title': 'Bots & Generators', 'label': 'Make 9', 'description': 'An investigation of generative systems and the creative role of the human behind the bot.', 'link': 'week09.html'},
        {'id': 'week10', 'title': 'Games & Play', 'label': 'Make 10', 'description': 'A project exploring the role of play, rules, and AI logic in interactive storytelling.', 'link': 'week10.html'},
        {'id': 'week11', 'title': 'AI & Labor', 'label': 'Make 11', 'description': 'An inquiry into the hidden work that powers AI systems and the human labor behind moderation and training.', 'link': 'week11.html'},
        {'id': 'week12', 'title': 'AI & Ecology', 'label': 'Make 12', 'description': 'A sustainability-focused project about the environmental cost of AI infrastructure.', 'link': 'week12.html'},
        {'id': 'week13', 'title': 'Futures of AI & Humanity', 'label': 'Make 13', 'description': 'A speculative project that uses future scenarios to reveal the assumptions behind our current technology choices.', 'link': 'week13.html'},
    ]


def create_journey_page():
    projects = get_journey_projects()
    project_blocks = []
    reflection_blocks = []

    for project in projects:
        project_blocks.append(f'''
        <article class="card journey-card">
          <div class="card-header">
            <div class="card-title">{project['title']}</div>
            <div class="card-date">{project['label']}</div>
          </div>
          <div class="card-body">
            <p class="card-description">{project['description']}</p>
            <div class="card-footer">
              <a href="{project['link']}" class="btn">View Project</a>
            </div>
          </div>
        </article>
        ''')

        reflection_md = read_markdown(project['id'], 'reflections')
        if reflection_md:
            reflection_excerpt = extract_reflection_excerpt(reflection_md)
        else:
            reflection_excerpt = '<p>Reflection coming soon.</p>'

        reflection_blocks.append(f'''
        <div class="timeline-item">
          <h3>{project['label']}: {project['title']}</h3>
          <div class="timeline-content">
            <p>{reflection_excerpt}</p>
            <a href="reflections.html" class="btn btn-secondary">Read More Reflections</a>
          </div>
        </div>
        ''')

    body_html = f'''
    <section class="hero-section">
      <div class="hero-copy">
        <h1>My AI Journey</h1>
        <p>This page traces the semester as a journey of projects, reflections, and evolving arguments about technology, power, and making. Each card below links to a project page, and the timeline shows how my reflections grew alongside the work.</p>
      </div>
    </section>

    <section class="category-section">
      <h2>Semester Projects</h2>
      <div class="grid">{''.join(project_blocks)}</div>
    </section>

    <section class="timeline-section">
      <h2>Reflection Timeline</h2>
      <div class="timeline-list">{''.join(reflection_blocks)}</div>
    </section>

    <section class="final-reflection-section">
      <h2>Final Takeaway</h2>
      <p>The work in this portfolio moved from seeing AI as a tool to recognizing it as a system of power. Every project asked: who benefits, who is made visible, and who is left out? The final reflection page carries that question forward with a clear argument about how futures are shaped by what we already accept today.</p>
      <a href="final-reflection.html" class="btn">Read the Final Reflection</a>
    </section>
    '''

    html = render_page('My AI Journey', body_html, page_class='journey-page')
    output_path = os.path.join(DOCS_DIR, 'my-ai-journey.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created {output_path}')


def create_sustainability_accessibility_page():
    body_html = '''
    <section class="hero-section">
      <h1>Sustainability & Accessibility</h1>
      <p>This page explains the concrete steps taken to make the portfolio both environmentally mindful and accessible to a wide audience.</p>
    </section>

    <section class="content-section">
      <h2>Environmental Design Choices</h2>
      <ul>
        <li>Limited external embeds and no automatic tracking scripts to keep page weight low.</li>
        <li>Used SVGs and compressed images stored locally under <code>docs/assets/images</code>.</li>
        <li>Built with simple HTML and CSS to reduce unnecessary resource use and speed up load times.</li>
        <li>Kept the design responsive so the site works well on mobile, tablet, and desktop.</li>
      </ul>
    </section>

    <section class="content-section">
      <h2>Accessibility Improvements</h2>
      <ul>
        <li>Semantic structure with headings, sections, buttons, and clear navigation.</li>
        <li>All images include descriptive <code>alt</code> text where available.</li>
        <li>Large buttons, high-contrast text, and spacious layouts for readability.</li>
        <li>Keyboard-friendly navigation and accessible form controls like search boxes.</li>
      </ul>
    </section>

    <section class="content-section">
      <h2>Why It Matters</h2>
      <p>Making a site that is easier to read, faster to load, and more respectful of user privacy is part of the same ethical work as questioning AI systems. Accessibility and sustainability are not add-ons. They are part of responsible design.</p>
    </section>
    '''

    html = render_page('Sustainability & Accessibility', body_html, page_class='sustainability-page')
    output_path = os.path.join(DOCS_DIR, 'sustainability-accessibility.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created {output_path}')


def create_design_ai_usage_page():
    body_html = '''
    <section class="hero-section">
      <h1>Design & AI Usage</h1>
      <p>This page describes the design approach, the AI tools used, and how human judgment guided the final work.</p>
    </section>

    <section class="content-section">
      <h2>Design Approach</h2>
      <p>The visual style uses strong headings, clear cards, and a calm palette to let ideas appear without distraction. The layout was created for both browsing and deep reading, with project cards that invite curiosity and reflection sections that provide context.</p>
    </section>

    <section class="content-section">
      <h2>AI Tools Used</h2>
      <ul>
        <li>ChatGPT for drafting and editing reflection text, refining arguments, and creating metadata for the portfolio.</li>
        <li>Image generation tools for AI portrait work and concept illustration summaries.</li>
        <li>Python scripting to convert Markdown into HTML and keep project pages consistent.</li>
      </ul>
    </section>

    <section class="content-section">
      <h2>Human Contribution</h2>
      <p>All final writing, project framing, and ethical decisions were made personally. Every page was reviewed and rewritten to ensure the voice is my own, and every AI contribution is disclosed in the make pages.</p>
    </section>
    '''

    html = render_page('Design & AI Usage', body_html, page_class='design-page')
    output_path = os.path.join(DOCS_DIR, 'design-ai-usage.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created {output_path}')


def create_ethics_page():
    body_html = '''
    <section class="hero-section">
      <h1>Ethics</h1>
      <p>This page reflects on bias, labor, transparency, and the ethical questions that guided the semester.</p>
    </section>

    <section class="content-section">
      <h2>Ethical Commitments</h2>
      <ul>
        <li>Disclosed AI contributions openly across the site.</li>
        <li>Focused on human labor and environmental cost rather than celebrating only capability.</li>
        <li>Built the site with accessibility and sustainability in mind.</li>
      </ul>
    </section>

    <section class="content-section">
      <h2>Readings That Shaped the Work</h2>
      <p>The portfolio draws on ethics and AI scholarship, including Bender et al. on dataset provenance, D'Ignazio & Klein on data feminism and power, and Crawford on the labor and environmental costs of machine intelligence.</p>
    </section>

    <section class="content-section">
      <h2>What This Means</h2>
      <p>Ethics in AI is not just about whether a model generates useful output. It is about who builds the model, whose labor it relies on, whose water it consumes, and what values are encoded in the decisions we call "neutral." This portfolio aims to make those questions visible.</p>
    </section>
    '''

    html = render_page('Ethics', body_html, page_class='ethics-page')
    output_path = os.path.join(DOCS_DIR, 'ethics.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created {output_path}')


def create_final_reflection_page():
    reflection_md = read_markdown('week13', 'reflections')
    if reflection_md:
        lines = reflection_md.splitlines()
        if lines and lines[0].startswith('# '):
            lines = lines[1:]
        reflection_html = markdown_to_html_content('\n'.join(lines)).strip()
    else:
        reflection_html = '<p>The final reflection will appear here once it is added.</p>'

    body_html = f'''
    <section class="hero-section">
      <h1>Final Reflection</h1>
      <p>My final argument about what it means to be human in the age of AI.</p>
    </section>

    <section class="content-section">
      <h2>In-Between Futures</h2>
      <p>AI futures feel most honest when they are neither pure utopia nor pure dystopia. The future I imagine is one where headline numbers look good while the costs are buried in terms of service clauses and hidden labor.</p>
    </section>

    <section class="content-section">
      <h2>What This Reveals About Us</h2>
      <p>These visions reveal what we are already willing to accept. They show whether we care more about convenience than accountability, more about cool interactions than the people and resources behind them.</p>
    </section>

    <section class="content-section">
      <h2>Reading the Evidence</h2>
      <p>Scholars like Bender et al. taught me to ask where datasets come from. D'Ignazio & Klein showed me that power is coded into every data collection choice. Crawford reminded me that AI is built on labor and environmental cost, not just clever math.</p>
    </section>

    <section class="content-section">{reflection_html}</section>
    '''

    html = render_page('Final Reflection', body_html, page_class='final-reflection-page')
    output_path = os.path.join(DOCS_DIR, 'final-reflection.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created {output_path}')


for week_id, meta in weeks.items():
    create_html_page(week_id, meta['title'], meta['subtitle'], folder='makes')

create_reflections_page()
create_journey_page()
create_sustainability_accessibility_page()
create_design_ai_usage_page()
create_ethics_page()
create_final_reflection_page()
print('All HTML pages created!')
