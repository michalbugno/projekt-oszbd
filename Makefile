all: oszbd0809f.pdf

oszbd0809f.pdf: oszbd0809f.tex images/data_flow_diagram.pdf images/erd_diagram.pdf images/logo_agh.pdf
	texi2pdf $<

clean:
	rm -rf *.aux *.log *.out *.toc
