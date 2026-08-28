import tkinter as tk
from tkinter import ttk


def create_labeled_combobox(parent, label, values, row, column, default=None):
    ttk.Label(parent, text=label).grid(row=row, column=column, padx=5, pady=5, sticky="w")
    combo = ttk.Combobox(parent, values=values, state="readonly")
    if default is not None:
        combo.set(default)
    combo.grid(row=row, column=column + 1, padx=5, pady=5, sticky="ew")
    return combo


def create_scrollable_tree(parent):
    frame = ttk.Frame(parent)
    frame.pack(fill="both", expand=True)

    tree = ttk.Treeview(frame, show="headings")
    yscroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    xscroll = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

    tree.grid(row=0, column=0, sticky="nsew")
    yscroll.grid(row=0, column=1, sticky="ns")
    xscroll.grid(row=1, column=0, sticky="ew")
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    return tree
