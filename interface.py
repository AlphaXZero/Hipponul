"""GUI module"""

from tkinter import font
import ttkbootstrap as ttk
import formulas as fm

PADX=20

def graphical_user_interface_old():
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

            oui2=fm.base_x_to_base_y("".join(oui),2,16)

        except ValueError:
            pass
        if entre2.get() and entree3.get():
            non = fm.format_nibble(
                fm.base_x_to_base_y(entre1.get(), int(entre2.get()), int(entree3.get()))
            )
            

        txt4["text"] = f"{non}"
        txt6["text"] = f"{fm.format_nibble(oui)} => {fm.format_nibble(oui2)}"

    def b():
        oui = fm.half_float_to_dec((fm.str_to_list(entre3.get()))) if len(entre3.get())==16 else fm.half_float_to_dec((entre3.get()))
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

def graphical_user_interface():
    """Build the GUI"""

    root = ttk.Window(themename="darkly")
    root.title("Hippocrate")
    title_font = font.Font(family="Helvetica", size=12, weight="bold")
    def dec_half_float_converter():
        """convert entry in half float representation"""
        oui = list(map(str, fm.half_float(float(entry_dhf.get()))))
        oui2=fm.base_x_to_base_y("".join(oui),2,16)
        result_dhf["text"] = f"{fm.format_nibble(oui)} => {fm.format_nibble(oui2)}"


    def half_float_dec_converter():
        """"""
        oui = fm.half_float_to_dec((fm.str_to_list(entre3.get()))) if len(entre3.get())==16 else fm.half_float_to_dec((entre3.get()))
        txt8["text"] = f"{oui}"

    def base_converter():
        """convert 3 entry in """
        non = fm.format_nibble(
        fm.base_x_to_base_y(entry1_bc.get(), int(entry2_bc.get()), int(entry3_bc.get()))
            )
        result_bc["text"] = f"{non}"

    title_bc = ttk.Label(text="Conversion décimal -> x", font = title_font)
    label_entry_bc = ttk.Label(text="Nombre décimal à convertir :")
    entry1_bc = ttk.Entry(root)
    label_entry2_bc =ttk.Label(text="Base de départ :")
    entry2_bc = ttk.Entry(root)
    label_entry3_bc = ttk.Label(text="Base d'arrivée :")
    entry3_bc = ttk.Entry(root)
    result_label_bc = ttk.Label(text="Résultat :")
    result_bc = ttk.Label(text="")
    button_bc = ttk.Button(text="Valider", command=base_converter, width=57)

    title_bc.grid(row = 0, column = 0, padx=PADX, pady=(30,5),sticky="W")
    label_entry_bc.grid(row = 1, column= 0, padx=PADX, sticky="W")
    entry1_bc.grid(row = 1, column = 1, pady=2, padx=PADX)
    label_entry2_bc.grid(row=2, column =0, padx=PADX, sticky="W")
    entry2_bc.grid(row=2, column=1, pady=2)
    label_entry3_bc.grid(row=3, column=0, padx=PADX, sticky="W")
    entry3_bc.grid(row=3, column=1, pady=2)
    result_label_bc.grid(row=4, column=0, padx=PADX, sticky="W",pady=(5,0))
    result_bc.grid(row=4,column=1, sticky="W",padx=PADX)
    button_bc.grid(row=5,column=0,columnspan=2, pady=(10,5), padx=PADX)


    title_dhf = ttk.Label(text="Conversion décimal -> half float",font=title_font)
    label_entry_dhf = ttk.Label(text="Nombre décimal à convertir")
    entry_dhf = ttk.Entry(root)
    result_label_dhf = ttk.Label(text="Résultat")
    result_dhf = ttk.Label(text="")
    button_dhf = ttk.Button(text="Valider", command=dec_half_float_converter, width=57)

    title_dhf.grid(row=6,column=0,pady=(15,5),padx=PADX, sticky="W")
    label_entry_dhf.grid(row=7,column=0,pady=2,padx=PADX, sticky="W")
    entry_dhf.grid(row=7,column=1)
    result_label_dhf.grid(row=8,column=0,pady=2,padx=PADX, sticky="W")
    result_dhf.grid(row=8,column=1, sticky="W")
    button_dhf.grid(row=9,column=0,columnspan=2,pady=2)
    



    


    txt5 = ttk.Label(text="décimal de base en half float :")
    txt6 = ttk.Label(text="")
    root.mainloop()
    
