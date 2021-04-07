all: doc

doc: template.docx

template.docx: head.md template.md
	pandoc -F docx_filters --citeproc --reference-doc reference.docx --metadata link-citations=true $^ -o $@

clean:
	-rm template.docx
