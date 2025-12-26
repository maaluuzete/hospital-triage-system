import customtkinter as ctk
from tkinter import messagebox
from triage_system import TriageSystem

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class TriageApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Triagem Hospitalar")
        self.geometry("600x500")
        self.resizable(False, False)
        self.system = TriageSystem()
        self.history = []
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(
            self,
            text="Atendendo Agora",
            font=("Arial", 24, "bold")
        ).pack(pady=10)
        self.current_patient_label = ctk.CTkLabel(
            self,
            text="-",
            font=("Arial", 20),
            text_color="red"
        )
        self.current_patient_label.pack(pady=10)
        ctk.CTkLabel(
            self,
            text="Últimos Atendidos",
            font=("Arial", 16)
        ).pack(pady=5)
        self.history_box = ctk.CTkTextbox(
            self,
            width=450,
            height=120,
            state="disabled"
        )
        self.history_box.pack(pady=5)
        form_frame = ctk.CTkFrame(self)
        form_frame.pack(pady=15)
        self.name_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="Nome do paciente",
            width=200
        )
        self.name_entry.grid(row=0, column=0, padx=5)
        self.priority_option = ctk.CTkOptionMenu(
            form_frame,
            values=["Emergência", "Urgente", "Rotina"]
        )
        self.priority_option.grid(row=0, column=1, padx=5)
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=15)
        ctk.CTkButton(
            button_frame,
            text="Adicionar Paciente",
            command=self.add_patient
        ).grid(row=0, column=0, padx=5)
        ctk.CTkButton(
            button_frame,
            text="Chamar Próximo",
            command=self.call_next_patient
        ).grid(row=0, column=1, padx=5)
        ctk.CTkButton(
            button_frame,
            text="Reset",
            fg_color="red",
            command=self.reset_system
        ).grid(row=0, column=2, padx=5)
    def add_patient(self):
        name = self.name_entry.get().strip()
        priority = self.priority_option.get()
        if not name:
            messagebox.showwarning("Erro", "Digite o nome do paciente.")
            return
        self.system.add_patient(name, priority)
        self.name_entry.delete(0, "end")
    def call_next_patient(self):
        patient = self.system.call_next_patient()
        if patient is None:
            messagebox.showinfo("Fila vazia", "Não há pacientes em espera.")
            return
        name, priority = patient
        display_text = f"{name} ({priority})"
        self.current_patient_label.configure(text=display_text)
        self.history.insert(0, display_text)
        self.history = self.history[:5]
        self.update_history()

    def update_history(self):
        self.history_box.configure(state="normal")
        self.history_box.delete("1.0", "end")
        for item in self.history:
            self.history_box.insert("end", item + "\n")
        self.history_box.configure(state="disabled")

    def reset_system(self):
        self.system.reset_system()
        self.history.clear()
        self.current_patient_label.configure(text="---")
        self.update_history()

if __name__ == "__main__":
    app = TriageApp()
    app.mainloop()
