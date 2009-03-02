all: doc.pdf

doc.pdf: doc.tex images/data_flow_diagram.pdf images/erd_diagram.pdf images/logo_agh.pdf
	texi2pdf doc.tex

clean:
	rm -rf *.aux *.log *.out *.toc
