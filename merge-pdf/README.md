# 📄 PDF Merger Tool

This project is a simple Python utility to merge multiple PDF files into a single file using the `PyPDF2` library. The script is designed for ease of use and can handle various PDF files seamlessly.

---

## 🛠 Features
- Merge multiple PDF files into a single file.
- Handle exceptions gracefully, ensuring smooth execution.
- Easy customization of input file paths and output file names.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.6 or higher**
- **PyPDF2**: Install it using pip:
  ```bash
  pip install PyPDF2

Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/nofilsiddiqui-2000/Practice-Projects.git
    cd "Practice-Projects/merge-pdf"
2. Open the script in your favorite text editor or IDE.
  
3. Modify the pdf_files variable with the paths of the PDF files you want to merge:
     ```bash
   pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
     
4. Set the desired name for the output merged PDF file in the output variable:
      ```bash
      output = "merged-files.pdf"

      
5. Run the script:
      ```bash
   python merge_pdfs.py

6. If successful, the merged PDF will be saved with the specified name in the current directory.

🔧 How It Works
- Import PyPDF2: Utilize the PdfMerger class to handle merging.
- Iterate Through PDFs: Append each PDF from the provided list.
- Output File: Write the merged content to a specified file.

✨ Future Improvements
- Add a GUI for non-technical users.
- Implement support for merging password-protected PDFs.
- Include drag-and-drop functionality for easier file selection.

⚠️ Note
- Ensure all input PDF file paths are correct and accessible.
- If an input file is missing, the script will print an error message



