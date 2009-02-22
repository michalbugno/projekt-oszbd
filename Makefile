all: doc.pdf harmonogram.pdf

doc.pdf: doc.tex images/data_flow_diagram.pdf images/erd_diagram.pdf
	texi2pdf doc.tex

harmonogram.pdf: harmonogram.tex
	texi2pdf harmonogram.tex

clean:
	rm -rf *.aux *.log *.out *.toc
