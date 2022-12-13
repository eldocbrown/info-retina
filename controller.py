__author__ = 'Juan Cruz Donato'

from fpdf import FPDF

paciente = ''
while len(paciente) < 1:
    paciente = input('Paciente: ')
    if len(paciente) < 1:
        print('Error: El nombre del paciente no puede ser vacío.')

retina1 = ''
while len(retina1) < 1:
    retina1 = input('Imagen Retina 1: ')
    if len(retina1) < 1:
        print('Error: El nombre del archivo de la imagen no puede ser vacío.')

retina2 = ''
while len(retina2) < 1:
    retina2 = input('Imagen Retina 2: ')
    if len(retina2) < 1:
        print('Error: El nombre del archivo de la imagen no puede ser vacío.')

informe = ''
while len(informe) < 1:
    informe = input('Nombre del informe: ')
    if len(informe) < 1:
        print('Error: El nombre del informe no puede ser vacío.')

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Paciente: ' + paciente)
pdf.image(retina1, 40, 30, 100)
pdf.image(retina2, 40, 130, 100)
pdf.output(informe + '.pdf', 'F')