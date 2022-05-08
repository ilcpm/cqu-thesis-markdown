all: doc

doc: paper.docx

paper.docx: head.md cover_bachelor.md paper.md
	pandoc -F pandoc_cqu_thesis --resource-path ./figures/:. --citeproc --reference-doc reference.docx --metadata link-citations=true $^ -o $@

clean:
	-rm paper.docx
