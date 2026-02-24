import customtkinter as ctk
import io
from contextlib import redirect_stdout

class NeonLeet(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Opens a blank window titled NeonLeet
        # in a 600x600 pixel size

        self.title("NeonLeet")
        self.geometry("600x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.hacking_terminal = ctk.CTkTextbox(self, width=600, height=150)
        self.run_button = ctk.CTkButton(self, text="Execute Payload",
                                        command=self.execute_payload)
        self.hacking_terminal.pack()
        self.run_button.pack()

        self.system_output = ctk.CTkTextbox(self, width=600, height=150)
        self.system_output.pack()

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