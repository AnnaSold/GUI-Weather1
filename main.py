import tkinter as tk
import Project_weather as p
            
        
root:tk.Tk = tk.Tk()


photo: tk.PhotoImage = tk.PhotoImage(file='погода.png')
root.iconphoto(False, photo)
root.geometry("450x350")
window: p.Window = p.Window(root)
root.title("Приложение для прогноза погоды")
root['bg'] = '#8aa9f2'
root.mainloop()
