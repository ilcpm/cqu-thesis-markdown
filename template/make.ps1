$target = "template"
$in = $target + ".md"
$out = $target + ".docx"

pandoc.exe `
    head.md `
    $in `
    -o $out `
    --filter docx_filters `
    --citeproc `
    --metadata link-citations=true `
    --reference-doc .\reference.docx
    # --filter ..\section_break.py `
    # --toc `

start $out
