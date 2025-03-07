from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(paragraph, styles['BodyText'])
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.gray),
                   ('FONTNAME', (0,0), (-1,0), 'Arial-Bold'),
                   ('ALIGN', (0,0), (-1,-1), 'CENTER')]
    empty_line = Spacer(1,20)

    report.build([report_title, empty_line, report_info])
