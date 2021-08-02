

def py_to_tex(fname):
    file = open(fname, "w")

    file.write("\documentclass{report}\n")
   # file.write("\usepackage[a4paper, width=150mm, top=25mm, bottom=25mm, bindingoffset=6mm] {geometry}")
    file.write("")
    file.write("\section{Analiza zadatka}\n")
  #  file.write("Osnovna ideja ovog projekta jeste izgradnja pametnog grada (eng. Robot Cities). Zadaci koje robot treba da obezbedi su sledeći:")
    file.write("")
    file.write("\begin{figure}[h]\n")
    file.write("\centering\n")
    file.write("\includegraphics[width=110mm]{img/teren.PNG}\n")
    file.write("\caption{Izgled terena.}\n")
    file.write("\label{fig:teren}\n")
    file.write("\end{figure}\n")

    file.close()


py_to_tex("output.tex")