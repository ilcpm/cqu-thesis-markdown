pandoc.exe `
    .\template.md `
    -o .\template.docx `
    --filter docx_filters `
    --citeproc `
    --reference-doc .\reference.docx
    # --filter ..\section_break.py `
    # --toc `

start .\template.docx
