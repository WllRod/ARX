# Import FPDF class
from fpdf import FPDF
from datetime import datetime
from os import getcwd

def main_relat_folha_ponto(list, path):
# Create instance of FPDF class
# Letter size paper, use inches as unit of measure
    pdf=FPDF(orientation='L',format='letter', unit='mm')
    
    
    # Add new page. Without this you cannot create the document.
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.image(getcwd()+'\\assets\\logo2.png', 10, 8, 33)
    pdf.set_font('Arial', 'B', 25)
    pdf.ln(10)
    pdf.cell(100)
    pdf.cell(30, 10, 'Folha de Ponto Detalhada', 0, 0, 'C')
    pdf.ln(20)
    pdf.set_line_width(0.0)
    #pdf.line(5.0,5.0,205.0,5.0) # top one
    #pdf.line(5.0,292.0,205.0,292.0) # bottom one
    #pdf.line(5.0,5.0,5.0,292.0) # left one
    #pdf.line(205.0,5.0,205.0,292.0) # right one
    # Remember to always put one of these at least once.
    pdf.set_font('Times','',10.0) 
    
    # Effective page width, or just epw
    epw = pdf.w - 2*pdf.l_margin
    
    # Set column width to 1/4 of effective page width to distribute content 
    # evenly across table and page
    col_width = epw/8
    
    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.
    
    data = [['Funcionário','Data','Horas Trabalhadas','Valor Dia', 'Horas Extras', 'Valor Hora Extra', 'Bonificação']]
    
    for x in list:
        temp_array  = []
        if(x[1]):
            date    = x[1]
            
        for c in x:
            if(c == date):
                c   = datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
            temp_array.append(c)
        data.append(temp_array)


    # Document title centered, 'B'old, 14 pt

    # Text height is the same as current font size
    th = pdf.font_size
    

    # Line break equivalent to 4 lines
    pdf.ln(4*th)
    
    # Here we add more padding by passing 2*th as height
    for row in data:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 2*th, str(datum)[0:15], border=1)
    
        pdf.ln(2*th)
    
    pdf.output(path,'F')