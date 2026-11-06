"""Build the A2 PDF from Markdown and unmodified student screenshots.
Screenshot focus views use PDF clipping; original PNGs remain unchanged.
"""
from pathlib import Path
from io import BytesIO
import re, html, json, math
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
TMP = ROOT / 'tmp/pdfs/a2'
OUT.mkdir(parents=True, exist_ok=True)
TMP.mkdir(parents=True, exist_ok=True)
text = (ROOT / 'A2-report.md').read_text(encoding='utf-8')
abstract = text.split('## Abstract\n', 1)[1].split('## Problem and project scope', 1)[0].strip()
main = '## Problem and project scope\n' + text.split('## Problem and project scope\n', 1)[1].split('## Figures', 1)[0]
def words(s):
    return len(re.sub(r'^#+\s*', '', s, flags=re.M).split())
ac, mc = words(abstract), words(main)
assert ac <= 300 and mc <= 1100 and ac + mc <= 1400, (ac, mc)
countline = f'Total report word count: {ac+mc:,} (abstract {ac}; main report {mc:,}, including section headings). Figures, references and repository links excluded.'
text = re.sub(r'^Total report word count:.*$', countline, text, flags=re.M)
(ROOT / 'A2-report.md').write_text(text, encoding='utf-8')
INK = colors.HexColor('#20252c')
BLUE = colors.HexColor('#294cb4')
styles = {
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10.5, leading=14.3, spaceAfter=8, textColor=INK),
    'h1': ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=14, leading=18, spaceBefore=15, spaceAfter=8, keepWithNext=True),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11, leading=15, spaceBefore=10, spaceAfter=6, keepWithNext=True),
    'small': ParagraphStyle('small', fontName='Helvetica', fontSize=8.5, leading=12, spaceAfter=5, textColor=INK),
    'ref': ParagraphStyle('ref', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=10),
}
def rich(s):
    s = html.escape(s).replace('–', '-').replace('—', '-')
    s = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', s)
    return re.sub(r'(https://[^\s]+)', lambda m: f'<link href="{m[0].rstrip(chr(46))}" color="#294cb4">{m[0]}</link>', s)
def append_md(story, s, body='body'):
    for block in s.strip().split('\n\n'):
        if block.startswith('### '): story.append(Paragraph(rich(block[4:]), styles['h2']))
        elif block.startswith('## '): story.append(Paragraph(rich(block[3:]), styles['h1']))
        else: story.append(Paragraph(rich(block.replace('\n', ' ')), styles[body]))
def footer(c, doc):
    c.setFont('Helvetica', 8); c.setFillColor(colors.HexColor('#69717a'))
    c.drawString(48, 29, 'ESA  |  Xuran Ding  |  Intelligent Interactive Systems A2')

story = [Paragraph('ESA Email Summary Assistant', ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=23, leading=29, spaceAfter=10)),
         Paragraph('Xuran Ding', styles['body']), Paragraph(countline, styles['small'])]
repo = 'https://github.com/dawsen1208/esa-email-summary-assistant'
for label, url in [('Repository',repo),('README and development record',repo+'/blob/3a4497c/README.md'),('Submitted prototype and screenshot snapshot',repo+'/commit/3a4497c')]:
    story.append(Paragraph(f'{label}: <link href="{url}" color="#294cb4">{url}</link>', styles['small']))
story.append(Spacer(1, 7)); story.append(Paragraph('Abstract', styles['h1']))
append_md(story, abstract); append_md(story, main)
SimpleDocTemplate(str(TMP/'text.pdf'), pagesize=A4, leftMargin=48,rightMargin=48,topMargin=44,bottomMargin=48).build(story,onFirstPage=footer,onLaterPages=footer)

W,H = landscape(A4)
c = canvas.Canvas(str(TMP/'figures.pdf'), pagesize=(W,H))
def heading(title, subtitle):
    c.setFillColor(INK); c.setFont('Helvetica-Bold',19); c.drawString(38,H-43,title)
    c.setFont('Helvetica',9); c.drawString(38,H-62,subtitle)
def foot(label):
    c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#69717a'));c.drawString(38,22,label)
