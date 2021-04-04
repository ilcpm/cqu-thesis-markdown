all: doc

doc: template.docx

template.docx: head.md template.md
	pandoc -F docx_filters --citeproc --reference-doc reference.docx $^ -o $@

clean:
	-rm template.docx
