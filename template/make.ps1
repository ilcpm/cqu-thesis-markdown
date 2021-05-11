# 转换脚本
$target = "template" # 转换的文件文件名
$in = $target + ".md"
$out = $target + ".docx"
$isOpenDocxAfterComplete = 1 # 转换完成是否需要自动打开

# 可以在下面按照顺序添加多个文件，会按照顺序合并在一起，实现多文档组织结构
# 这里默认是由“head.md”和上面的$target文件合并得到的
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
