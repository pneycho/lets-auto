"""
Convert a folder full of marksdowns to pdf.

You need to install pandoc. Look at documentation for Windows.
For Ubuntu, 
sudo apt-get install pandoc
sudo apt-get install texlive-latex-base
sudo apt-get install texlive-fonts-recommended
sudo apt-get install texlive-fonts-extra
sudo apt-get install texlive-laetex-extra

-f -> Input format, You might run into some trouble with the conversion of latex equations so try all of them
Options= -markdown_mmd, MultiMarkdown (best)
		 - markdown_phpextra, PHP Extra Markdown
		 - markdown_strict, original unextended Markdown
		 - markdown. Pandoc's Markdown
		 - gfm , Github-flavored Markdown 

Docs: https://pandoc.org/MANUAL.html
"""

import os 

base_dir = "/home/shreyan/Downloads/cs231n-2016-winter-master/notes/2-convolutional-neural-networks/"

os.chdir(base_dir)
for fname in os.listdir(base_dir):
	fpath = base_dir+fname
	cmd = f"pandoc -f markdown_mmd -t pdf {fname} -o {fname[:-3]}.pdf"
	print("Running command:", cmd)
	os.system(cmd)