import PyPDF2

def merge_pdfs(input_files, output_file):
    merger = PyPDF2.PdfMerger()
    
    for file in input_files:
        merger.append(file)
    
    merger.write(output_file)
    merger.close()

# Example usage
input_files = ['stub1.pdf', 'stub2.pdf', 'stub3.pdf']
output_file = 'merged_april.pdf'

merge_pdfs(input_files, output_file)
