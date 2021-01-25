$target = "template"
$in = $target + ".md"
$out = $target + ".docx"

pandoc.exe `
    $in `
    -o $out `
    --filter ..\header_convert.py `
    --filter ..\equations_no.py `
    --filter ..\figures_no.py `
    --filter ..\refs.py `
    --filter ..\texcommands.py `
    --citeproc `
    --reference-doc .\reference.docx
    # --filter ..\section_break.py `
    # --toc `

start $out