def box(x,y,w,h,lines,sim=False,planned=False):
    c.setFillColor(colors.HexColor('#fff6dc' if sim else '#edf2fa'))
    c.setStrokeColor(colors.HexColor('#a6afbb'))
    if planned:c.setDash(4,3)
    c.roundRect(x,y,w,h,5,stroke=1,fill=1);c.setDash()
    c.setFillColor(INK)
    for i,line in enumerate(lines):
        c.setFont('Helvetica-Bold' if i==0 else 'Helvetica',10 if i==0 else 9)
        c.drawCentredString(x+w/2,y+h-19-i*15,line)
def arrow(points,label='',at=None):
    c.setStrokeColor(BLUE);c.setLineWidth(1.1)
    p=c.beginPath();p.moveTo(*points[0])
    for xy in points[1:]:p.lineTo(*xy)
    c.drawPath(p)
    a,b=points[-2:];angle=math.atan2(b[1]-a[1],b[0]-a[0])
    p=c.beginPath();p.moveTo(*b)
    for off in (-.5,.5):p.lineTo(b[0]-7*math.cos(angle+off),b[1]-7*math.sin(angle+off));p.moveTo(*b)
    c.drawPath(p)
    if label and at:
        c.setFillColor(INK);c.setFont('Helvetica',8);c.drawString(*at,label)
heading('Figure 1  System architecture','Status is shown inside each component. Arrows show information and user-control flows.')
box(46,358,205,85,['Prepared demo data','SIMULATED AI OUTPUT','Task text, deadlines, source IDs'],sim=True)
box(318,358,205,85,['Temporary state','IMPLEMENTED - JavaScript','Tasks, status, review flag'])
box(590,358,205,85,['Task cards and feedback','IMPLEMENTED - DOM rendering','Dates, progress, status labels'])
box(590,480,205,50,['Student','Inspect, correct, add, confirm'])
box(46,175,205,85,['Original email view','IMPLEMENTED - HTML passages','Fictional email; stable source IDs'])
box(318,175,205,85,['Evidence controller','IMPLEMENTED - JavaScript','Select card; focus and highlight'])
box(590,175,205,85,['Edit and review controls','IMPLEMENTED - event handlers','Save / cancel / acknowledge'])
arrow([(251,400),(318,400)],'initial data',(259,410))
arrow([(523,400),(590,400)],'render',(540,410))
arrow([(692,480),(692,443)],'user actions',(701,455))
arrow([(633,358),(633,310),(420,310),(420,260)],'Find in email',(473,319))
arrow([(318,216),(251,216)],'source ID',(263,227))
arrow([(692,358),(692,260)],'edit / add / review',(700,300))
arrow([(590,195),(553,195),(553,337),(470,337),(470,358)],'update state',(558,280))
arrow([(420,260),(420,292),(565,292),(565,375),(590,375)],'selection',(475,280))
box(46,57,749,67,['PLANNED / NOT DEVELOPED','Live model extraction and evidence selection; arbitrary email input; persistent storage.','No connection to these services exists in the submitted prototype.'],planned=True)
foot('Prepared data substitutes for model inference. Page reload/reset clears changes. No automatic omission detection.')
c.showPage()

def crop(path, area, x,y,w,h):
    """Place a focused view in the PDF without modifying the original PNG."""
    img=ImageReader(str(ROOT/'assets/storyboards'/path));iw,ih=img.getSize()
    a,b,d,e=area;cw=(d-a)*iw;ch=(e-b)*ih;s=min(w/cw,h/ch)
    dw,dh=cw*s,ch*s;xx=x+(w-dw)/2;yy=y+(h-dh)/2
    c.saveState();p=c.beginPath();p.rect(xx,yy,dw,dh);c.clipPath(p,stroke=0,fill=0)
    c.drawImage(img,xx-a*iw*s,yy-(1-e)*ih*s,width=iw*s,height=ih*s)
    c.restoreState()
def label(x,y,title,description):
    c.setFillColor(INK);c.setFont('Helvetica-Bold',11);c.drawString(x,y,title)
    c.setFont('Helvetica',9);c.drawString(x,y-15,description)
