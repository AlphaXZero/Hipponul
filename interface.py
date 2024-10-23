"""GUI module"""

import ttkbootstrap as ttk
import formulas as fm


def graphical_user_interface():
    """Build the GUI"""
    root = ttk.Window(themename="darkly")
    root.title("Hippocrate")
    root.geometry("900x500")
    #TODO: séparer half float et conversion
    def a():
        non = ""
        oui2 = ""
        try:
            oui = list(map(str, fm.half_float(float(entre1.get()))))
            print(oui)
            oui2=fm.base_x_to_base_y("".join(oui),2,16)
            print(oui2)
        except ValueError:
            pass
        if entre2.get() and entree3.get():
            non = fm.format_nibble(
                fm.base_x_to_base_y(entre1.get(), int(entre2.get()), int(entree3.get()))
            )
            

        txt4["text"] = f"{non}"
        txt6["text"] = f"{fm.format_nibble(oui)} => {fm.format_nibble(oui2)}"

    def b():
        oui = fm.half_float_to_dec((fm.str_to_list(entre3.get())))
        txt8["text"] = f"{oui}"
        return 0

    titre1 = ttk.Label(text="Conversion décimal -> x")
    txt = ttk.Label(text="Nombre decimal à convertir :")
    txt2 = ttk.Label(text="Base de départ :")
    txt3 = ttk.Label(text="résultat :")
    txt4 = ttk.Label(text="")
    txt5 = ttk.Label(text="décimal de base en half float :")
    txt6 = ttk.Label(text="")
    txtt1 = ttk.Label(text="Base d'arrivée :")

    entre1 = ttk.Entry()

    entre2 = ttk.Entry()
    entree3 = ttk.Entry()
    bou1 = ttk.Button(text="Valider", command=a)

    titre1.grid(row=0, column=2)
    txt.grid(row=1, column=0)
    txt2.grid(row=2, column=0)
    txt3.grid(row=2, column=4)
    txt4.grid(row=2, column=5)
    txt5.grid(row=1, column=4)
    txt6.grid(row=1, column=5)
    entre1.grid(row=1, column=2)
    entre2.grid(row=2, column=2)
    entree3.grid(row=3, column=2)
    bou1.grid(row=2, column=3)
    txtt1.grid(row=3, column=0)

    bou2 = ttk.Button(text="Valider", command=b)
    titre2 = ttk.Label(text="Conversion Half-Float -> nombre")
    txt7 = ttk.Label(text="reponse :")
    entre3 = ttk.Entry()
    txt8 = ttk.Label(text="")
    titre2.grid(row=4, column=2)
    txt7.grid(row=5, column=2)
    txt8.grid(row=5, column=3)
    entre3.grid(row=5, column=0)
    bou2.grid(row=5, column=1)

    root.mainloop()
