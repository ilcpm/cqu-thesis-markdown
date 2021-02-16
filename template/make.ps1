$target = "template"
$in = $target + ".md"
$out = $target + ".docx"

pandoc.exe `
    $in `
    -o $out `
    --filter docx_filters `
    --citeproc `
    --reference-doc .\reference.docx
    # --filter ..\section_break.py `
    # --toc `

start $out