heading('Figure 2  Correcting an inaccurate deadline','User actions and visible responses - focused views of the original screenshots.')
label(38,496,'2a  Read the suggested task','The prepared summary says 6 November; the task needs checking.')
crop('01-proposal-before.png',(.51,.45,.80,.66),38,302,366,171)
label(437,496,'2b  Select Find in email','Compare the highlighted 9 November source with the suggested date.')
crop('02-proposal-evidence.png',(.21,.51,.49,.59),437,399,366,75)
crop('02-proposal-evidence.png',(.51,.32,.80,.53),437,302,366,94)
label(38,271,'2c  Edit the deadline','Enter 9 November 2026 at 12:00, then select Save task.')
crop('03-proposal-edit.png',(.374,.314,.617,.69),38,57,366,193)
label(437,271,'2d  Inspect the saved result','Edited by you; the date changes and progress increases.')
crop('04-proposal-saved.png',(.51,.32,.80,.53),437,57,366,193)
foot('Source checked; deadline corrected by the student. AI extraction and source mapping are simulated.')
c.showPage()
heading('Figure 3  Confirming an accurate task','The student compares the consent-form task with its source before confirming it.')
label(38,493,'3a  Compare with the source','11 November 2026 at 17:00 appears in both places.')
crop('05-consent-evidence.png',(.21,.575,.49,.655),38,371,366,97)
crop('05-consent-evidence.png',(.51,.53,.80,.72),38,134,366,218)
label(437,493,'3b  Select Confirm correct','The status becomes Confirmed by you; progress is 2 of 2.')
crop('06-consent-confirmed.png',(.51,.245,.80,.31),437,393,366,75)
crop('06-consent-confirmed.png',(.51,.53,.80,.72),437,134,366,218)
foot('Confirmation records the student judgement. Full-email review remains a separate acknowledgement.')
c.showPage()
heading('Figure 4  Adding a requirement found through manual review','The student finds the omission. ESA provides a form and records review acknowledgement.')
label(38,496,'4a  Review the original email','Read requirements beyond the two suggested tasks.')
crop('07-manual-review.png',(.205,.50,.50,.55),38,427,366,47)
crop('07-manual-review.png',(.195,.715,.50,.91),38,302,366,119)
label(437,496,'4b  Select Add new task','Enter the checklist and the proposal deadline.')
crop('08-add-checklist.png',(.38,.316,.626,.685),437,302,366,172)
label(38,271,'4c  Save the added task and edit it','The checklist appears with Edited by you and its deadline.')
crop('09-checklist-added.png',(.51,.532,.80,.715),38,62,366,185)
label(437,271,'4d  Finish full-email review','Review recorded; guidance closes; Edited by you is retained.')
crop('10-review-finished.png',(.51,.054,.80,.093),437,211,366,37)
crop('10-review-finished.png',(.51,.534,.80,.715),437,95,366,108)
crop('10-review-finished.png',(.394,.943,.608,.985),437,54,366,35)
foot('Completion records the student acknowledgement; it does not detect omissions or guarantee completeness.')
c.save()

refs=text.split('## References\n',1)[1]
story=[Paragraph('References',styles['h1'])]
for block in refs.strip().split('\n\n'):
    if block.startswith('- '):
        for line in block.splitlines():story.append(Paragraph(rich(line[2:]),styles['ref']))
    else:story.append(Paragraph(rich(block),styles['ref']))
SimpleDocTemplate(str(TMP/'references.pdf'),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=44,bottomMargin=48).build(story,onFirstPage=footer,onLaterPages=footer)
writer=PdfWriter()
for name in ['text.pdf','figures.pdf','references.pdf']:writer.append(TMP/name)
for i,page in enumerate(writer.pages):
    buffer=BytesIO(); stamp=canvas.Canvas(buffer,pagesize=(float(page.mediabox.width),float(page.mediabox.height)))
    stamp.setFont('Helvetica',8);stamp.setFillColor(colors.HexColor('#69717a'))
    stamp.drawRightString(float(page.mediabox.width)-38,22,f'{i+1} / {len(writer.pages)}')
    stamp.save();buffer.seek(0);page.merge_page(PdfReader(buffer).pages[0])
writer.add_metadata({'/Title':'ESA Email Summary Assistant','/Author':'Xuran Ding','/Subject':'Intelligent Interactive Systems Assignment 2'})
writer.write(OUT/'ESA_A2_Report.pdf')
report={'abstract_words':ac,'main_words':mc,'total_words':ac+mc,'pages':len(writer.pages),'screenshot_count':10}
(TMP/'build-summary.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))
