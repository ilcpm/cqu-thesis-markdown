pandoc.exe `
    .\template.md `
    -o .\template.docx `
    --citeproc `
    --filter ..\header_convert.py `
    --filter ..\equations_no.py `
    --filter ..\texcommands.py `
    --reference-doc .\reference.docx
    # --filter ..\section_break.py `
    # --toc `

start .\template.docx
