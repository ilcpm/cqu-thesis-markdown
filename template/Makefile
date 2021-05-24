all: doc

doc: template.docx

template.docx: head.md 本科封面.md template.md
	pandoc -F pandoc_word_helper --citeproc --reference-doc reference.docx --metadata link-citations=true $^ -o $@

clean:
	-rm template.docx
