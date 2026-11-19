"""Generate 1200x630 link-preview cards into images/og/, figure-first.

The figure fills most of the card and a short title sits in a band below it, so the card
still reads when LinkedIn shrinks it to a small thumbnail.

Run from anywhere: python3 scripts/og_cards.py  (needs ImageMagick 7 and macOS Georgia/Arial fonts).
For a new project page, add its slug to CARDS below (short title + figure), run the script,
then point the page's og:image and twitter:image at /images/og/<slug>.jpg.
"""
import os, subprocess, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'images/og')
TMP = tempfile.mkdtemp(prefix='og_cards_')
os.makedirs(OUT, exist_ok=True)
SERIF = '/System/Library/Fonts/Supplemental/Georgia Bold.ttf'
SANS_B = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
SANS = '/System/Library/Fonts/Supplemental/Arial.ttf'
BG, ACCENT, TEXT, MUTED, BORDER = '#f7f5f0', '#0b4bc1', '#1c1c1c', '#6b665f', '#e3dfd7'
W, H = 1200, 630

# slug: (short title, figure). Keep titles short: they must read at thumbnail size.
CARDS = {
    'phd-thesis': ('PhD thesis: pathology detection in CT', 'images/projects/phd-thesis/unsupervised-maps.webp'),
    'pulmonary-embolism': ('Pulmonary embolism detection in CT', 'images/JFR_recap.webp'),
    'weakly-supervised-ct': ('Weakly supervised 3D CT pathology detection', 'images/projects/weakly-supervised-ct/method-overview.webp'),
    'ct-3dflow': ('CT-3DFlow: unsupervised 3D CT', 'images/projects/ct-3dflow/framework.webp'),
    'contrastive-pretraining': ('Contrastive pretraining for 3D CT', 'images/ieee-contrastive.webp'),
    'bert-ct-reports': ('BERT on French CT reports', 'images/BERT_recap.webp'),
    'ecapri': ('eCAPRI: post-TAVI mortality prediction', 'images/CAPRI_recap.webp'),
    'muscle-segmentation': ('Skeletal muscle segmentation in CT', 'images/SARCO_PROJECT.webp'),
    'dat-spect': ('DaT SPECT classification', 'images/dat-parkinson-challenge.webp'),
    'nas-darts': ('Neural architecture search for mammography', 'images/projects/nas-darts/learned-cells.webp'),
    'cyclegan': ('CycleGAN cell segmentation', 'images/projects/cyclegan/results-metrics.webp'),
    'video-inpainting': ('Unsupervised video inpainting', 'images/projects/video-inpainting/architecture.webp'),
    'handwritten-recognition': ('Handwritten text recognition', 'images/projects/handwritten-recognition/line-detection.webp'),
}


def im(*args):
    subprocess.run(['magick', *args], check=True)


def tmp(name):
    return os.path.join(TMP, name)


def band(base, title, size=46):
    """Title band under the figure: short serif title, then name and site."""
    return [base,
            '-fill', TEXT, '-font', SERIF, '-pointsize', str(size), '-annotate', '+48+548', title,
            '-fill', ACCENT, '-font', SANS_B, '-pointsize', '22', '-annotate', '+48+592', 'Aissam Djahnine',
            '-fill', MUTED, '-font', SANS, '-pointsize', '22', '-annotate', '+238+592', '·  aissamdjahnine.github.io']


def title_size(t):
    n = len(t)
    return 48 if n <= 32 else 44 if n <= 38 else 40 if n <= 44 else 36


def figure_card(slug, title, figure):
    # white panel across the top, figure fitted inside it
    fig = tmp(slug + '-fig.png')
    im(os.path.join(ROOT, figure), '-resize', '1092x412', '-background', 'white', '-gravity', 'center', '-extent', '1104x424', fig)
    base = tmp(slug + '-base.png')
    im('-size', '%dx%d' % (W, H), 'xc:' + BG,
       '-fill', ACCENT, '-draw', 'rectangle 0,0 1200,8',
       '-fill', 'white', '-stroke', BORDER, '-strokewidth', '2', '-draw', 'roundrectangle 40,32 1160,472 18,18',
       '-stroke', 'none', fig, '-geometry', '+48+40', '-composite', base)
    out = os.path.join(OUT, slug + '.jpg')
    im(*band(base, title, title_size(title)), '-quality', '86', out)
    print('card', slug, os.path.getsize(out) // 1024, 'KB')


def home_card():
    # large round photo left, name and role right: both readable as a thumbnail
    photo = tmp('home-photo.png')
    im(os.path.join(ROOT, 'images/Photo_identite_3-modified.png'), '-resize', '440x440^', '-gravity', 'center', '-extent', '440x440',
       '(', '-size', '440x440', 'xc:none', '-fill', 'white', '-draw', 'circle 220,220 220,0', ')', '-compose', 'DstIn', '-composite', photo)
    out = os.path.join(OUT, 'home.jpg')
    im('-size', '%dx%d' % (W, H), 'xc:' + BG,
       '-fill', ACCENT, '-draw', 'rectangle 0,0 1200,8',
       photo, '-geometry', '+64+95', '-composite',
       '-fill', TEXT, '-font', SERIF, '-pointsize', '68', '-annotate', '+560+250', 'Aissam Djahnine',
       '-fill', TEXT, '-font', SANS_B, '-pointsize', '34', '-annotate', '+562+320', 'AI Research Engineer',
       '-fill', MUTED, '-font', SANS, '-pointsize', '30', '-annotate', '+562+366', 'PhD in Computer Science',
       '-fill', MUTED, '-font', SANS, '-pointsize', '30', '-annotate', '+562+408', 'Medical imaging · Computer vision',
       '-fill', ACCENT, '-font', SANS_B, '-pointsize', '24', '-annotate', '+562+490', 'aissamdjahnine.github.io',
       '-quality', '86', out)
    print('card home', os.path.getsize(out) // 1024, 'KB')


def all_projects_card():
    thumbs = ['images/github-projects/nas-darts-cells.webp', 'images/projects/video-inpainting/architecture.webp',
              'images/projects/handwritten-recognition/thumb.webp', 'images/github-projects/gan-project.webp']
    col = tmp('all-projects-collage.png')
    im('montage', *[os.path.join(ROOT, p) for p in thumbs], '-tile', '4x1', '-geometry', '262x400+6+6', '-background', 'white', col)
    figure_card('all-projects', 'All projects', col)


for slug, (title, fig) in CARDS.items():
    figure_card(slug, title, fig)
home_card()
all_projects_card()
