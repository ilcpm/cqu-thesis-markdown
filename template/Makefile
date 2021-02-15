all: doc

doc: template.docx

template.docx: template.md
	pandoc $^ -o $@ -F docx_filters --citeproc --reference-doc reference.docx

clean:
	rm template.docx
