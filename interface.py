"""GUI module"""

from tkinter import font
import ttkbootstrap as ttk
import formulas as fm

PADX = 20


def graphical_user_interface():
    """Build the GUI"""

    root = ttk.Window(themename="darkly")
    root.title("Hippocrate")
    title_font = font.Font(family="Helvetica", size=12, weight="bold")

    def dec_half_float_converter():
        """convert entry in half float representation"""
        binary_repr_hf = [str(i) for i in fm.half_float(float(entry_dhf.get()))]
        try:
            hex_repr_hf = fm.base_x_to_base_y("".join(binary_repr_hf), 2, 16)
            result_dhf["text"] = (
                f"{fm.format_nibble(binary_repr_hf)} => {fm.format_nibble(hex_repr_hf)}"
            )
        except ValueError:
            result_dhf["text"] = f"{fm.format_nibble(binary_repr_hf)}"

    def half_float_dec_converter():
        """convert half float in decimal"""
        deci = (
            fm.half_float_to_dec((fm.str_to_list(entry_hfd.get())))
            if len(entry_hfd.get()) == 16
            else fm.half_float_to_dec((entry_hfd.get()))
        )
        deci_expo = fm.half_flaot_to_dec_2(entry_hfd.get())
        result_hfd["text"] = f"{deci} -> {deci_expo}"

    def base_converter():
        """convert number in ant base in the same number in another chosen base"""
        nbr = fm.format_nibble(
            fm.base_x_to_base_y(
                entry1_bc.get(), int(entry2_bc.get()), int(entry3_bc.get())
            )
        )
        result_bc["text"] = f"{nbr}"

    title_bc = ttk.Label(text="Conversion base x -> base y", font=title_font)
    label_entry_bc = ttk.Label(text="Nombre à convertir :")
    entry1_bc = ttk.Entry(root)
    label_entry2_bc = ttk.Label(text="Base de départ :")
    entry2_bc = ttk.Entry(root)
    label_entry3_bc = ttk.Label(text="Base d'arrivée :")
    entry3_bc = ttk.Entry(root)
    result_label_bc = ttk.Label(text="Résultat :")
    result_bc = ttk.Label(text="")
    button_bc = ttk.Button(text="Valider", command=base_converter, width=57)
    title_bc.grid(row=0, column=0, padx=PADX, pady=(30, 5), sticky="W")
    label_entry_bc.grid(row=1, column=0, padx=PADX, sticky="W")
    entry1_bc.grid(row=1, column=1, pady=2, padx=PADX)
    label_entry2_bc.grid(row=2, column=0, padx=PADX, sticky="W")
    entry2_bc.grid(row=2, column=1, pady=2)
    label_entry3_bc.grid(row=3, column=0, padx=PADX, sticky="W")
    entry3_bc.grid(row=3, column=1, pady=2)
    result_label_bc.grid(row=4, column=0, padx=PADX, sticky="W", pady=(5, 0))
    result_bc.grid(row=4, column=1, sticky="W", padx=PADX)
    button_bc.grid(row=5, column=0, columnspan=2, pady=(10, 5), padx=PADX)

    title_dhf = ttk.Label(text="Conversion décimal -> half float :", font=title_font)
    label_entry_dhf = ttk.Label(text="Nombre décimal à convertir :")
    entry_dhf = ttk.Entry(root)
    result_label_dhf = ttk.Label(text="Résultat :")
    result_dhf = ttk.Label(text="")
    button_dhf = ttk.Button(text="Valider", command=dec_half_float_converter, width=57)
    title_dhf.grid(row=6, column=0, pady=(15, 5), padx=PADX, sticky="W")
    label_entry_dhf.grid(row=7, column=0, pady=2, padx=PADX, sticky="W")
    entry_dhf.grid(row=7, column=1)
    result_label_dhf.grid(row=8, column=0, pady=2, padx=PADX, sticky="W")
    result_dhf.grid(row=8, column=1, sticky="W")
    button_dhf.grid(row=9, column=0, columnspan=2, pady=10)

    title_hfd = ttk.Label(text="Conversion half float -> décimal", font=title_font)
    label_entry_hfd = ttk.Label(text="half float à convertir :")
    entry_hfd = ttk.Entry(root)
    result_label_hfd = ttk.Label(text="Résultat :")
    result_hfd = ttk.Label(text="")
    button_hfd = ttk.Button(
        text="Valider :", command=half_float_dec_converter, width=57
    )
    title_hfd.grid(row=10, column=0, pady=(15, 5), padx=PADX, sticky="W")
    label_entry_hfd.grid(row=11, column=0, pady=2, padx=PADX, sticky="W")
    entry_hfd.grid(row=11, column=1)
    result_label_hfd.grid(row=12, column=0, pady=2, padx=PADX, sticky="W")
    result_hfd.grid(row=12, column=1, sticky="W")
    button_hfd.grid(row=13, column=0, columnspan=2, pady=(10, 40))

    root.mainloop()
