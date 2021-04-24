$target = "template"
$in = $target + ".md"
$out = $target + ".docx"

pandoc.exe `
    head.md `
    $in `
    -o $out `
    --filter pandoc_word_helper `
    --citeproc `
    --metadata link-citations=true `
    --reference-doc .\reference.docx

start $out
