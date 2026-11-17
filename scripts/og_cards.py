"""Generate 1200x630 link-preview cards into images/og/ (title left, figure right).

Run from anywhere: python3 scripts/og_cards.py  (needs ImageMagick 7 and macOS Georgia/Arial fonts).
A new project page gets a card automatically; then point its og:image and twitter:image at /images/og/<slug>.jpg.
"""
import os, re, html, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'images/og')
TMP = tempfile.mkdtemp(prefix='og_cards_')
os.makedirs(OUT, exist_ok=True); os.makedirs(TMP, exist_ok=True)
SERIF = '/System/Library/Fonts/Supplemental/Georgia Bold.ttf'
SANS_B = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
SANS = '/System/Library/Fonts/Supplemental/Arial.ttf'
BG, ACCENT, TEXT, MUTED, BORDER = '#f7f5f0', '#0b4bc1', '#1c1c1c', '#6b665f', '#e3dfd7'

OVERRIDES = {
    'bert-ct-reports': dict(title='BERT analysis of French CT reports to measure the pulmonary embolism positivity rate',
                            eyebrow='Research in Diagnostic and Interventional Imaging · 2023'),
    'ecapri': dict(eyebrow='European Radiology · 2026 · Open access'),
    'phd-thesis': dict(eyebrow='PhD thesis · Université Claude Bernard Lyon 1 · 2024', figure='/images/projects/phd-thesis/unsupervised-maps.webp'),
    'video-inpainting': dict(eyebrow="Master's course project · Sorbonne Université · 2020"),
    'cyclegan': dict(eyebrow="Master's project · Institut Pasteur"),
    'pulmonary-embolism': dict(eyebrow='Diagnostic and Interventional Imaging · 2024'),
}


def im(*args):
    subprocess.run(['magick', *args], check=True)


def title_size(t):
    n = len(t)
    return 54 if n <= 40 else 48 if n <= 60 else 42 if n <= 85 else 36


def card(slug, eyebrow, title, figure=None, figure_png=None):
    fig = figure_png or os.path.join(TMP, slug + '-fig.png')
    if figure:
        # figure on a white rounded panel, fitted inside 500x480
        im(os.path.join(ROOT, figure.lstrip('/')), '-resize', '500x480', '-background', 'white', '-gravity', 'center',
           '-extent', '520x500', fig)
    panel = os.path.join(TMP, slug + '-panel.png')
    im('-size', '536x516', 'xc:none', '-fill', 'white', '-stroke', BORDER, '-strokewidth', '2',
       '-draw', 'roundrectangle 1,1 534,514 18,18', panel)
    ttl = os.path.join(TMP, slug + '-title.png')
    im('-background', 'none', '-fill', TEXT, '-font', SERIF, '-pointsize', str(title_size(title)),
       '-interline-spacing', '4', '-size', '520x', 'caption:' + title, ttl)
    eye = os.path.join(TMP, slug + '-eye.png')
    im('-background', 'none', '-fill', ACCENT, '-font', SANS_B, '-pointsize', '21', '-size', '520x', 'caption:' + eyebrow.upper(), eye)
    out = os.path.join(OUT, slug + '.jpg')
    im('-size', '1200x630', 'xc:' + BG,
       '-fill', ACCENT, '-draw', 'rectangle 0,0 1200,8',
       eye, '-geometry', '+64+76', '-composite',
       ttl, '-geometry', '+64+150', '-composite',
       '-fill', TEXT, '-font', SANS_B, '-pointsize', '24', '-annotate', '+64+548', 'Aissam Djahnine',
       '-fill', MUTED, '-font', SANS, '-pointsize', '21', '-annotate', '+64+580', 'aissamdjahnine.github.io',
       panel, '-geometry', '+628+57', '-composite',
       fig, '-geometry', '+636+65', '-composite',
       '-quality', '86', out)
    print('card', out, os.path.getsize(out) // 1024, 'KB')


def page_meta(slug):
    s = open(os.path.join(ROOT, 'projects', slug + '.html')).read()
    v = html.unescape(re.search(r'class="venue">(.*?)<', s).group(1))
    h = html.unescape(re.sub('<[^>]+>', '', re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1))).strip()
    t = re.search(r'<figure class="teaser">.*?<img src="([^"]+)"', s, re.S).group(1)
    o = OVERRIDES.get(slug, {})
    return o.get('eyebrow', v), o.get('title', h), o.get('figure', t)


slugs = [f[:-5] for f in sorted(os.listdir(os.path.join(ROOT, 'projects'))) if f.endswith('.html')]
for slug in slugs:
    e, t, f = page_meta(slug)
    card(slug, e, t, figure=f)

# Home: round photo in the panel
photo = os.path.join(TMP, 'home-fig.png')
im(os.path.join(ROOT, 'images/Photo_identite_3-modified.png'), '-resize', '340x340^', '-gravity', 'center', '-extent', '340x340',
   '(', '-size', '340x340', 'xc:none', '-fill', 'white', '-draw', 'circle 170,170 170,0', ')', '-compose', 'DstIn', '-composite',
   '-background', 'white', '-compose', 'over', '-gravity', 'center', '-extent', '520x500', photo)
card('home', 'Medical imaging · Computer vision', 'AI Research Engineer @ DentalMonitoring, PhD in Computer Science', figure_png=photo)

# All projects: 2x2 collage of featured thumbnails
thumbs = ['images/github-projects/nas-darts-cells.webp', 'images/projects/video-inpainting/architecture.webp',
          'images/projects/handwritten-recognition/thumb.webp', 'images/github-projects/gan-project.webp']
col = os.path.join(TMP, 'all-projects-fig.png')
im('montage', *[os.path.join(ROOT, p) for p in thumbs], '-tile', '2x2', '-geometry', '248x236+6+6', '-background', 'white', col)
im(col, '-resize', '520x500', '-background', 'white', '-gravity', 'center', '-extent', '520x500', col)
card('all-projects', 'Portfolio', 'All projects: research write-ups, course work and side projects', figure_png=col)
