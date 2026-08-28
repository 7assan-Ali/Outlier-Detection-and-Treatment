import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pandas as pd

from Src.iqr_detection import detect_iqr_outliers
from Src.outlier_treatment import cap_iqr, keep, trim_iqr, winsorize_iqr
from Src.zscore_detection import detect_zscore_outliers


class OutlierApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Outlier Detection & Treatment")
        self.geometry("1100x700")
        self.minsize(900, 600)
        self.df = None
        self.result_df = None
        self.numeric_columns = []
        self._build_ui()

    def _build_ui(self):
        top = ttk.Frame(self, padding=12)
        top.pack(fill="x")
        ttk.Label(top, text="Outlier Detection & Treatment", font=("Segoe UI", 18, "bold")).pack(side="left")
        ttk.Button(top, text="Load CSV", command=self.load_csv).pack(side="right")

        controls = ttk.LabelFrame(self, text="Analysis", padding=10)
        controls.pack(fill="x", padx=12, pady=6)

        ttk.Label(controls, text="Detection Method").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.method = ttk.Combobox(controls, values=["IQR", "Z-Score"], state="readonly")
        self.method.set("IQR")
        self.method.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(controls, text="Treatment").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.treatment = ttk.Combobox(
            controls,
            values=["Keep", "Trimming", "Capping", "Winsorization"],
            state="readonly",
        )
        self.treatment.set("Keep")
        self.treatment.grid(row=0, column=3, padx=5, pady=5)

        ttk.Button(controls, text="Run Analysis", command=self.run_analysis).grid(row=0, column=4, padx=15)
        ttk.Button(controls, text="Export Result", command=self.export_result).grid(row=0, column=5, padx=5)

        self.status = ttk.Label(self, text="Load a CSV file to begin.", padding=(12, 5))
        self.status.pack(fill="x")

        frame = ttk.Frame(self, padding=12)
        frame.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(frame, show="headings")
        yscroll = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        xscroll = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")
        xscroll.grid(row=1, column=0, sticky="ew")
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

    def load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not path:
            return
        try:
            self.df = pd.read_csv(path)
            self.result_df = self.df.copy()
            self.numeric_columns = self.df.select_dtypes(include="number").columns.tolist()
            self.status.config(text=f"Loaded: {len(self.df):,} rows × {len(self.df.columns)} columns")
            self._show_table(self.df.head(100))
        except Exception as exc:
            messagebox.showerror("Load Error", str(exc))

    def run_analysis(self):
        if self.df is None:
            messagebox.showwarning("No Data", "Please load a CSV file first.")
            return
        if not self.numeric_columns:
            messagebox.showwarning("No Numeric Features", "The dataset has no numeric columns.")
            return

        try:
            if self.method.get() == "IQR":
                detection = detect_iqr_outliers(self.df, self.numeric_columns)
            else:
                detection = detect_zscore_outliers(self.df, self.numeric_columns)

            treatment = self.treatment.get()
            if treatment == "Keep":
                self.result_df = keep(self.df)
            elif treatment == "Trimming":
                self.result_df = trim_iqr(self.df, self.numeric_columns)
            elif treatment == "Capping":
                self.result_df = cap_iqr(self.df, self.numeric_columns)
            else:
                self.result_df = winsorize_iqr(self.df, self.numeric_columns)

            self.status.config(
                text=f"{self.method.get()} detected {int(detection['Outlier Count'].sum()):,} outliers | "
                     f"Result: {len(self.result_df):,} rows"
            )
            self._show_table(detection)
        except Exception as exc:
            messagebox.showerror("Analysis Error", str(exc))

    def _show_table(self, data: pd.DataFrame):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(data.columns)
        for column in data.columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=130, anchor="center")
        for row in data.itertuples(index=False, name=None):
            self.tree.insert("", "end", values=[str(value) for value in row])

    def export_result(self):
        if self.result_df is None:
            messagebox.showwarning("No Result", "Run an analysis first.")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialfile="treated_dataset.csv",
        )
        if path:
            self.result_df.to_csv(path, index=False)
            messagebox.showinfo("Export Complete", "The result was saved successfully.")


def main():
    app = OutlierApp()
    app.mainloop()


if __name__ == "__main__":
    main()
