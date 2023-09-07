# Confidential-PDF-Generator
This PDF tool removes selectable text from PDF files

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This project was actually a personal request from a family friend wanting to make his PDF contracts harder to maliciously edit by making text unselectable. After searching the internet I was surprised no such tool existed so I decided to personally make it for him!

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The program works by first converting each individual page into a PNG file, re-sorts them to maintain their original order, and finally converts back to PDF removing all selectable text and meta-data in the process.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Viewing sample results:  
  
Note: GitHub allows for preview of PDF files  

For original input click on 'sample_input.pdf'  

For program's output click on 'result.pdf'  

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instructions:  
  
1. Download Python
2. Run the following command:
   pip install -r requirements.txt
3. Place your PDF file in the folder 'Input_Images'
4. Click play in VS Code or your IDE of choice
5. A file called result.pdf will be generated!

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


