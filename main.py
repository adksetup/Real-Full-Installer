from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry
from termcolor import cprint
import subprocess

class RealFullInstaller:
    def __init__(self, window: CTk) -> None:
        self.window = window
        self.window.geometry('280x300')
        self.status: str = ''
        self.window.resizable(True, True)
        self.window.wm_title('RealFullInstaller 0.2')
        self.app_name = CTkLabel(self.window, text='RealFullInstaller',
                                 font=('Helvetica bold', 26))
        self.app_name.place(relx=0.5, rely=0.2, anchor='center')
        self.install_btn = CTkButton(self.window, text='Install',
                                     command=self.install, corner_radius=20)
        self.install_btn.place(relx=0.5, rely=0.4, anchor='center')
        self.search_btn = CTkButton(self.window, text='Search',
                                command=self.search, corner_radius=20)
        self.search_btn.place(relx=0.5, rely=0.6, anchor='center')
        self.unins_btn = CTkButton(self.window, text='Uninstall',
                                   command=self.uninstall, corner_radius=20)
        self.unins_btn.place(relx=0.5, rely=0.8, anchor='center')
    def install(self):
        try:
            self.status = 'Install'
            for widget in self.window.winfo_children():
                widget.destroy()
            o_label1 = CTkLabel(self.window, text='Enter app name',
                                font=('Helvetica bold', 26))
            o_label1.place(relx=0.5, rely=0.4, anchor='center')
            self.o_entry1 = CTkEntry(self.window, width=200, corner_radius=5,
                                placeholder_text='App name')
            self.o_entry1.place(relx=0.5, rely=0.6, anchor='center')
            o_btn1 = CTkButton(self.window, text='Install',
                               command=self.install_r, corner_radius=5)
            o_btn1.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e:
            cprint(text=f'ERROR: {e}', color='red')
    def search(self):
        try:
            self.status = 'Search'
            for widget in self.window.winfo_children():
                widget.destroy()
            o_label2 = CTkLabel(self.window, text='Enter app name',
                                font=('Helvetica bold', 26))
            o_label2.place(relx=0.5, rely=0.4, anchor='center')
            self.o_entry2 = CTkEntry(self.window, width=200, corner_radius=5,
                                     placeholder_text='App name')
            self.o_entry2.place(relx=0.5, rely=0.6, anchor='center')
            o_btn2 = CTkButton(self.window, text='Search',
                               command=self.search_r, corner_radius=5)
            o_btn2.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e:
            cprint(text=f'ERROR: {e}', color='red')
    def uninstall(self):
        try:
            self.status = 'Uninstall'
            for widget in self.window.winfo_children():
                widget.destroy()
            o_label3 = CTkLabel(self.window, text='Enter app name',
                                font=('Helvetica bold', 26))
            o_label3.place(relx=0.5, rely=0.4, anchor='center')
            self.o_entry3 = CTkEntry(self.window, width=200, corner_radius=5,
                                     placeholder_text='App name')
            self.o_entry3.place(relx=0.5, rely=0.6, anchor='center')
            o_btn3 = CTkButton(self.window, text='Uninstall',
                               command=self.uninstall_r, corner_radius=5)
            o_btn3.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e:
            cprint(text=f'ERROR: {e}', color='red')
    def install_r(self):
        self.status = 'Install R'
        print('What operating system are you using?')
        print('1 macOS (Brew)')
        print('2 Linux (Apt)')
        print('3 Windows (Chocolatey)')
        print('4 Windows (Winget)')
        usr_inp1 = input(' (Number) ')
        if usr_inp1 == '1':
            print('Operating System (Package Manager): macOS (Brew)')
            subprocess.run('brew install {0}'.format(self.o_entry1.get()), shell=True)
        elif usr_inp1 == '2':
            print('Operating System (Package Manager): Linux (Apt)')
            subprocess.run('apt install {0}'.format(self.o_entry1.get()), shell=True)
        elif usr_inp1 == '3':
            print('Operating System (Package Manager): Windows (Chocolatey)')
            subprocess.run('choco install {0}'.format(self.o_entry1.get()), shell=True)
        elif usr_inp1 == '4':
            print('Operating System (Package Manager): Windows (Winget)')
            subprocess.run('winget install {0}'.format(self.o_entry1.get()), shell=True)
        else:
            cprint(text='ERROR: Option Not Found', color='red')
    def search_r(self):
        self.status = 'Search R'
        print('Operating System (Package Manager): macOS (Brew)')
        subprocess.run('brew search {0}'.format(self.o_entry2.get(), shell=True))
    def uninstall_r(self):
        self.status = 'Uninstall R'
        print('What operating system are you using?')
        print('1 macOS (Brew)')
        print('2 Linux (Apt)')
        print('3 Windows (Chocolatey)')
        print('4 Windows (Winget)')
        usr_inp1 = input(' (Number) ')
        if  usr_inp1 == '1':
            print('Operating System (Package Manager): macOS (Brew)')
            subprocess.run('brew uninstall {0}'.format(self.o_entry3.get()), shell=True)
        elif usr_inp1 == '2':
            print('Operating System (Package Manager): Linux (Apt)')
            subprocess.run('apt remove {0}'.format(self.o_entry3.get()), shell=True)
        elif usr_inp1 == '3':
            print('Operating System (Package Manager): Windows (Chocolatey)')
            subprocess.run('choco uninstall {0}'.format(self.o_entry3.get()), shell=True)
        elif usr_inp1 == '4':
            print('Operating System (Package Manager): Windows (Winget)')
            subprocess.run('winget uninstall {0}'.format(self.o_entry3.get()), shell=True)
        else:
            cprint(text='ERROR: Option Not Found', color='red')

if __name__ == '__main__':
    app = CTk()
    gui = RealFullInstaller(app)
    app.mainloop()
