all: doc

doc: template.docx

template.docx: head.md cover_bachelor.md template.md
	pandoc -F pandoc_cqu_thesis --resource-path ./figures/:. --citeproc --reference-doc reference.docx --metadata link-citations=true $^ -o $@

clean:
	-rm template.docx
