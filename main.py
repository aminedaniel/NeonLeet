import customtkinter as ctk
import io
from contextlib import redirect_stdout

class NeonLeet(ctk.CTk):
    def __init__(self):
        super().__init__()

        current_row = 0
        current_column = 0

        # Opens a blank window titled NeonLeet
        # in a 600x600 pixel size

        # Make the columns expand horizontally
        self.grid_columnconfigure(0, weight=1)

        self.mission_label = ctk.CTkLabel(
            self,
            text="Mission: Two Sum",
            font=("Courier", 24, "bold"),
            text_color="#00FF00"
        )

        self.mission_label.grid(row=current_row, column=current_column, pady=10, padx=10, sticky="nsew")
        current_row += 1

        self.title("NeonLeet")
        self.geometry("600x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.hacking_terminal = ctk.CTkTextbox(self, width=600, height=150)
        self.run_button = ctk.CTkButton(self, text="Execute Payload",
                                        command=self.execute_payload)

        self.hacking_terminal.grid(row=current_row, column=current_column, pady=10, padx=10, sticky="nsew")
        self.grid_rowconfigure(current_row, weight=1)  # Row for terminal
        current_row += 1

        self.run_button.grid(row=current_row, column=current_column, pady=10, padx=10)
        current_row += 1

        self.system_output = ctk.CTkTextbox(self, width=600, height=150)
        self.system_output.grid(row=current_row, column=0, pady=10, padx=10, sticky= "nsew")
        self.grid_rowconfigure(current_row, weight=1)  # Row for terminal
        current_row += 1

    def execute_payload(self):
        self.system_output.delete("1.0", "end")
        grab_code = self.hacking_terminal.get("1.0", "end")
        f = io.StringIO()
        try:
            with redirect_stdout(f):
                exec(grab_code)
            result = f.getvalue()
        except Exception as e:
            result = f"Input Error: {e}"

        self.system_output.insert("1.0", result)


if __name__ == "__main__":
    app = NeonLeet()
    app.mainloop()