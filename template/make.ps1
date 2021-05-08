$target = "template"
$in = $target + ".md"
$out = $target + ".docx"
$isOpenDocxAfterComplete = 1


pandoc.exe `
    head.md `
    $in `
    -o $out `
    --filter pandoc_word_helper `
    --citeproc `
    --metadata link-citations=true `
    --reference-doc .\reference.docx

if ($isOpenDocxAfterComplete) {
    Start-Process $out
}
