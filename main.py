import customtkinter as ctk

class MyApp(ctk.CTk):
    def __init__(self,**kwargs):
        super(MyApp,self).__init__(**kwargs)
        # Define window
        self.title('Metric Helper')
        self.resizable(0,0)

        # Define color & font 
        field_font = ('Canbria',13,'bold')
        bg_color = '#111111' # '#4dff7c'
        button_color = '#111111' # '#8dddf7'
        self.config(bg= bg_color)

        # Create input & output 
        self.input_field = ctk.CTkEntry(self,width=20,font=field_font)
        self.input_field.grid(row=0,column=0,padx=10,pady=10,ipadx=60)
        ctk.CTkLabel(self,text='=',bg_color=bg_color).grid(row=0,column=1,padx=10,pady=10)
        self.output_field = ctk.CTkEntry(self,width=20,font=field_font)
        self.output_field.grid(row=0,column=2,padx=10,pady=10,ipadx=60)

        self.input_field.insert(0,'0')

        # Create input & output combobox
        metric_list = ['femto','pico','nano', 
                       'micro','milli','centi',
                       'deci','base value','deca',
                       'hecto','kilo','mega','giga','tera', 'peta']

        self.input_combox = ctk.CTkComboBox(master=self,values=metric_list,justify='center',font=field_font)
        self.input_combox.grid(row=1,column=0,padx=10,pady=10)
        ctk.CTkLabel(self, text="to", font=field_font, bg_color=bg_color).grid(row=1,column=1,padx=10,pady=10)
        self.output_combox = ctk.CTkComboBox(master=self,values=metric_list,justify='center',font=field_font)
        self.output_combox.grid(row=1,column=2,padx=10,pady=10)

        self.input_combox.set('base value');self.output_combox.set('base value')

        ctk.CTkButton(self, text='Convert', font=field_font, bg_color=button_color,command=self.convert)\
            .grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)
        
        # Run window's main loop
        self.mainloop()

    # Define function
    def convert(self):
        metric_values = {'femto':10**-15,'pico':10**-12,'nano':10**-9,
                         'micro':10**-6,'milli':10**-3,'centi':10**-2,
                         'deci':10**-1,'base value':10**0,'deca':10**1,
                         'hecto':10**2,'kilo':10**3,'mega':10**6,
                         'giga':10**9,'tera':10**12,'peta':10**15}
        # Clear output
        self.output_field.delete(0,"end")

        start_value = float(self.input_field.get())
        start_prefix = self.input_combox.get()
        end_prefix = self.output_combox.get()

        base_value = start_value*metric_values[start_prefix]
        end_value = base_value/metric_values[end_prefix]
        
        # Insert output
        self.output_field.insert(0, str(end_value))

if __name__ == "__main__":
    MyApp()