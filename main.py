import json
import requests
from tkcalendar import Calendar, DateEntry
import datetime
import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import ttk, END
import tkinter.font as tkfont
from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog as fd
from ttkwidgets.autocomplete import AutocompleteEntryListbox

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


headers = {
        'API-HOST': 'YOUR-API-HOST-NAME',
        'API-KEY': 'YOUR-API-KEY',
    }

seasons = ['2023-2024','2022-2023', '2021-2022']

class Pre_load_App(customtkinter.CTk):
    COUNT = 0

    def __init__(self):
        super().__init__()

        style = ttk.Style()

        style.theme_use("default")

        style.configure("Treeview",
                        background="#343638",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#F3F1E9",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        font=(None, 17))
        style.map("Treeview.Heading",
                  background=[('active', '#3484F0')])

        self.on_closing = None
        self.var = customtkinter.StringVar(self)
        self.title("ClassApp")
        # self.iconbitmap("Files/Images/camera.ico")
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # self.window_width = screen_width
        # self.window_height = screen_height
        # self.geometry("%dx%d" % (self.window_width, self.window_height))
        self.geometry(f"1330x900")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        self.complete_data = {}
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=200,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self, width=1000)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=100, pady=15)

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.add_menu_display211 = customtkinter.CTkFrame(master=self.frame_right,
                                                          corner_radius=15,
                                                          height=400,
                                                          width=10)
        self.add_menu_display211.grid(pady=15, padx=15, sticky="nws")

        columns = ('column_1', 'column_2', 'column_3', 'column_4','column_5','column_6')

        self.table = ttk.Treeview(master=self.add_menu_display211,
                                  columns=columns,
                                  height=20,
                                  selectmode='browse',
                                  show='headings')

        self.table.column("#1", anchor="c", width=150)
        self.table.column("#2", anchor="c",  width=150)
        self.table.column("#3", anchor="c",  width=150)
        self.table.column("#4", anchor="c",  width=150)
        self.table.column("#5", anchor="c",  width=150)
        self.table.column("#6", anchor="c",  width=150)

        self.table.heading('column_1', text='Column 1')
        self.table.heading('column_2', text='Column 2')
        self.table.heading('column_3', text='Column 3')
        self.table.heading('column_4', text='Column 4')
        self.table.heading('column_5', text='Column 5')
        self.table.heading('column_6', text='Column 6')

        self.table.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.table.bind('<Motion>', 'break')

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Menu",
                                              font=("Roboto Medium", -16))
        self.label_1.grid(row=1, column=0, pady=20, padx=10)

        self.result_label_1 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638')
        self.result_label_1.place(x=110, y=300)

        self.result_label_2 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638')
        self.result_label_2.place(x=350, y=350)

        self.result_label_3 = customtkinter.CTkLabel(master=self.frame_right,
                                                     text='',
                                                     font=("Roboto Medium", -25),
                                                     bg_color='#343638')
        self.result_label_3.place(x=710, y=300)

        self.result_label_4 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638')
        self.result_label_4.place(x=400, y=300)

        self.result_label_5 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638',)
        self.result_label_5.place(x=110, y=400)

        self.result_label_6 = customtkinter.CTkLabel(master=self.frame_right,
                                                     text='',
                                                     font=("Roboto Medium", -25),
                                                     bg_color='#343638')
        self.result_label_6.place(x=400, y=400)

        self.result_label_7 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638')
        self.result_label_7.place(x=710, y=400)

        self.result_label_8 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638')
        self.result_label_8.place(x=280, y=210)


        def get_teams(date):

            left_1 = 0
            left_2 = 0
            right_1 = 0
            right_2 = 0

            params = {
                'date': date,
            }
            # print(date)
            if self.optionmenu_0.get() == 'Basketball':
                url = 'https://v1.basketball.api-sports.io/games'
            elif self.optionmenu_0.get() == 'Handball':
                url = 'https://v1.handball.api-sports.io/games'

            response = requests.get(f'{url}', params=params, headers=headers)

            if str(response.status_code) == "200":
                self.optionmenu_1.configure(state='read')

                global new_values_for_combobox
                new_values_for_combobox = []

                # global team_id_dict
                # team_id_dict = {}
                self.complete_data = {}
                count = 1
                pretty_json = json.loads(response.text)
                total_len = pretty_json['results']
                nba_g_league_count = 0
                for team_data in pretty_json['response']:
                    if team_data['league']['name'] == "NBA - G League":
                        nba_g_league_count+=1
                total_len = total_len - nba_g_league_count
                
                self.complete_data['total_games'] = total_len

                self.games_counter.configure(text=f'0 / {total_len}')
                self.update()
                for home_away in pretty_json['response']:
                    if home_away['league']['name'] != "NBA - G League":
                        home = home_away['teams']['home']['name']
                        home_id = home_away['teams']['home']['id']

                        away = home_away['teams']['away']['name']
                        away_id = home_away['teams']['away']['id']

                        league_id = home_away['league']['id']
                        league_name = home_away['league']['name']
                        country_name = home_away['country']['name']

                        match_time = home_away['time']
                        match_time = self.add_two_hours(match_time)
                        
                        # league_name = home_away['league']['name']
                        # league_season = home_away['league']['season']

                        # print(f'Home Team --> Name: {home},  id: {home_id}')
                        # print(f'Away Team --> Name: {away},  id: {away_id}')
                        # print(f'League ID: {league_id}, League Name: {league_name}, Season: {league_season}')
                        # print('\n\n')

                        # match = '{:20s} vs {:20s}    {}'.format(home,away,match_time)
                        match = f'{home} vs {away}'

                        # calc = 100-len_match
                        match_2 = f"{count:02d}.      {match_time}            {match}"
                        print(match_2)
                        if match_2 not in new_values_for_combobox:
                            new_values_for_combobox.append(match_2)
                        print('this is count: ',count)

                        if self.optionmenu_0.get() == 'Basketball':
                            final_score = ''
                            if home_away['scores']['home']['total'] != None and home_away['scores']['away']['total'] != None:
                                final_score = f"{home_away['scores']['home']['total']} : {home_away['scores']['away']['total']}"
                        elif self.optionmenu_0.get() == 'Handball':
                            final_score = ''
                            if home_away['scores']['home'] != None and home_away['scores']['away'] != None:
                                final_score = f"{home_away['scores']['home']} : {home_away['scores']['away']}"

                        self.complete_data[count] = self.get_teams_data_advance(date,home_id, away_id, league_id, final_score, league_name,country_name)
                        self.complete_data[count].append(match)
                        self.complete_data[count].append(match_2)
                        
                        # json_string = json.dumps(self.complete_data, indent = 4)

                        print('--------------------------------this complete data starts--------------------------------')
                        print(self.complete_data)
                        print('--------------------------------this complete data ends--------------------------------')

                        with open(f'{date}_{self.optionmenu_0.get()}.json', 'w') as outfile:
                            json.dump(self.complete_data, outfile)

                        # print(self.complete_data[count][0])
                        print('this is final score ',final_score)
                        if 'away_home_points_avg' in self.complete_data[count][0] and final_score != '':
                            print('new hehe')
                            total_score = final_score.split(':')
                            total_score = int(total_score[0]) + int(total_score[1])
                            above_text = float(self.complete_data[count][0]['f_result_4'])
                            lower_text = int(self.complete_data[count][0]['final_counter_text'].split('/')[0])
                            if lower_text >= 8:
                                if total_score > above_text:
                                    left_1+=1
                                else:
                                    left_2+=1
                            elif lower_text <= 2:
                                if total_score > above_text:
                                    right_1+=1
                                else:
                                    right_2+=1
                            print('left ',left_1)
                            print(left_2)
                            print(right_1)
                            print(right_2)
                        self.games_counter.configure(text=f'{count} / {total_len}')
                        # time.sleep(2)
                        self.update()

                        count+=1
                self.different_counters_left.configure(text=f'{left_1} / {left_2}')
                self.different_counters_right.configure(text=f'{right_1} / {right_2}')

                print(new_values_for_combobox)
                self.optionmenu_1.configure(values=new_values_for_combobox)
                self.optionmenu_1.set(new_values_for_combobox[0])


            else:
                tkinter.messagebox.showerror('Error', 'An error occurred, please try again!')

        def date_date_picker():
            today = datetime.date.today()

            def date_select():
                self.button_1.configure(text=f'{date_date.selection_get()}')
                top.destroy()

                get_teams(date_date.selection_get())

            top = customtkinter.CTkToplevel(self.frame_left)
            top.geometry('800x500')
            top.title("Select Date")
            top.attributes("-topmost", True)
            global date_date
            date_date = Calendar(top,
                                 font="Arial 14", selectmode='day',
                                 cursor="hand2", year=today.year, month=today.month, day=today.day)
            date_date.pack(fill="both", expand=True,padx=40)
            customtkinter.CTkButton(top, text="Select Date", font=("Helvetica", 14), command=date_select).pack(pady=20)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Select Date",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=date_date_picker,
                                                cursor='hand2')
        self.button_1.grid(row=2, column=0, pady=(15, 15), padx=20)

        # self.button_2 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Delete Item",
        #                                         corner_radius=15,
        #                                         border_width=1.5,
        #                                         border_color="#3484F0",  # alternative red: #f03933
        #                                         fg_color="#343638",
        #                                         cursor='hand2',
        #                                         command=None)
        # self.button_2.grid(row=3, column=0, pady=15, padx=20)
        #
        # self.button_3 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Edit Item",
        #                                         corner_radius=15,
        #                                         border_width=1.5,
        #                                         border_color="#3484F0",
        #                                         fg_color="#343638",
        #                                         cursor='hand2',
        #                                         command=None)
        # self.button_3.grid(row=4, column=0, pady=15, padx=20)

        self.optionmenu_0_values = ['Basketball','Handball']
        self.optionmenu_0 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=self.optionmenu_0_values,
                                                        corner_radius=15,
                                                        button_color="#565b5e",
                                                        fg_color="#343638",
                                                        button_hover_color="#3484F0",
                                                        command=None,
                                                        height=20)
        self.optionmenu_0.grid(row=3, column=0, pady=(15, 25), padx=20)
        self.optionmenu_0.set(self.optionmenu_0_values[0])

        self.home_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='',
                                                 font=("Roboto Medium", -14))
        self.home_label.grid(row=7, column=0, pady=(20, 0), padx=10)

        self.vs_label = customtkinter.CTkLabel(master=self.frame_left,
                                               text='',
                                               font=("Roboto Medium", -14))
        self.vs_label.grid(row=8, column=0, pady=(5,5), padx=10)

        self.away_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='',
                                                 font=("Roboto Medium", -14))
        self.away_label.grid(row=9, column=0, padx=10,pady=(0,20))

        self.games_counter = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='0 / 0',
                                                 font=("Roboto Medium", -18))
        self.games_counter.grid(row=10, column=0, padx=10,pady=(12,0))

        self.league_name = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='',
                                                 font=("Roboto Medium", -14))
        self.league_name.grid(row=11, column=0, padx=10,pady=(20,0))

        self.country_name = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='',
                                                 font=("Roboto Medium", -14))
        self.country_name.grid(row=12, column=0, padx=10,pady=(20,0))

        self.different_counters_left = customtkinter.CTkLabel(master=self.frame_left,text='',width=0,
                                                   font=("Roboto Medium", 1))
        self.different_counters_left.grid(row=13, column=0)

        self.different_counters_left = customtkinter.CTkLabel(master=self.frame_left,
                                                   text='0 / 0',
                                                   font=("Roboto Medium", 11),text_color='#22AA49')
        self.different_counters_left.place(x=50,y=643)

        self.different_counters_right = customtkinter.CTkLabel(master=self.frame_left,
                                                   text='0 / 0',
                                                   font=("Roboto Medium", 11),text_color='#CE2027')
        self.different_counters_right.place(x=100,y=643)

        self.get_data_btn = customtkinter.CTkButton(master=self.frame_left,
                                                text="Get Data",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=lambda : self.get_data(index=None),
                                                cursor='hand2')
        self.get_data_btn.grid(row=14, column=0, pady=(30, 0), padx=20)

        self.copy_btn = customtkinter.CTkButton(master=self.frame_left,
                                                text="Copy",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=lambda : self.copy(),
                                                cursor='hand2')
        self.copy_btn.grid(row=15, column=0, pady=(20, 20), padx=20)

        
        self.load_from_file = customtkinter.CTkButton(master=self.frame_left,
                                                text="Load Data",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=lambda : self.load_file(),
                                                cursor='hand2')
        self.load_from_file.grid(row=16, column=0, pady=(0, 20), padx=20)

        
        self.continue_btn = customtkinter.CTkButton(master=self.frame_left,
                                                text="Continue",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=lambda : self.continue_data(),
                                                cursor='hand2')
        self.continue_btn.grid(row=17, column=0, pady=(0, 20), padx=20)

        
        
        def home_away_labels(event):
            self.home_label.configure(text=self.optionmenu_1.get().split('vs')[0].strip(' ').split('            ')[1].strip(' '))
            self.vs_label.configure(text='vs')
            self.away_label.configure(text=self.optionmenu_1.get().split('vs')[1].strip(' '))

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        corner_radius=15,
                                                        button_color="#565b5e",
                                                        fg_color="#343638",
                                                        button_hover_color="#3484F0",
                                                        command=home_away_labels,
                                                        height=20,
                                                        dynamic_resizing=False,
                                                        dropdown_hover_color='#3484F0')
        self.optionmenu_1.grid(row=4, column=0, pady=(15, 15), padx=20)
        self.optionmenu_1.set("Select date first")
        self.optionmenu_1.configure(state='disabled')

        self.search_team = customtkinter.CTkButton(master=self.frame_left,
                                                text="Search",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=self.search_teams,
                                                cursor='hand2')
        self.search_team.grid(row=5, column=0, pady=(15, 15), padx=20)
        
        self.final_score = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='',
                                                 font=("Roboto Medium", -17))
        self.final_score.grid(row=6, column=0, pady=(15, 15), padx=20)
        # self.optionmenu_1.bind("<Configure>", home_away_labels)
        # self.optionmenu_1.bind("<<OptionSelected>>", home_away_labels)

        # ============ frame_right ============

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        font = tkfont.nametofont('TkTextFont')
        self.table.tag_configure('TkTextFont', font=tkfont.nametofont('TkTextFont'))
        self.table.tag_configure('average_color_change', foreground="#FF7F2A",font=tkfont.nametofont('TkTextFont'))
        style.configure('Treeview', rowheight=font.metrics('linespace'))

        _font = tkfont.nametofont('TkTextFont')
        _font.configure(size=21)
        style.configure('Treeview', rowheight=_font.metrics('linespace'))

        def selection_remove(selection):
            self.table.selection_remove(self.table.focus())
            print("Deselected item")

        def change_values_option_menu_down(event):
            if self.optionmenu_1.get() == 'Select date first':
                tkinter.messagebox.showinfo("Error", "Please select date first")
                return
            try:
                # self.optionmenu_1.set(self.temp_data_optionmenu[1])
                # print(new_values_for_combobox)
                index = int(self.optionmenu_1.get().split('.')[0]) - 1
                index += 1
                index = index % len(new_values_for_combobox)
                self.optionmenu_1.set(new_values_for_combobox[index])
                home_away_labels(event=None)

                updated_index = int(self.optionmenu_1.get().split('.')[0])
                self.get_data(index=updated_index)
            except:
                # self.optionmenu_1.set(self.temp_data_optionmenu[1])
                # print(new_values_for_combobox)
                index = int(self.optionmenu_1.get().split('.')[0]) - 1
                index += 1
                index = index % len(combobox_values_updated)
                self.optionmenu_1.set(combobox_values_updated[index])
                home_away_labels(event=None)

                updated_index = int(self.optionmenu_1.get().split('.')[0])
                self.get_data(index=updated_index)
            
        def change_values_option_menu_up(event):
            if self.optionmenu_1.get() == 'Select date first':
                tkinter.messagebox.showinfo("Error", "Please select date first")
                return
            # self.optionmenu_1.set(self.temp_data_optionmenu[1])
            # print(new_values_for_combobox)
            try:
                index = int(self.optionmenu_1.get().split('.')[0]) - 1
                index -= 1
                self.optionmenu_1.set(new_values_for_combobox[index])
                home_away_labels(event=None)

                updated_index = int(self.optionmenu_1.get().split('.')[0])
                self.get_data(index=updated_index)
            except:
                index = int(self.optionmenu_1.get().split('.')[0]) - 1
                index -= 1
                self.optionmenu_1.set(combobox_values_updated[index])
                home_away_labels(event=None)

                updated_index = int(self.optionmenu_1.get().split('.')[0])
                self.get_data(index=updated_index)

        photo = PhotoImage(file = r"up arrow.png")
        photoimage = photo.subsample(6, 6)

        self.up_arrow_btn = tkinter.Button(self, text = 'Click Me !', bg='#282424',activebackground='#343638', image = photoimage, borderwidth=0, cursor='hand2', command= lambda: change_values_option_menu_up(event=None))
        self.up_arrow_btn.place (x=1238,y=30)


        photo_2 = PhotoImage(file = r"down arrow.png")
        photoimage_2 = photo_2.subsample(6, 6)

        self.down_arrow_btn = tkinter.Button(self, text = 'Click Me !', bg='#282424',activebackground='#343638', image = photoimage_2, borderwidth=0, cursor='hand2', command=lambda: change_values_option_menu_down(event=None))
        self.down_arrow_btn.place (x=1238,y=750)


        self.table.bind("<Escape>", selection_remove)
        self.bind('<Up>',change_values_option_menu_up)
        self.bind('<Down>',change_values_option_menu_down)

        self.mainloop()

    def search_teams(self):
        top = customtkinter.CTkToplevel(self.frame_left)
        top.geometry('860x625')
        top.title("Search Teams")
        top.attributes("-topmost", True)
        all_teams = self.optionmenu_1._values
        # self.search_team = AutocompleteEntryListbox(master=top, width=30, font=('Helvetica', 15),completevalues=all_teams, allow_other_values= True)
        # self.search_team.grid(row=0, column=0, pady=(15, 15), padx=20)

        def filter_list():
            search_text = search_entry.get()
            listbox.delete(0, END)  # Clear the listbox
            # Filter and populate the listbox with matching items
            matching_items = [item for item in all_teams if search_text.lower() in item.lower()]
            for item in matching_items:
                listbox.insert(END, item)

        heading_label = tkinter.Label(top, text="Search Teams", font=('Helvetica', 22), fg='white', bg='#242424')
        heading_label.pack(pady=(20,15))

        search_entry = tkinter.Entry(top, font=('Helvetica', 16), width=60)
        search_entry.pack(pady=(0,22))
        search_entry.bind("<KeyRelease>", lambda event: filter_list())

        listbox = Listbox(top, width=65, height=17,background="#343638", foreground="white", font=('Helvetica', 16))
        listbox.pack()

        # Populate the listbox with initial items
        for item in all_teams:
            listbox.insert(END, item)

        def team_clicked(event):
            team_name = ''
            selection = event.widget.curselection()
            if selection:
                index = selection[0]
                data = event.widget.get(index)
                team_name=data
            else:
                team_name = ""

            search_entry.delete(0, END)
            search_entry.insert(0, team_name)

        def search_result_send(event):
            team_data = search_entry.get()
            self.optionmenu_1.set(team_data)
            index_value = int(team_data.split('.')[0])
            self.get_data(index_value)

        serach_btn = customtkinter.CTkButton(top, text="Search", font=("Helvetica", 14), command=lambda: search_result_send(event=None))
        serach_btn.pack(pady=20)
        top.bind("<Return>", search_result_send)
        listbox.bind('<<ListboxSelect>>', team_clicked)

    def add_two_hours(self,time_string):
        # Convert string to datetime object
        time_format = "%H:%M"
        time = datetime.datetime.strptime(time_string, time_format)

        # Add 2 hours to the datetime object
        time += datetime.timedelta(hours=2)

        # Convert back to string
        new_time_string = time.strftime(time_format)
        return new_time_string

    def copy(self):
        home_away_team_text = f"{self.home_label.cget('text')} vs {self.away_label.cget('text')}"
        self.clipboard_append(home_away_team_text)

    def load_file(self):
        left_1 = 0
        left_2 = 0
        right_1 = 0
        right_2 = 0

        global filename, date_filename, sport_name
        filename = fd.askopenfilename()

        with open(filename) as json_file:
            self.complete_data = json.load(json_file)
        print(self.complete_data)
        filename = filename.split('/')[-1]
        date_filename,sport_name = filename.split('_')[0],filename.split('_')[1].split('.')[0]


        total_games = self.complete_data["total_games"]
        self.complete_data.pop("total_games")
        self.games_counter.configure(text=f' {max(self.complete_data, key=int)} / {total_games}')
        self.update()

        self.optionmenu_1.configure(state='read')
        
        global combobox_values_updated
        combobox_values_updated = []
        for k,v in self.complete_data.items():
            combobox_values_updated.append(self.complete_data[k][-1])
        count = 1
        for i in self.complete_data:
            if 'away_home_points_avg' in self.complete_data[str(count)][0] and self.complete_data[str(count)][0]["final_score"] != '':
                print('new hehe')
                total_score = self.complete_data[str(count)][0]["final_score"].split(':')
                total_score = int(total_score[0]) + int(total_score[1])
                above_text = float(self.complete_data[str(count)][0]['f_result_4'])
                lower_text = int(self.complete_data[str(count)][0]['final_counter_text'].split('/')[0])
                if lower_text >= 8:
                    if total_score > above_text:
                        left_1+=1
                    else:
                        left_2+=1
                elif lower_text <= 2:
                    if total_score > above_text:
                        right_1+=1
                    else:
                        right_2+=1
                print('left ',left_1)
                print(left_2)
                print(right_1)
                print(right_2)
            count+=1

        # time.sleep(2)
        self.update()

        self.different_counters_left.configure(text=f'{left_1} / {left_2}')
        self.different_counters_right.configure(text=f'{right_1} / {right_2}')
        
        self.optionmenu_1.configure(values=combobox_values_updated)
        self.optionmenu_1.set(combobox_values_updated[0])
        

    def continue_data(self):

        with open(filename) as json_file:
            self.complete_data = json.load(json_file)
        print(self.complete_data)

        left_1, left_2 = int(self.different_counters_left.cget('text').split('/')[0]), int(self.different_counters_left.cget('text').split('/')[1])
        right_1, right_2 = int(self.different_counters_right.cget('text').split('/')[0]), int(self.different_counters_right.cget('text').split('/')[1])

        params = {
            'date': date_filename,
        }
        print(sport_name)
        print(date_filename)
        if sport_name == 'Basketball':
            url = 'https://v1.basketball.api-sports.io/games'
        elif sport_name == 'Handball':
            url = 'https://v1.handball.api-sports.io/games'

        response = requests.get(f'{url}', params=params, headers=headers)

        if str(response.status_code) == "200":
            self.optionmenu_1.configure(state='read')

            # global team_id_dict
            # team_id_dict = {}
            # self.complete_data = {}
            count = 1
            pretty_json = json.loads(response.text)
            total_len = pretty_json['results']
            nba_g_league_count = 0
            for team_data in pretty_json['response']:
                if team_data['league']['name'] == "NBA - G League":
                    nba_g_league_count+=1
            total_len = total_len - nba_g_league_count
            
            self.complete_data['total_games'] = total_len

            self.games_counter.configure(text=f'0 / {total_len}')
            self.update()
            for home_away in pretty_json['response']:
                if home_away['league']['name'] != "NBA - G League":
                    if str(count) not in self.complete_data:
                        home = home_away['teams']['home']['name']
                        home_id = home_away['teams']['home']['id']

                        away = home_away['teams']['away']['name']
                        away_id = home_away['teams']['away']['id']

                        league_id = home_away['league']['id']
                        league_name = home_away['league']['name']
                        country_name = home_away['country']['name']

                        match_time = home_away['time']
                        match_time = self.add_two_hours(match_time)

                        # league_name = home_away['league']['name']
                        # league_season = home_away['league']['season']

                        # print(f'Home Team --> Name: {home},  id: {home_id}')
                        # print(f'Away Team --> Name: {away},  id: {away_id}')
                        # print(f'League ID: {league_id}, League Name: {league_name}, Season: {league_season}')
                        # print('\n\n')

                        # match = '{:20s} vs {:20s}    {}'.format(home,away,match_time)
                        match = f'{home} vs {away}'

                        # calc = 100-len_match
                        match_2 = f"{count:02d}.      {match_time}            {match}"
                        print(match_2)
                        if match_2 not in combobox_values_updated:
                            combobox_values_updated.append(match_2)
                        print('this is count: ',count)

                        if self.optionmenu_0.get() == 'Basketball':
                            final_score = ''
                            if home_away['scores']['home']['total'] != None and home_away['scores']['away']['total'] != None:
                                final_score = f"{home_away['scores']['home']['total']} : {home_away['scores']['away']['total']}"
                        elif self.optionmenu_0.get() == 'Handball':
                            final_score = ''
                            if home_away['scores']['home'] != None and home_away['scores']['away'] != None:
                                final_score = f"{home_away['scores']['home']} : {home_away['scores']['away']}"

                        self.complete_data[count] = self.get_teams_data_advance(date_filename,home_id, away_id, league_id, final_score, league_name,country_name)
                        self.complete_data[count].append(match)
                        self.complete_data[count].append(match_2)
                        
                        # json_string = json.dumps(self.complete_data, indent = 4)

                        print('--------------------------------this complete data starts--------------------------------')
                        print(self.complete_data)
                        print('--------------------------------this complete data ends--------------------------------')

                        with open(f'{date_filename}_{self.optionmenu_0.get()}.json', 'w') as outfile:
                            json.dump(self.complete_data, outfile)

                        # print(self.complete_data[count][0])
                        print('this is final score ',final_score)
                        if 'away_home_points_avg' in self.complete_data[count][0] and final_score != '':
                            print('new hehe')
                            total_score = final_score.split(':')
                            total_score = int(total_score[0]) + int(total_score[1])
                            above_text = float(self.complete_data[count][0]['f_result_4'])
                            lower_text = int(self.complete_data[count][0]['final_counter_text'].split('/')[0])
                            if lower_text >= 8:
                                if total_score > above_text:
                                    left_1+=1
                                else:
                                    left_2+=1
                            elif lower_text <= 2:
                                if total_score > above_text:
                                    right_1+=1
                                else:
                                    right_2+=1
                            print('left ',left_1)
                            print(left_2)
                            print(right_1)
                            print(right_2)
                        self.games_counter.configure(text=f'{count} / {total_len}')
                        # time.sleep(2)
                        self.update()

                    count+=1
            self.different_counters_left.configure(text=f'{left_1} / {left_2}')
            self.different_counters_right.configure(text=f'{right_1} / {right_2}')

            print(combobox_values_updated)
            self.optionmenu_1.configure(values=combobox_values_updated)
            self.optionmenu_1.set(combobox_values_updated[0])


        else:
            tkinter.messagebox.showerror('Error', 'An error occurred, please try again!')

    def find(self,lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -1

    def get_additional_columns_data(self,home_home_points,home_away_points,average_1,average_2,url,season,team_id,league_id,date,away=False):
        if away == False:
            print(team_id, league_id, date)
            resp = requests.get(
                f'{url}?season={season}&team={team_id}&league={league_id}&date={date}',
                headers=headers)
            pretty_json = json.loads(resp.text)
            data = pretty_json['response']
            if data['country']['id'] == None:
                resp = requests.get(
                    f'{url}?season={season.split("-")[0]}&team={team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                data = pretty_json['response']
            print('*****************************************************')
            print(data)
            total_home_played = int(data['games']['played']['home'])
            for_home = int(data['points']['for']['total']['home'])
            try:
                average_by_for_home = round(for_home / total_home_played, 2)
            except:
                average_by_for_home = 0
            try:
                calc_final_second_col = round((home_home_points * average_2) / average_by_for_home, 2)
            except:
                calc_final_second_col = 0
            # print(f'total home played: {total_home_played}, total points in home: {for_home}')
            # print(f"({home_home_points} x {average_2}) / {average_by_for_home} = {calc_final_second_col}")

            total_home_played = int(data['games']['played']['home'])
            against_home = int(data['points']['against']['total']['home'])
            try:
                average_by_against_home = round(against_home / total_home_played, 2)
            except:
                average_by_against_home = 0
            try:
                calc_final_third_col = round((home_away_points * average_1) / average_by_against_home, 2)
            except:
                calc_final_third_col = 0

            # print(f'total against home played: {total_home_played}, total against points in home: {against_home}')
            # print(f"({home_away_points} x {average_1}) / {average_by_against_home} = {calc_final_third_col}")

            return [calc_final_second_col, calc_final_third_col]

        elif away == True:

            # print(team_id, league_id)
            resp = requests.get(
                f'{url}?season={season}&team={team_id}&league={league_id}&date={date}',
                headers=headers)
            pretty_json = json.loads(resp.text)
            data = pretty_json['response']
            if data['country']['id'] == None:
                resp = requests.get(
                    f'{url}?season={season.split("-")[0]}&team={team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                data = pretty_json['response']
            print('*****************************************************')
            print(data)

            total_home_played = int(data['games']['played']['away'])
            for_home = int(data['points']['for']['total']['away'])
            try:
                average_by_for_home = round(for_home / total_home_played, 2)
            except:
                average_by_for_home = 0
            try:
                calc_final_first_col = round((home_home_points * average_2) / average_by_for_home, 2)
            except:
                calc_final_first_col = 0
            # print(f'total away played: {total_home_played}, total points in away: {for_home}')
            # print(f"({home_home_points} x {average_2}) / {average_by_for_home} = {calc_final_first_col}")

            total_home_played = int(data['games']['played']['away'])
            against_home = int(data['points']['against']['total']['away'])
            try:
                average_by_against_home = round(against_home / total_home_played, 2)
            except:
                average_by_against_home = 0
            try:
                calc_final_fourth_col = round((home_away_points * average_1) / average_by_against_home, 2)
            except:
                calc_final_fourth_col = 0

            # print(f'total against away played: {total_home_played}, total against points in away: {against_home}')
            # print(f"({home_away_points} x {average_1}) / {average_by_against_home} = {calc_final_fourth_col}")

            return [calc_final_first_col,calc_final_fourth_col]


    def get_additional_columns_data_handball(self,home_home_goals,home_away_goals,average_1,average_2,url,season,team_id,league_id,date,away=False):
        if away == False:
            # print(team_id, league_id)
            resp = requests.get(
                f'{url}?season={season}&team={team_id}&league={league_id}&date={date}',
                headers=headers)
            pretty_json = json.loads(resp.text)
            data = pretty_json['response']
            if data['country']['id'] == None:
                resp = requests.get(
                    f'{url}?season={season.split("-")[0]}&team={team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                data = pretty_json['response']
            total_home_played = int(data['games']['played']['home'])
            for_home = int(data['goals']['for']['total']['home'])
            try:
                average_by_for_home = round(for_home / total_home_played, 2)
            except:
                average_by_for_home = 0
            try:
                calc_final_second_col = round((home_home_goals * average_2) / average_by_for_home, 2)
            except:
                calc_final_second_col = 0
            # print(f'total home played: {total_home_played}, total goals in home: {for_home}')
            # print(f"({home_home_goals} x {average_2}) / {average_by_for_home} = {calc_final_second_col}")

            total_home_played = int(data['games']['played']['home'])
            against_home = int(data['goals']['against']['total']['home'])
            try:
                average_by_against_home = round(against_home / total_home_played, 2)
            except:
                average_by_against_home = 0
            try:
                calc_final_third_col = round((home_away_goals * average_1) / average_by_against_home, 2)
            except:
                calc_final_third_col = 0
            # print(f'total against home played: {total_home_played}, total against goals in home: {against_home}')
            # print(f"({home_away_goals} x {average_1}) / {average_by_against_home} = {calc_final_third_col}")

            return [calc_final_second_col, calc_final_third_col]

        elif away == True:

            # print(team_id, league_id)
            resp = requests.get(
                f'{url}?season={season}&team={team_id}&league={league_id}&date={date}',
                headers=headers)
            pretty_json = json.loads(resp.text)
            data = pretty_json['response']
            if data['country']['id'] == None:
                resp = requests.get(
                    f'{url}?season={season.split("-")[0]}&team={team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                data = pretty_json['response']
            total_home_played = int(data['games']['played']['away'])
            for_home = int(data['goals']['for']['total']['away'])
            try:
                average_by_for_home = round(for_home / total_home_played, 2)
            except:
                average_by_for_home = 0
            try:
                calc_final_first_col = round((home_home_goals * average_2) / average_by_for_home, 2)
            except:
                calc_final_first_col = 0
            # print(f'total away played: {total_home_played}, total goals in away: {for_home}')
            # print(f"({home_home_goals} x {average_2}) / {average_by_for_home} = {calc_final_first_col}")

            total_home_played = int(data['games']['played']['away'])
            against_home = int(data['goals']['against']['total']['away'])
            try:
                average_by_against_home = round(against_home / total_home_played, 2)
            except:
                average_by_against_home = 0
            try:
                calc_final_fourth_col = round((home_away_goals * average_1) / average_by_against_home, 2)
            except:
                calc_final_fourth_col = 0

            # print(f'total against away played: {total_home_played}, total against goals in away: {against_home}')
            # print(f"({home_away_goals} x {average_1}) / {average_by_against_home} = {calc_final_fourth_col}")

            return [calc_final_first_col,calc_final_fourth_col]

    def get_away_home_ids(self, url, away_home_ids, league_id):
        away_home_points_avg = []

        for id in away_home_ids:
            if len(away_home_points_avg) == 5:
                break
            print(
                f'------------------------------------------------------------------------------------------------------------{id[2]}------------------------------------------------------------------------------------------------------------')
            counter = 0
            found_in_first_season = False
            points = 0

            for season in seasons:
                resp = requests.get(
                    f'{url}?season={season}&team={id[1]}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={id[1]}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # count = False

                # print(pretty_json['response'].index())
                # index_value = next((index for (index, d) in enumerate(pretty_json['response']) if d["id"] == str(id[0])), None)
                # print(index_value)

                main_lst = pretty_json['response']
                # print(json.dumps(pretty_json,indent=3))
                main_lst.reverse()
                index_value = self.find(main_lst, 'id', id[0])

                if index_value != -1:
                    found_in_first_season = True

                if counter >= 5:
                    break
                else:
                    if found_in_first_season == True:
                        # print('This is index value ',index_value)
                        # print('Finding match ID: ', id[0])
                        for i in main_lst[index_value + 1:]:
                            # print(i)
                            if str(i['teams']['home']['id']) == str(id[1]) and i['scores']['home']['total'] != None:
                                if (str(i['scores']['home']['total']) != '20' and str(i['scores']['home']['total']) != '0') or (str(i['scores']['away']['total']) != '20' and str(i['scores']['away']['total']) != '0'):

                                    if i['scores']['home']['over_time'] != None:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(i['id']) + '    ' + str(i['scores']['home']['total']-i['scores']['home']['over_time']) + ' vs ' + str(i['scores']['away']['total']-i['scores']['away']['over_time']) + ' season: ' + season)
                                    else:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(i['id']) + '    ' + str(i['scores']['home']['total']) + ' vs ' + str(i['scores']['away']['total']) + ' season: ' + season)

                                    # print(i['id'])

                                    points += i['scores']['home']['total']
                                    if i['scores']['home']['over_time'] != None:
                                        points -= i['scores']['home']['over_time']

                                    counter += 1

                            if counter == 5:
                                break

                    # for i in  pretty_json['response']:
                    #     if str(i['id']) == str(id[0]):

                found_in_first_season = True
            print('Total points ', points)
            if counter == 0 or counter == 1:
                points = 0
            else:
                points = round(points / counter, 2)
            print(f'points {points} for team {id[2]} counter {counter}')
            away_home_points_avg.append(points)
        return away_home_points_avg

    def get_home_away_ids(self, url, home_away_ids, league_id):

        home_away_points_avg = []

        for id in home_away_ids:
            if len(home_away_points_avg) == 5:
                break
            print(f'------------------------------------------------------------------------------------------------------------{id[2]}------------------------------------------------------------------------------------------------------------')
            counter = 0
            found_in_first_season = False
            points = 0
            for season in seasons:
                resp = requests.get(
                    f'{url}?season={season}&team={id[1]}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={id[1]}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # count = False

                # print(pretty_json['response'].index())
                # index_value = next((index for (index, d) in enumerate(pretty_json['response']) if d["id"] == str(id[0])), None)
                # print(index_value)
                main_lst = pretty_json['response']
                # print(json.dumps(pretty_json,indent=3))
                main_lst.reverse()
                index_value = self.find(main_lst, 'id', id[0])
                print('length of list ',len(main_lst))
                if index_value != -1:
                    found_in_first_season = True

                if counter >= 5:
                    break
                else:
                    if found_in_first_season == True:
                        print('This is index value ',index_value)
                        print('Finding match ID: ',id[0])
                        for i in main_lst[index_value + 1:]:
                            # print(i)
                            if str(i['teams']['away']['id']) == str(id[1]) and i['scores']['away']['total'] != None:
                                if (str(i['scores']['home']['total']) != '20' and str(i['scores']['home']['total']) != '0') or (str(i['scores']['away']['total']) != '20' and str(i['scores']['away']['total']) != '0'):

                                    if i['scores']['home']['over_time'] != None and (i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(
                                            i['scores']['home']['total'] - i['scores']['home']['over_time']) + ' vs ' + str(
                                            i['scores']['away']['total'] - i['scores']['away'][
                                                'over_time']) + ' season: ' + season)
                                    else:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(i['scores']['home']['total']) + ' vs ' + str(
                                            i['scores']['away']['total']) + ' season: ' + season)

                                    points += i['scores']['away']['total']
                                    if i['scores']['away']['over_time'] != None:
                                        points -= i['scores']['away']['over_time']
                                    counter += 1

                            if counter == 5:
                                break

                    # for i in  pretty_json['response']:
                    #     if str(i['id']) == str(id[0]):

                found_in_first_season = True
            print('Total points ', points)
            if counter == 0 or counter == 1:
                points = 0
            else:
                points = round(points / counter, 2)
            print(f'points {points} for team {id[2]} counter {counter}')
            print(f'points {points} for team {id[2]}')

            home_away_points_avg.append(points)

        return home_away_points_avg

    def get_away_home_ids_handball(self, url, away_home_ids, league_id):
        seasons = ['2023-2024','2022-2023', '2021-2022']
        print(away_home_ids)
        away_home_points_avg = []
        for id in away_home_ids:
            if len(away_home_points_avg) == 5:
                break
            print(f'------------------------------------------------------------------------------------------------------------{id[2]}------------------------------------------------------------------------------------------------------------')
            counter = 0
            found_in_first_season = False
            points = 0
            for season in seasons:
                resp = requests.get(
                    f'{url}?season={season}&team={id[1]}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={id[1]}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # count = False

                # print(pretty_json['response'].index())
                # index_value = next((index for (index, d) in enumerate(pretty_json['response']) if d["id"] == str(id[0])), None)
                # print(index_value)
                main_lst = pretty_json['response']
                # print(json.dumps(pretty_json,indent=3))
                main_lst.reverse()
                index_value = self.find(main_lst, 'id', id[0])

                if index_value != -1:
                    found_in_first_season = True

                if counter >= 5:
                    break
                else:
                    if found_in_first_season == True:
                        # print('This is index value ',index_value)
                        # print('Finding match ID: ',id[0])
                        for i in main_lst[index_value + 1:]:
                            # print(i)
                            if str(i['teams']['home']['id']) == str(id[1]) and i['scores']['home'] != None:
                                if (i['scores']['home'] != 10 and i['scores']['away'] != 0) or (
                                        i['scores']['away'] != 10 and i['scores']['home'] != 0):

                                    print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                        i['id']) + '    ' + str(i['scores']['home']) + ' vs ' + str(
                                        i['scores']['away']) + ' season: ' + season)
                                    points += i['scores']['home']
                                    counter += 1

                            if counter == 5:
                                break

                    # for i in  pretty_json['response']:
                    #     if str(i['id']) == str(id[0]):

                found_in_first_season = True
            print('Total points ', points)
            if counter == 0 or counter == 1:
                points = 0
            else:
                points = round(points / counter, 2)
            print(f'points {points} for team {id[2]} counter {counter}')
            away_home_points_avg.append(points)
            print(f'points {points} for team {id[2]}')

        return away_home_points_avg

    def get_home_away_ids_handball(self, url, home_away_ids, league_id):
        seasons = ['2023-2024','2022-2023', '2021-2022']

        print(home_away_ids)
        home_away_points_avg = []
        for id in home_away_ids:
            if len(home_away_points_avg) == 5:
                break
            print(f'------------------------------------------------------------------------------------------------------------{id[2]}------------------------------------------------------------------------------------------------------------')
            counter = 0
            found_in_first_season = False
            points = 0
            for season in seasons:
                resp = requests.get(
                    f'{url}?season={season}&team={id[1]}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                # count = False

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={id[1]}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # print(pretty_json['response'].index())
                # index_value = next((index for (index, d) in enumerate(pretty_json['response']) if d["id"] == str(id[0])), None)
                # print(index_value)
                main_lst = pretty_json['response']
                # print(json.dumps(pretty_json,indent=3))
                main_lst.reverse()
                index_value = self.find(main_lst, 'id', id[0])

                if index_value != -1:
                    found_in_first_season = True

                if counter >= 5:
                    break
                else:
                    if found_in_first_season == True:
                        # print('This is index value ', index_value)
                        # print('Finding match ID: ', id[0])
                        for i in main_lst[index_value + 1:]:
                            # print(i)
                            if str(i['teams']['away']['id']) == str(id[1]) and i['scores']['away'] != None:
                                if (i['scores']['home'] != 10 and i['scores']['away'] != 0) or (
                                        i['scores']['away'] != 10 and i['scores']['home'] != 0):

                                    print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                        i['id']) + '    ' + str(i['scores']['home']) + ' vs ' + str(
                                        i['scores']['away']) + ' season: ' + season)
                                    # print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                    #     i['id']) + '    ' + str(i['scores']['home']['total']) + ' vs ' + str(
                                    #     i['scores']['away']['total']) + ' season: ' + season)
                                    points += i['scores']['away']
                                    counter += 1

                            if counter == 5:
                                break

                    # for i in  pretty_json['response']:
                    #     if str(i['id']) == str(id[0]):

                found_in_first_season = True
            if counter == 0 or counter == 1:
                points = 0
            else:
                points = round(points / counter, 2)
            print(f'points {points} for team {id[2]} counter {counter}')
            home_away_points_avg.append(points)

        return home_away_points_avg

    def get_teams_data_advance(self,date,home_team_id,away_team_id,league_id,final_score,league_name,country_name):

        if self.optionmenu_0.get() == 'Basketball':
            seasons = ['2023-2024','2022-2023', '2021-2022']

            url = 'https://v1.basketball.api-sports.io/games'

            # home = self.optionmenu_1.get().split('vs')[0].strip(' ').split('            ')[1].strip(' ')
            # away = self.optionmenu_1.get().split('vs')[1].strip(' ')

            # print(home)
            # print(away)

            # home_team_id, away_team_id, league_id = team_id_dict[self.optionmenu_1.get()][0], \
            #                                         team_id_dict[self.optionmenu_1.get()][1], \
            #                                         team_id_dict[self.optionmenu_1.get()][2]

            home_home_points = []
            home_away_points = []

            away_home_points = []
            away_away_points = []

            # home_away_points_avg = []

            home_away_ids = []
            away_home_ids = []

            for season in seasons:
                #  fetching data for "home" home team

                temp_lst_1 = []
                temp_lst_2 = []
                resp = requests.get(
                    f'{url}?season={season}&team={home_team_id}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={home_team_id}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                print('this is link ' + f'{url}?season={season}&team={home_team_id}&league={league_id}')
                print('this is status ',resp.status_code)
                # date_index_counter = 0
                # for temp_date in pretty_json['response']:
                #     raw_date = temp_date['date'].split('T')[0]
                #     # if raw_date < str(date):
                #     print(raw_date)
                        # break
                # print(pretty_json)
                temp_lst_6 = []
                for i in pretty_json['response']:
                    print('going through')
                    if i['date'].split('T')[0] < str(date):
                        print('going through again')
                        print(i['date'].split('T')[0])
                        if str(i['teams']['home']['id']) == str(home_team_id):
                            if (str(i['scores']['home']['total']) != '20' and str(
                                    i['scores']['home']['total']) != '0') or (
                                    str(i['scores']['away']['total']) != '20' and str(
                                    i['scores']['away']['total']) != '0'):
                                if i['scores']['home']['total'] != None and (
                                        i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                    total = i['scores']['home']['total']
                                    if i['scores']['home']['over_time'] != None:
                                        total -= i['scores']['home']['over_time']
                                    temp_lst_1.append(total)

                                    if i['scores']['home']['over_time'] != None:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(
                                            i['scores']['home']['total'] - i['scores']['home']['over_time']) + ' vs ' + str(
                                            i['scores']['away']['total'] - i['scores']['away'][
                                                'over_time']) + ' season: ' + season)
                                    else:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(i['scores']['home']['total']) + ' vs ' + str(
                                            i['scores']['away']['total']) + ' season: ' + season)
                                    # temp_lst_3.append(i['scores']['home']['total'] - i['scores']['home']['over_time'])

                                    match_id = i['id']
                                    away_team_here_id = i['teams']['away']['id']
                                    # print(i['teams']['home']['name'])
                                    temp_lst_6.append(
                                        [match_id, away_team_here_id, i['teams']['away']['name'], i['league']['season']])

                                if i['scores']['away']['total'] != None and (
                                        i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                    total = i['scores']['away']['total']
                                    if i['scores']['away']['over_time'] != None:
                                        total -= i['scores']['away']['over_time']
                                    temp_lst_2.append(total)

                temp_lst_6.reverse()
                # print(temp_lst_6)
                for z in temp_lst_6:
                    home_away_ids.append(z)

                temp_lst_1.reverse()
                temp_lst_2.reverse()

                for i in temp_lst_1:
                    home_home_points.append(i)
                    # print(i)

                for i in temp_lst_2:
                    home_away_points.append(i)
                    # print(i)

                #  fetching data for "home" away team

                # temp_lst = []
                # resp = requests.get(f'https://v1.basketball.api-sports.io/games?season={season}&team={home_team_id}', headers=headers)
                # pretty_json = json.loads(resp.text)
                # print(pretty_json)
                # for i in pretty_json['response']:
                #     if str(i['teams']['home']['id']) == str(home_team_id):
                #         if i['scores']['away']['total'] != None:
                #             temp_lst.append(i['scores']['away']['total'])
                # temp_lst.reverse()
                # for i in temp_lst:
                #     home_away_points.append(i)
                #     # print(i)

                temp_lst_3 = []
                temp_lst_4 = []
                resp = requests.get(
                    f'{url}?season={season}&team={away_team_id}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={away_team_id}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # print(pretty_json)

                temp_lst_5 = []
                for i in pretty_json['response']:
                    if i['date'].split('T')[0] < str(date):
                        print(i['date'].split('T')[0])
                        if str(i['teams']['away']['id']) == str(away_team_id):
                            if (str(i['scores']['home']['total']) != '20' and str(
                                    i['scores']['home']['total']) != '0') or (
                                    str(i['scores']['away']['total']) != '20' and str(
                                    i['scores']['away']['total']) != '0'):
                                if i['scores']['home']['total'] != None and (
                                        i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                    total = i['scores']['home']['total']
                                    if i['scores']['home']['over_time'] != None:
                                        total -= i['scores']['home']['over_time']

                                    temp_lst_3.append(total)
                                    if i['scores']['home']['over_time'] != None:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(
                                            i['scores']['home']['total'] - i['scores']['home']['over_time']) + ' vs ' + str(
                                            i['scores']['away']['total'] - i['scores']['away'][
                                                'over_time']) + ' season: ' + season)
                                    else:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(i['scores']['home']['total']) + ' vs ' + str(
                                            i['scores']['away']['total']) + ' season: ' + season)
                                    # temp_lst_3.append(i['scores']['home']['total'] - i['scores']['home']['over_time'])

                                if i['scores']['away']['total'] != None and (
                                        i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                    total = i['scores']['away']['total']
                                    if i['scores']['away']['over_time'] != None:
                                        total -= i['scores']['away']['over_time']
                                    temp_lst_4.append(total)
                                    # temp_lst_4.append(i['scores']['away']['total'] - i['scores']['away']['over_time'])
                                    match_id = i['id']
                                    home_team_here_id = i['teams']['home']['id']
                                    # print(i['teams']['home']['name'])
                                    temp_lst_5.append(
                                        [match_id, home_team_here_id, i['teams']['home']['name'], i['league']['season']])
                                    # for team_season in seasons:
                                    #     away_home = requests.get(f'https://v1.basketball.api-sports.io/games?season={team_season}&team={home_team_here_id}',headers=headers)
                                    #     away_home_json = json.loads(away_home.text)
                                    #     # print(away_home_json)
                                    #     inner_temp = []
                                    #     count = False
                                    #     for j in away_home_json['response']:
                                    #         # print(j['teams']['home']['name'])
                                    #         if count == True:
                                    #             if str(j['teams']['home']['id']) == str(home_team_here_id):
                                    #                 if j['scores']['home']['total'] != None:
                                    #                     inner_temp.append(j['scores']['home']['total'])
                                    #         if str(j['id']) == str(match_id):
                                    #             count = True
                                    #     inner_temp.reverse()
                                    #     for temp in inner_temp:
                                    #         temp_lst_5.append(temp)
                                    #     # print(temp_lst_5)
                                    # away_home_ids.append(temp_lst_5)

                temp_lst_5.reverse()

                for z in temp_lst_5:
                    away_home_ids.append(z)
                    # print(i)

                temp_lst_3.reverse()
                temp_lst_4.reverse()

                for i in temp_lst_3:
                    away_home_points.append(i)
                    # print(i)

                for i in temp_lst_4:
                    away_away_points.append(i)
                    # print(i)

            # print(away_home_points_avg)
            print(away_home_points)
            print(home_home_points)
            print(away_away_points)
            # print(home_away_points_avg)
            print(home_away_points)
            print(away_home_ids[:5])
            print(home_away_ids[:5])

            away_home_points_avg = self.get_away_home_ids(url, away_home_ids, league_id)

            home_away_points_avg = self.get_home_away_ids(url, home_away_ids, league_id)

            if len(away_home_points_avg) >= 5 and len(home_away_points_avg) >= 5:

                for i in range(5):
                    if away_home_points_avg[i] == 0:
                        away_home_points_avg[i] = away_home_points[i]

                    if home_away_points_avg[i] == 0:
                        home_away_points_avg[i] = home_away_points[i]

                away_home_points_avg.append(round(sum(away_home_points_avg) / len(away_home_points_avg), 2))

                away_home_points = away_home_points[:5]
                away_home_points.append(round(sum(away_home_points) / len(away_home_points), 2))

                home_home_points = home_home_points[:5]
                home_home_points.append(round(sum(home_home_points) / len(home_home_points), 2))

                away_away_points = away_away_points[:5]
                away_away_points.append(round(sum(away_away_points) / len(away_away_points), 2))

                # away_away_points = away_away_points[:5]
                # away_away_points.append(round(sum(away_away_points) / len(away_away_points), 2))
                #

                home_away_points_avg.append(round(sum(home_away_points_avg) / len(home_away_points_avg), 2))

                home_away_points = home_away_points[:5]
                home_away_points.append(round(sum(home_away_points) / len(home_away_points), 2))

            # home_home_points[:5]
            # away_away_points[:5]
            # home_away_points_avg
            # home_away_points[:5]

            print(away_home_points_avg)
            print(away_home_points)
            print(home_home_points)
            print(away_away_points)
            print(home_away_points_avg)
            print(home_away_points)

            if len(away_home_points_avg) >= 6 and len(away_home_points) >= 6 and len(home_home_points) >= 6 and len(
                    away_away_points) >= 6 and len(home_away_points_avg) >= 6 and len(home_away_points) >= 6:
                
                resp = requests.get(
                    f'https://v1.basketball.api-sports.io/statistics?season=2023-2024&team={home_team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                        f'https://v1.basketball.api-sports.io/statistics?season=2023&team={home_team_id}&league={league_id}&date={date}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                        f'https://v1.basketball.api-sports.io/statistics?season=2022-2023&team={home_team_id}&league={league_id}&date={date}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                        f'https://v1.basketball.api-sports.io/statistics?season=2022&team={home_team_id}&league={league_id}&date={date}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] != None:
                    data = pretty_json['response']
                    print(data)
                    games_played_home = int(data['games']['played']['home'])
                    for_total_home = int(data['points']['for']['total']['home'])
                    against_total_home = int(data['points']['against']['total']['home'])
                    try:
                        average_of_total_against_home_points_by_games_played = against_total_home / games_played_home
                    except:
                        average_of_total_against_home_points_by_games_played = 0
                    try:
                        average_of_total_for_home_points_by_games_played = for_total_home / games_played_home
                    except:
                        average_of_total_for_home_points_by_games_played = 0
                else:
                    average_of_total_against_home_points_by_games_played = 'No data'
                    average_of_total_for_home_points_by_games_played = 'No data'

                resp = requests.get(
                    f'https://v1.basketball.api-sports.io/statistics?season=2023-2024&team={away_team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                        f'https://v1.basketball.api-sports.io/statistics?season=2023&team={away_team_id}&league={league_id}&date={date}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)
                    #print(f'https://v1.basketball.api-sports.io/statistics?season=2022&team={away_team_id}&league={league_id}&date={date}')
                    print(True)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                    f'https://v1.basketball.api-sports.io/statistics?season=2022-2023&team={away_team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                        f'https://v1.basketball.api-sports.io/statistics?season=2022&team={away_team_id}&league={league_id}&date={date}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)
                    #print(f'https://v1.basketball.api-sports.io/statistics?season=2022&team={away_team_id}&league={league_id}&date={date}')
                    print(True)

                if pretty_json['response']['country']['id'] != None:
                    data = pretty_json['response']
                    print(data)

                    games_played_away = int(data['games']['played']['away'])
                    for_total_away = int(data['points']['for']['total']['away'])
                    against_total_away = int(data['points']['against']['total']['away'])
                    try:
                        average_of_total_against_away_points_by_games_played = against_total_away / games_played_away
                    except:
                        average_of_total_against_away_points_by_games_played = 0
                    try:
                        average_of_total_for_away_points_by_games_played = for_total_away / games_played_away
                    except:
                        average_of_total_for_away_points_by_games_played = 0
                else:
                    average_of_total_against_away_points_by_games_played = 'No data'
                    average_of_total_for_away_points_by_games_played = 'No data'
                # print(against_total_away, '/', games_played_away)
                # print(for_total_home, '/', games_played_home)
                # print(against_total_home, '/', games_played_home)
                # print(for_total_away, '/', games_played_away)

                first_column_second_row = []
                second_column_second_row = []
                third_column_second_row = []
                fourth_column_second_row = []

                counter_for_scores = 0
                for team_id in away_home_ids[:5]:
                    print(average_of_total_against_home_points_by_games_played,average_of_total_for_home_points_by_games_played)
                    if average_of_total_against_home_points_by_games_played != 'No data' and average_of_total_for_home_points_by_games_played != 'No data':
                        final_results_second_row = self.get_additional_columns_data(
                            home_home_points=away_home_points[counter_for_scores],
                            home_away_points=away_away_points[counter_for_scores],
                            average_1=average_of_total_against_home_points_by_games_played,
                            average_2=average_of_total_for_home_points_by_games_played,
                            away=False, url='https://v1.basketball.api-sports.io/statistics',
                            season='2023-2024', team_id=team_id[1], league_id=league_id, date=date)
                        
                        if final_results_second_row == [0,0]:

                            final_results_second_row = self.get_additional_columns_data(
                            home_home_points=away_home_points[counter_for_scores],
                            home_away_points=away_away_points[counter_for_scores],
                            average_1=average_of_total_against_home_points_by_games_played,
                            average_2=average_of_total_for_home_points_by_games_played,
                            away=False, url='https://v1.basketball.api-sports.io/statistics',
                            season='2022-2023', team_id=team_id[1], league_id=league_id, date=date)
                    else:
                        final_results_second_row = ['No data','No data']
                    counter_for_scores += 1

                    print(final_results_second_row)
                    second_column_second_row.append(final_results_second_row[0])
                    third_column_second_row.append(final_results_second_row[1])

                print('---------------------------------------------------------------------')
                counter_for_scores = 0
                for team_id in home_away_ids[:5]:
                    print(average_of_total_against_away_points_by_games_played,average_of_total_for_away_points_by_games_played)
                    if average_of_total_against_away_points_by_games_played != 'No data' and average_of_total_for_away_points_by_games_played != 'No data':
                        final_results_second_row = self.get_additional_columns_data(
                            home_home_points=home_away_points[counter_for_scores],
                            home_away_points=home_home_points[counter_for_scores],
                            average_1=average_of_total_against_away_points_by_games_played,
                            average_2=average_of_total_for_away_points_by_games_played,
                            away=True, url='https://v1.basketball.api-sports.io/statistics',
                            season='2023-2024', team_id=team_id[1], league_id=league_id, date=date)
                        if final_results_second_row == [0,0]:
                            final_results_second_row = self.get_additional_columns_data(
                            home_home_points=home_away_points[counter_for_scores],
                            home_away_points=home_home_points[counter_for_scores],
                            average_1=average_of_total_against_away_points_by_games_played,
                            average_2=average_of_total_for_away_points_by_games_played,
                            away=True, url='https://v1.basketball.api-sports.io/statistics',
                            season='2022-2023', team_id=team_id[1], league_id=league_id, date=date)
                    else:
                        final_results_second_row = ['No data','No data']
                    counter_for_scores += 1

                    print(final_results_second_row)
                    fourth_column_second_row.append(final_results_second_row[0])
                    first_column_second_row.append(final_results_second_row[1])

                try:
                    first_column_second_row.append(round(sum(first_column_second_row) / len(first_column_second_row), 2))
                except:
                    first_column_second_row.append('None')
                try:
                    second_column_second_row.append(round(sum(second_column_second_row) / len(second_column_second_row), 2))
                except:
                    second_column_second_row.append('None')
                try:
                    third_column_second_row.append(round(sum(third_column_second_row) / len(third_column_second_row), 2))
                except:
                    third_column_second_row.append('None')
                try:
                    fourth_column_second_row.append(round(sum(fourth_column_second_row) / len(fourth_column_second_row), 2))
                except:
                    fourth_column_second_row.append('None')

                print(first_column_second_row)
                print(second_column_second_row)
                print(third_column_second_row)
                print(fourth_column_second_row)

                final_second_row_results = [first_column_second_row, second_column_second_row, third_column_second_row,
                                            fourth_column_second_row]

                print('checking')
                print(away_away_points[-1], 'numerator')
                print(away_home_points[-1], 'denominator')
                print(home_away_points[-1], 'numerator')
                print(home_home_points[-1], 'denominator')
                print('checked')
                a = round(away_home_points[-1] / away_home_points_avg[-1], 2)  # for column 1 and 2
                b = round(home_away_points[-1] / home_away_points_avg[-1], 2)  # for column 5 and 6

                a_final = round(a * home_home_points[-1], 2)  # for column 3 and 4
                b_final = round(b * away_away_points[-1], 2)  # for column 3 and 4
                result = round(a_final + b_final, 2)  # for column 3 and 4

                f_result_1 = a
                f_result_2 = f'{a_final} = {result} = {b_final}'
                f_result_3 = b
                f_result_4 = round(home_home_points[-1] + away_away_points[-1], 2)

                higher_counter = 0
                higher_counter_2 = 0

                for i in range(5):
                    if away_home_points[i] >= away_home_points_avg[i]:
                        higher_counter += 1
                for i in range(5):
                    if home_away_points[i] >= home_away_points_avg[i]:
                        higher_counter_2 += 1

                final_counter = higher_counter + higher_counter_2

                higher_counter_text = f'{higher_counter} / 5'
                higher_counter_2_text = f'{higher_counter_2} / 5'
                final_counter_text = f'{final_counter} / 10'

                final_dict = [{
                    "away_home_points_avg" : away_home_points_avg,
                    "away_home_points" : away_home_points,
                    "home_home_points" : home_home_points,
                    "away_away_points" : away_away_points,
                    "home_away_points_avg" : home_away_points_avg,
                    "home_away_points" : home_away_points,
                    "f_result_1":f_result_1,
                    "f_result_2" : f_result_2,
                    "f_result_3": f_result_3,
                    "f_result_4":f_result_4,
                    "higher_counter_text":higher_counter_text,
                    "final_counter_text":final_counter_text,
                    "higher_counter_2_text":higher_counter_2_text,
                    "final_score":final_score,
                    "league_name":league_name,
                    "country_name":country_name,
                    "final_second_row_results":final_second_row_results

                }]

            else:
                final_dict = [{"final_score":final_score,
                               "league_name":league_name,
                               "country_name":country_name}]

            return final_dict

        elif self.optionmenu_0.get() == 'Handball':
            seasons = ['2023-2024','2022-2023', '2021-2022']

            url = 'https://v1.handball.api-sports.io/games'

            # home = self.optionmenu_1.get().split('vs')[0].strip(' ').split('            ')[1].strip(' ')
            # away = self.optionmenu_1.get().split('vs')[1].strip(' ')
            #
            # print(home)
            # print(away)

            # home_team_id, away_team_id, league_id = team_id_dict[self.optionmenu_1.get()][0], \
            #                                         team_id_dict[self.optionmenu_1.get()][1], \
            #                                         team_id_dict[self.optionmenu_1.get()][2]
            #
            home_home_points = []
            home_away_points = []

            away_home_points = []
            away_away_points = []

            home_away_ids = []
            away_home_ids = []

            for season in seasons:
                #  fetching data for "home" home team

                temp_lst_1 = []
                temp_lst_2 = []
                resp = requests.get(
                    f'{url}?season={season}&team={home_team_id}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={home_team_id}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # print(pretty_json)
                temp_lst_6 = []
                for i in pretty_json['response']:
                    if str(i['teams']['home']['id']) == str(home_team_id):
                        if (i['scores']['home'] != 10 and i['scores']['away'] != 0) or (i['scores']['away'] != 10 and i['scores']['home'] != 0):

                            if i['scores']['home'] != None and (
                                    i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                temp_lst_1.append(i['scores']['home'])
                                match_id = i['id']
                                away_team_here_id = i['teams']['away']['id']
                                # print(i['teams']['home']['name'])
                                temp_lst_6.append([match_id, away_team_here_id, i['teams']['away']['name']])

                            if i['scores']['away'] != None and (
                                    i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                temp_lst_2.append(i['scores']['away'])

                temp_lst_6.reverse()
                # print(temp_lst_6)
                for z in temp_lst_6:
                    home_away_ids.append(z)

                temp_lst_1.reverse()
                temp_lst_2.reverse()

                for i in temp_lst_1:
                    home_home_points.append(i)
                    # print(i)

                for i in temp_lst_2:
                    home_away_points.append(i)
                    # print(i)

                #  fetching data for "home" away team

                # temp_lst = []
                # resp = requests.get(f'https://v1.basketball.api-sports.io/games?season={season}&team={home_team_id}', headers=headers)
                # pretty_json = json.loads(resp.text)
                # print(pretty_json)
                # for i in pretty_json['response']:
                #     if str(i['teams']['home']['id']) == str(home_team_id):
                #         if i['scores']['away']['total'] != None:
                #             temp_lst.append(i['scores']['away']['total'])
                # temp_lst.reverse()
                # for i in temp_lst:
                #     home_away_points.append(i)
                #     # print(i)

                temp_lst_3 = []
                temp_lst_4 = []
                resp = requests.get(
                    f'{url}?season={season}&team={away_team_id}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={away_team_id}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # print(pretty_json)
                temp_lst_5 = []
                for i in pretty_json['response']:
                    if str(i['teams']['away']['id']) == str(away_team_id):
                        if (i['scores']['home'] != 10 and i['scores']['away'] != 0) or (i['scores']['away'] != 10 and i['scores']['home'] != 0):

                            if i['scores']['home'] != None and (
                                    i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                temp_lst_3.append(i['scores']['home'])

                            if i['scores']['away'] != None and (
                                    i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                temp_lst_4.append(i['scores']['away'])
                                match_id = i['id']
                                home_team_here_id = i['teams']['home']['id']
                                # print(i['teams']['home']['name'])
                                temp_lst_5.append([match_id, home_team_here_id, i['teams']['home']['name']])
                                # for team_season in seasons:
                                #     away_home = requests.get(f'https://v1.basketball.api-sports.io/games?season={team_season}&team={home_team_here_id}',headers=headers)
                                #     away_home_json = json.loads(away_home.text)
                                #     # print(away_home_json)
                                #     inner_temp = []
                                #     count = False
                                #     for j in away_home_json['response']:
                                #         # print(j['teams']['home']['name'])
                                #         if count == True:
                                #             if str(j['teams']['home']['id']) == str(home_team_here_id):
                                #                 if j['scores']['home']['total'] != None:
                                #                     inner_temp.append(j['scores']['home']['total'])
                                #         if str(j['id']) == str(match_id):
                                #             count = True
                                #     inner_temp.reverse()
                                #     for temp in inner_temp:
                                #         temp_lst_5.append(temp)
                                #     # print(temp_lst_5)
                                # away_home_ids.append(temp_lst_5)

                temp_lst_5.reverse()

                for z in temp_lst_5:
                    away_home_ids.append(z)
                    # print(i)

                temp_lst_3.reverse()
                temp_lst_4.reverse()

                for i in temp_lst_3:
                    away_home_points.append(i)
                    # print(i)

                for i in temp_lst_4:
                    away_away_points.append(i)
                    # print(i)
            # print('this is home away',away_home_ids)

            # print('this is away home',home_away_ids)

            home_away_points_avg = self.get_home_away_ids_handball(url, home_away_ids, league_id)
            away_home_points_avg = self.get_away_home_ids_handball(url, away_home_ids, league_id)

            if len(away_home_points_avg) >= 5 and len(home_away_points_avg) >= 5:

                for i in range(5):
                    if away_home_points_avg[i] == 0:
                        away_home_points_avg[i] = away_home_points[i]

                    if home_away_points_avg[i] == 0:
                        home_away_points_avg[i] = home_away_points[i]

                away_home_points_avg.append(round(sum(away_home_points_avg) / len(away_home_points_avg), 2))

                away_home_points = away_home_points[:5]
                away_home_points.append(round(sum(away_home_points) / len(away_home_points), 2))

                home_home_points = home_home_points[:5]
                home_home_points.append(round(sum(home_home_points) / len(home_home_points), 2))

                away_away_points = away_away_points[:5]
                away_away_points.append(round(sum(away_away_points) / len(away_away_points), 2))

                # away_away_points = away_away_points[:5]
                # away_away_points.append(round(sum(away_away_points) / len(away_away_points), 2))
                #

                home_away_points_avg.append(round(sum(home_away_points_avg) / len(home_away_points_avg), 2))

                home_away_points = home_away_points[:5]
                home_away_points.append(round(sum(home_away_points) / len(home_away_points), 2))

            # home_home_points[:5]
            # away_away_points[:5]
            # home_away_points_avg
            # home_away_points[:5]

            print(away_home_points_avg)
            print(away_home_points)
            print(home_home_points)
            print(away_away_points)
            print(home_away_points_avg)
            print(home_away_points)

            if len(away_home_points_avg) >= 6 and len(away_home_points) >= 6 and len(home_home_points) >= 6 and len(
                    away_away_points) >= 6 and len(home_away_points_avg) >= 6 and len(home_away_points) >= 6:

                resp = requests.get(
                    f'https://v1.handball.api-sports.io/teams/statistics?season=2023&team={home_team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                    f'https://v1.handball.api-sports.io/teams/statistics?season=2022&team={home_team_id}&league={league_id}&date={date}',
                    headers=headers)
                    pretty_json = json.loads(resp.text)
                data = pretty_json['response']
                print('this is ', data)
                games_played_home = int(data['games']['played']['home'])
                for_total_home = int(data['goals']['for']['total']['home'])
                against_total_home = int(data['goals']['against']['total']['home'])
                try:
                    average_of_total_against_home_goals_by_games_played = against_total_home / games_played_home
                except:
                    average_of_total_against_home_goals_by_games_played = 0
                try:
                    average_of_total_for_home_goals_by_games_played = for_total_home / games_played_home
                except:
                    average_of_total_for_home_goals_by_games_played = 0

                resp = requests.get(
                    f'https://v1.handball.api-sports.io/teams/statistics?season=2023&team={away_team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                    f'https://v1.handball.api-sports.io/teams/statistics?season=2022&team={away_team_id}&league={league_id}&date={date}',
                    headers=headers)
                    pretty_json = json.loads(resp.text)
                data = pretty_json['response']
                games_played_away = int(data['games']['played']['away'])
                for_total_away = int(data['goals']['for']['total']['away'])
                against_total_away = int(data['goals']['against']['total']['away'])
                try:
                    average_of_total_against_away_goals_by_games_played = against_total_away / games_played_away
                except:
                    average_of_total_against_away_goals_by_games_played = 0
                try:
                    average_of_total_for_away_goals_by_games_played = for_total_away / games_played_away
                except:
                    average_of_total_for_away_goals_by_games_played = 0

                print(against_total_away, '/', games_played_away)
                print(for_total_home, '/', games_played_home)
                print(against_total_home, '/', games_played_home)
                print(for_total_away, '/', games_played_away)

                first_column_second_row = []
                second_column_second_row = []
                third_column_second_row = []
                fourth_column_second_row = []

                counter_for_scores = 0
                for team_id in away_home_ids[:5]:
                    final_results_second_row = self.get_additional_columns_data_handball(
                        home_home_goals=away_home_points[counter_for_scores],
                        home_away_goals=away_away_points[counter_for_scores],
                        average_1=average_of_total_against_home_goals_by_games_played,
                        average_2=average_of_total_for_home_goals_by_games_played,
                        away=False, url='https://v1.handball.api-sports.io/teams/statistics',
                        season='2023', team_id=team_id[1], league_id=league_id, date=date)
                    if final_results_second_row == [0,0]:
                        final_results_second_row = self.get_additional_columns_data_handball(
                        home_home_goals=away_home_points[counter_for_scores],
                        home_away_goals=away_away_points[counter_for_scores],
                        average_1=average_of_total_against_home_goals_by_games_played,
                        average_2=average_of_total_for_home_goals_by_games_played,
                        away=False, url='https://v1.handball.api-sports.io/teams/statistics',
                        season='2022', team_id=team_id[1], league_id=league_id, date=date)
                    counter_for_scores += 1

                    print(final_results_second_row)
                    second_column_second_row.append(final_results_second_row[0])
                    third_column_second_row.append(final_results_second_row[1])

                print('---------------------------------------------------------------------')
                counter_for_scores = 0
                for team_id in home_away_ids[:5]:
                    final_results_second_row = self.get_additional_columns_data_handball(
                        home_home_goals=home_away_points[counter_for_scores],
                        home_away_goals=home_home_points[counter_for_scores],
                        average_1=average_of_total_against_away_goals_by_games_played,
                        average_2=average_of_total_for_away_goals_by_games_played,
                        away=True, url='https://v1.handball.api-sports.io/teams/statistics',
                        season='2023', team_id=team_id[1], league_id=league_id, date=date)
                    if final_results_second_row == [0,0]:
                        final_results_second_row = self.get_additional_columns_data_handball(
                        home_home_goals=home_away_points[counter_for_scores],
                        home_away_goals=home_home_points[counter_for_scores],
                        average_1=average_of_total_against_away_goals_by_games_played,
                        average_2=average_of_total_for_away_goals_by_games_played,
                        away=True, url='https://v1.handball.api-sports.io/teams/statistics',
                        season='2022', team_id=team_id[1], league_id=league_id, date=date)

                    counter_for_scores += 1

                    print(final_results_second_row)
                    fourth_column_second_row.append(final_results_second_row[0])
                    first_column_second_row.append(final_results_second_row[1])

                try:
                    first_column_second_row.append(
                        round(sum(first_column_second_row) / len(first_column_second_row), 2))
                except:
                    first_column_second_row.append('None')
                try:
                    second_column_second_row.append(
                        round(sum(second_column_second_row) / len(second_column_second_row), 2))
                except:
                    second_column_second_row.append('None')
                try:
                    third_column_second_row.append(
                        round(sum(third_column_second_row) / len(third_column_second_row), 2))
                except:
                    third_column_second_row.append('None')
                try:
                    fourth_column_second_row.append(
                        round(sum(fourth_column_second_row) / len(fourth_column_second_row), 2))
                except:
                    fourth_column_second_row.append('None')

                print(first_column_second_row)
                print(second_column_second_row)
                print(third_column_second_row)
                print(fourth_column_second_row)

                final_second_row_results = [first_column_second_row, second_column_second_row, third_column_second_row,
                                            fourth_column_second_row]

                print('checking')
                print(away_away_points[-1], 'numerator')
                print(away_home_points[-1], 'denominator')
                print(home_away_points[-1], 'numerator')
                print(home_home_points[-1], 'denominator')
                print('checked')
                a = round(away_home_points[-1] / away_home_points_avg[-1], 2)  # for column 1 and 2
                b = round(home_away_points[-1] / home_away_points_avg[-1], 2)  # for column 5 and 6

                a_final = round(a * home_home_points[-1], 2)  # for column 3 and 4
                b_final = round(b * away_away_points[-1], 2)  # for column 3 and 4
                result = round(a_final + b_final, 2)  # for column 3 and 4

                f_result_1 = a
                f_result_2 = f'{a_final} = {result} = {b_final}'
                f_result_3 = b
                f_result_4 = round(home_home_points[-1] + away_away_points[-1], 2)

                higher_counter = 0
                higher_counter_2 = 0

                for i in range(5):
                    if away_home_points[i] >= away_home_points_avg[i]:
                        higher_counter += 1
                for i in range(5):
                    if home_away_points[i] >= home_away_points_avg[i]:
                        higher_counter_2 += 1

                final_counter = higher_counter + higher_counter_2

                higher_counter_text = f'{higher_counter} / 5'
                higher_counter_2_text = f'{higher_counter_2} / 5'
                final_counter_text = f'{final_counter} / 10'

                final_dict = [{
                    "away_home_points_avg": away_home_points_avg,
                    "away_home_points": away_home_points,
                    "home_home_points": home_home_points,
                    "away_away_points": away_away_points,
                    "home_away_points_avg": home_away_points_avg,
                    "home_away_points": home_away_points,
                    "f_result_1": f_result_1,
                    "f_result_2": f_result_2,
                    "f_result_3": f_result_3,
                    "f_result_4": f_result_4,
                    "higher_counter_text": higher_counter_text,
                    "final_counter_text": final_counter_text,
                    "higher_counter_2_text": higher_counter_2_text,
                    "final_score": final_score,
                    "league_name":league_name,
                    "final_second_row_results":final_second_row_results,
                    "country_name":country_name

                }]

            else:
                final_dict = [{"final_score":final_score,
                               "league_name":league_name,
                               "country_name":country_name}]

            return final_dict

    def get_data(self,index):
        if self.optionmenu_1.get() == 'Select date first':
            tkinter.messagebox.showinfo('Error', 'Please select a date first')
        else:
            
            if index == None:
                index = int(self.optionmenu_1.get().split('.')[0])
            print(self.complete_data)
            try:
                final_data = self.complete_data[index]
            except:
                final_data = self.complete_data[str(index)]
            # print(len(final_data))
            # print(final_data)

            if 'away_home_points_avg' not in final_data[0]:

                final_score = final_data[0]['final_score']
                league_name = final_data[0]['league_name']
                country_name = final_data[0]['country_name']

                self.table.delete(*self.table.get_children())
                self.result_label_1.configure(text='')
                self.result_label_2.configure(text='')
                self.result_label_3.configure(text='')
                self.result_label_4.configure(text='')
                self.result_label_5.configure(text='')
                self.result_label_6.configure(text='')
                self.result_label_7.configure(text='')
                self.final_score.configure(text=final_score)
                self.league_name.configure(text=league_name)
                self.country_name.configure(text=country_name)
                self.result_label_8.configure(text='Not enough data for one of the teams')
                self.result_label_8.place(x=280, y=210)
                # self.result_label.place(x=128, y=300)

            else:
                self.table.delete(*self.table.get_children())

                away_home_points_avg = final_data[0]['away_home_points_avg']
                away_home_points = final_data[0]['away_home_points']
                home_home_points = final_data[0]['home_home_points']
                away_away_points = final_data[0]['away_away_points']
                home_away_points_avg = final_data[0]['home_away_points_avg']
                home_away_points = final_data[0]['home_away_points']
                f_result_1 = final_data[0]['f_result_1']
                f_result_2 = final_data[0]['f_result_2']
                f_result_3 = final_data[0]['f_result_3']
                f_result_4 = final_data[0]['f_result_4']
                higher_counter_text = final_data[0]['higher_counter_text']
                final_counter_text = final_data[0]['final_counter_text']
                higher_counter_2_text = final_data[0]['higher_counter_2_text']
                final_score = final_data[0]['final_score']
                league_name = final_data[0]['league_name']
                country_name = final_data[0]['country_name']
                final_second_row_results = final_data[0]['final_second_row_results']

                indexer = 1
                for i in range(6):
                    self.table.insert("", 'end', text="L" + str(indexer),
                                      values=(away_home_points_avg[i], away_home_points[i],
                                              home_home_points[i], away_away_points[i],
                                              home_away_points_avg[i], home_away_points[i]), tags='TkTextFont')
                    indexer += 1

                for i in range(4):
                    self.table.insert("", 'end', text="L" + str(indexer),
                                      values=('', '', '', '', '', ''), tags='TkTextFont')
                    indexer += 1

                for i in range(5):
                    self.table.insert("", 'end', text="L" + str(indexer),
                                      values=(final_second_row_results[0][i], final_second_row_results[1][i], '', '',
                                              final_second_row_results[2][i], final_second_row_results[3][i]),
                                      tags='TkTextFont')
                    indexer += 1

                self.table.insert("", 'end', text="L" + str(indexer),
                                  values=(final_second_row_results[0][-1], final_second_row_results[1][-1], '', '',
                                          final_second_row_results[2][-1], final_second_row_results[3][-1]),
                                  tags='average_color_change')


                # print(away_home_points_avg)
                # print(away_home_points)
                # print(home_home_points)
                # print(away_away_points)
                # print(home_away_points_avg)
                # print(home_away_points)

                if int(higher_counter_text.split('/')[0]) >= 4:
                    fg_color_left = '#22AA49'
                elif int(higher_counter_text.split('/')[0]) <= 1:
                    fg_color_left = '#CE2027'
                else:
                    fg_color_left = 'white'

                if int(higher_counter_2_text.split('/')[0]) >= 4:
                    fg_color_right = '#22AA49'
                elif int(higher_counter_2_text.split('/')[0]) <= 1:
                    fg_color_right = '#CE2027'
                else:
                    fg_color_right = 'white'

                if int(final_counter_text.split('/')[0]) >= 8:
                    fg_color_middle = '#22AA49'
                elif int(final_counter_text.split('/')[0]) <= 2:
                    fg_color_middle = '#CE2027'
                elif int(final_counter_text.split('/')[0]) <= 7 and int(final_counter_text.split('/')[0]) >= 5:
                    fg_color_middle = '#01a1e8'
                else:
                    fg_color_middle = 'white'

                self.result_label_1.configure(text=f_result_1)
                self.result_label_2.configure(text=f_result_2)
                self.result_label_3.configure(text=f_result_3)
                self.result_label_4.configure(text=f_result_4)
                self.result_label_5.configure(text=higher_counter_text, text_color=fg_color_left)
                self.result_label_6.configure(text=final_counter_text, text_color=fg_color_middle)
                self.result_label_7.configure(text=higher_counter_2_text, text_color=fg_color_right)
                self.final_score.configure(text=final_score)
                self.league_name.configure(text=league_name)
                self.country_name.configure(text=country_name)
                self.result_label_8.place_forget()

####### ------------------------------------ Single Frame ------------------------------------ ########
class Single_load_App(customtkinter.CTk):
    COUNT = 0

    def __init__(self):
        super().__init__()

        style = ttk.Style()

        style.theme_use("default")

        style.configure("Treeview",
                        background="#343638",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#F3F1E9",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        font=(None, 17))
        style.map("Treeview.Heading",
                  background=[('active', '#3484F0')])

        self.on_closing = None
        self.var = customtkinter.StringVar(self)
        self.title("ClassApp")

        self.geometry(f"1330x880")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # self.complete_data = {}
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=200,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self, width=1000)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=100, pady=15)

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.add_menu_display211 = customtkinter.CTkFrame(master=self.frame_right,
                                                          corner_radius=15,
                                                          height=400,
                                                          width=10)
        self.add_menu_display211.grid(pady=15, padx=15, sticky="nws")

        columns = ('column_1', 'column_2', 'column_3', 'column_4','column_5','column_6')

        self.table = ttk.Treeview(master=self.add_menu_display211,
                                  columns=columns,
                                  height=20,
                                  selectmode='browse',
                                  show='headings')

        self.table.column("#1", anchor="c", width=150)
        self.table.column("#2", anchor="c",  width=150)
        self.table.column("#3", anchor="c",  width=150)
        self.table.column("#4", anchor="c",  width=150)
        self.table.column("#5", anchor="c",  width=150)
        self.table.column("#6", anchor="c",  width=150)

        self.table.heading('column_1', text='Column 1')
        self.table.heading('column_2', text='Column 2')
        self.table.heading('column_3', text='Column 3')
        self.table.heading('column_4', text='Column 4')
        self.table.heading('column_5', text='Column 5')
        self.table.heading('column_6', text='Column 6')

        self.table.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.table.bind('<Motion>', 'break')

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Menu",
                                              font=("Roboto Medium", -16))
        self.label_1.grid(row=1, column=0, pady=20, padx=10)

        self.result_label_1 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638')
        self.result_label_1.place(x=110, y=300)

        self.result_label_2 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638')
        self.result_label_2.place(x=350, y=350)

        self.result_label_3 = customtkinter.CTkLabel(master=self.frame_right,
                                                     text='',
                                                     font=("Roboto Medium", -25),
                                                     bg_color='#343638')
        self.result_label_3.place(x=710, y=300)

        self.result_label_4 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638')
        self.result_label_4.place(x=400, y=300)

        self.result_label_5 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638',)
        self.result_label_5.place(x=110, y=400)

        self.result_label_6 = customtkinter.CTkLabel(master=self.frame_right,
                                                     text='',
                                                     font=("Roboto Medium", -25),
                                                     bg_color='#343638')
        self.result_label_6.place(x=400, y=400)

        self.result_label_7 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638')
        self.result_label_7.place(x=710, y=400)

        self.result_label_8 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text='',
                                                   font=("Roboto Medium", -25),
                                                   bg_color='#343638')
        self.result_label_8.place(x=280, y=210)


        def get_teams(date):

            # left_1 = 0
            # left_2 = 0
            # right_1 = 0
            # right_2 = 0
            #

            params = {
                'date': date,
            }

            # print(date)
            if self.optionmenu_0.get() == 'Basketball':
                url = 'https://v1.basketball.api-sports.io/games'
            elif self.optionmenu_0.get() == 'Handball':
                url = 'https://v1.handball.api-sports.io/games'

            response = requests.get(f'{url}', params=params, headers=headers)

            if str(response.status_code) == "200":
                self.optionmenu_1.configure(state='read')

                global new_values_for_combobox
                new_values_for_combobox = []

                # global team_id_dict
                # team_id_dict = {}
                # global
                self.complete_data = {}
                count = 1
                pretty_json = json.loads(response.text)
                total_len = pretty_json['results']
                nba_g_league_count = 0
                for team_data in pretty_json['response']:
                    if team_data['league']['name'] == "NBA - G League":
                        nba_g_league_count+=1
                total_len = total_len - nba_g_league_count

                self.games_counter.configure(text=f'0 / {total_len}')
                self.update()
                for home_away in pretty_json['response']:
                    if home_away['league']['name'] != "NBA - G League":
                        home = home_away['teams']['home']['name']
                        home_id = home_away['teams']['home']['id']

                        away = home_away['teams']['away']['name']
                        away_id = home_away['teams']['away']['id']

                        league_id = home_away['league']['id']
                        league_name = home_away['league']['name']
                        country_name = home_away['country']['name']

                        match_time = home_away['time']
                        match_time = self.add_two_hours(match_time)
                        
                        # league_name = home_away['league']['name']
                        # league_season = home_away['league']['season']

                        # print(f'Home Team --> Name: {home},  id: {home_id}')
                        # print(f'Away Team --> Name: {away},  id: {away_id}')
                        # print(f'League ID: {league_id}, League Name: {league_name}, Season: {league_season}')
                        # print('\n\n')

                        # match = '{:20s} vs {:20s}    {}'.format(home,away,match_time)
                        match = f'{home} vs {away}'

                        # calc = 100-len_match
                        match_2 = f"{count:02d}.      {match_time}            {match}"
                        print(match_2)
                        if match_2 not in new_values_for_combobox:
                            new_values_for_combobox.append(match_2)
                        print('this is count: ',count)

                        if self.optionmenu_0.get() == 'Basketball':
                            final_score = ''
                            if home_away['scores']['home']['total'] != None and home_away['scores']['away']['total'] != None:
                                final_score = f"{home_away['scores']['home']['total']} : {home_away['scores']['away']['total']}"
                        elif self.optionmenu_0.get() == 'Handball':
                            final_score = ''
                            if home_away['scores']['home'] != None and home_away['scores']['away'] != None:
                                final_score = f"{home_away['scores']['home']} : {home_away['scores']['away']}"

                        self.complete_data[count] = [date,home_id, away_id, league_id, final_score, league_name, country_name]
                        # print(self.complete_data[count][0])
                        print('this is final score ',final_score)
                        # if 'away_home_points_avg' in self.complete_data[count][0] and final_score != '':
                        #     print('new hehe')
                        #     total_score = final_score.split(':')
                        #     total_score = int(total_score[0]) + int(total_score[1])
                        #     above_text = float(self.complete_data[count][0]['f_result_4'])
                        #     lower_text = int(self.complete_data[count][0]['final_counter_text'].split('/')[0])
                        #     if lower_text >= 8:
                        #         if total_score > above_text:
                        #             left_1+=1
                        #         else:
                        #             left_2+=1
                        #     elif lower_text <= 2:
                        #         if total_score > above_text:
                        #             right_1+=1
                        #         else:
                        #             right_2+=1
                        #     print('left ',left_1)
                        #     print(left_2)
                        #     print(right_1)
                        #     print(right_2)
                        self.games_counter.configure(text=f'{count} / {total_len}')
                        # time.sleep(2)
                        self.update()

                        count+=1
                # self.different_counters_left.configure(text=f'{left_1} / {left_2}')
                # self.different_counters_right.configure(text=f'{right_1} / {right_2}')

                self.optionmenu_1.configure(values=new_values_for_combobox)
                self.optionmenu_1.set(new_values_for_combobox[0])

            else:
                tkinter.messagebox.showerror('Error', 'An error occurred, please try again!')

        def date_date_picker():
            today = datetime.date.today()

            def date_select():
                self.button_1.configure(text=f'{date_date.selection_get()}')
                top.destroy()

                global now_date
                now_date = date_date.selection_get()
                get_teams(date_date.selection_get())

            top = customtkinter.CTkToplevel(self.frame_left)
            top.geometry('800x500')
            top.title("Select Date")
            top.attributes("-topmost", True)
            global date_date
            date_date = Calendar(top,
                                 font="Arial 14", selectmode='day',
                                 cursor="hand2", year=today.year, month=today.month, day=today.day)
            date_date.pack(fill="both", expand=True,padx=40)
            customtkinter.CTkButton(top, text="Select Date", font=("Helvetica", 14), command=date_select).pack(pady=20)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Select Date",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=date_date_picker,
                                                cursor='hand2')
        self.button_1.grid(row=2, column=0, pady=(15, 15), padx=20)

        # self.button_2 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Delete Item",
        #                                         corner_radius=15,
        #                                         border_width=1.5,
        #                                         border_color="#3484F0",  # alternative red: #f03933
        #                                         fg_color="#343638",
        #                                         cursor='hand2',
        #                                         command=None)
        # self.button_2.grid(row=3, column=0, pady=15, padx=20)
        #
        # self.button_3 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Edit Item",
        #                                         corner_radius=15,
        #                                         border_width=1.5,
        #                                         border_color="#3484F0",
        #                                         fg_color="#343638",
        #                                         cursor='hand2',
        #                                         command=None)
        # self.button_3.grid(row=4, column=0, pady=15, padx=20)

        self.optionmenu_0_values = ['Basketball','Handball']
        self.optionmenu_0 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=self.optionmenu_0_values,
                                                        corner_radius=15,
                                                        button_color="#565b5e",
                                                        fg_color="#343638",
                                                        button_hover_color="#3484F0",
                                                        command=None,
                                                        height=20)
        self.optionmenu_0.grid(row=3, column=0, pady=(15, 25), padx=20)
        self.optionmenu_0.set(self.optionmenu_0_values[0])

        self.home_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='',
                                                 font=("Roboto Medium", -14))
        self.home_label.grid(row=6, column=0, pady=(20, 0), padx=10)

        self.vs_label = customtkinter.CTkLabel(master=self.frame_left,
                                               text='',
                                               font=("Roboto Medium", -14))
        self.vs_label.grid(row=7, column=0, pady=(5,5), padx=10)

        self.away_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='',
                                                 font=("Roboto Medium", -14))
        self.away_label.grid(row=8, column=0, padx=10,pady=(0,20))

        self.games_counter = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='0 / 0',
                                                 font=("Roboto Medium", -18))
        self.games_counter.grid(row=9, column=0, padx=10,pady=(25,0))

        self.league_name = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='',
                                                 font=("Roboto Medium", -14))
        self.league_name.grid(row=10, column=0, padx=10,pady=(20,0))

        self.country_name = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='',
                                                 font=("Roboto Medium", -14))
        self.country_name.grid(row=11, column=0, padx=10,pady=(20,0))

        self.different_counters_left = customtkinter.CTkLabel(master=self.frame_left,text='',width=0,
                                                   font=("Roboto Medium", 1))
        self.different_counters_left.grid(row=12, column=0)

        self.different_counters_left = customtkinter.CTkLabel(master=self.frame_left,
                                                   text='0 / 0',
                                                   font=("Roboto Medium", 11),text_color='#22AA49')
        self.different_counters_left.place(x=50,y=592)

        self.different_counters_right = customtkinter.CTkLabel(master=self.frame_left,
                                                   text='0 / 0',
                                                   font=("Roboto Medium", 11),text_color='#CE2027')
        self.different_counters_right.place(x=100,y=592)

        self.get_data_btn = customtkinter.CTkButton(master=self.frame_left,
                                                text="Get Data",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=lambda : self.get_data(index=None),
                                                cursor='hand2')
        self.get_data_btn.grid(row=13, column=0, pady=(30, 0), padx=20)
        
        self.copy_btn = customtkinter.CTkButton(master=self.frame_left,
                                                text="Copy",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=lambda : self.copy(),
                                                cursor='hand2')
        self.copy_btn.grid(row=14, column=0, pady=(20, 20), padx=20)

        def home_away_labels(event):
            self.home_label.configure(text=self.optionmenu_1.get().split('vs')[0].strip(' ').split('            ')[1].strip(' '))
            self.vs_label.configure(text='vs')
            self.away_label.configure(text=self.optionmenu_1.get().split('vs')[1].strip(' '))

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        corner_radius=15,
                                                        button_color="#565b5e",
                                                        fg_color="#343638",
                                                        button_hover_color="#3484F0",
                                                        command=home_away_labels,
                                                        height=20,
                                                        dynamic_resizing=False,
                                                        dropdown_hover_color='#3484F0')
        self.optionmenu_1.grid(row=4, column=0, pady=(15, 15), padx=20)
        self.optionmenu_1.set("Select date first")
        self.optionmenu_1.configure(state='disabled')

        self.final_score = customtkinter.CTkLabel(master=self.frame_left,
                                                 text='',
                                                 font=("Roboto Medium", -17))
        self.final_score.grid(row=5, column=0, pady=(15, 15), padx=20)
        # self.optionmenu_1.bind("<Configure>", home_away_labels)
        # self.optionmenu_1.bind("<<OptionSelected>>", home_away_labels)

        # ============ frame_right ============

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        font = tkfont.nametofont('TkTextFont')
        self.table.tag_configure('TkTextFont', font=tkfont.nametofont('TkTextFont'))
        self.table.tag_configure('average_color_change', foreground="#FF7F2A",font=tkfont.nametofont('TkTextFont'))
        style.configure('Treeview', rowheight=font.metrics('linespace'))

        _font = tkfont.nametofont('TkTextFont')
        _font.configure(size=21)
        style.configure('Treeview', rowheight=_font.metrics('linespace'))

        def selection_remove(selection):
            self.table.selection_remove(self.table.focus())
            print("Deselected item")

        def change_values_option_menu_down(event):
            # self.optionmenu_1.set(self.temp_data_optionmenu[1])
            # print(new_values_for_combobox)
            index = int(self.optionmenu_1.get().split('.')[0]) - 1
            index += 1
            index = index % len(new_values_for_combobox)
            self.optionmenu_1.set(new_values_for_combobox[index])
            home_away_labels(event=None)

            updated_index = int(self.optionmenu_1.get().split('.')[0])
            self.get_data(index=updated_index)

        def change_values_option_menu_up(event):
            # self.optionmenu_1.set(self.temp_data_optionmenu[1])
            # print(new_values_for_combobox)
            index = int(self.optionmenu_1.get().split('.')[0]) - 1
            index -= 1
            self.optionmenu_1.set(new_values_for_combobox[index])
            home_away_labels(event=None)

            updated_index = int(self.optionmenu_1.get().split('.')[0])
            self.get_data(index=updated_index)


        self.table.bind("<Escape>", selection_remove)
        # self.bind('<Up>',change_values_option_menu_up)
        # self.bind('<Down>',change_values_option_menu_down)

        self.mainloop()

    def add_two_hours(self,time_string):
        # Convert string to datetime object
        time_format = "%H:%M"
        time = datetime.datetime.strptime(time_string, time_format)

        # Add 2 hours to the datetime object
        time += datetime.timedelta(hours=2)

        # Convert back to string
        new_time_string = time.strftime(time_format)
        return new_time_string

    def copy(self):
        home_away_team_text = f"{self.home_label.cget('text')} vs {self.away_label.cget('text')}"
        self.clipboard_append(home_away_team_text)

    def find(self,lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -1


    def get_additional_columns_data(self,home_home_points,home_away_points,average_1,average_2,url,season,team_id,league_id,date,away=False):
        if away == False:
            print(team_id, league_id,date)
            resp = requests.get(
                f'{url}?season={season}&team={team_id}&league={league_id}&date={date}',
                headers=headers)
            pretty_json = json.loads(resp.text)
            data = pretty_json['response']
            if data['country']['id'] == None:
                resp = requests.get(
                    f'{url}?season={season.split("-")[0]}&team={team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                data = pretty_json['response']
            print(data)
            total_home_played = int(data['games']['played']['home'])
            for_home = int(data['points']['for']['total']['home'])
            try:
                average_by_for_home = round(for_home / total_home_played, 2)
            except:
                average_by_for_home = 0
            try:
                calc_final_second_col = round((home_home_points * average_2) / average_by_for_home, 2)
            except:
                calc_final_second_col = 0
                # print(f'total home played: {total_home_played}, total points in home: {for_home}')
                # print(f"({home_home_points} x {average_2}) / {average_by_for_home} = {calc_final_second_col}")

            total_home_played = int(data['games']['played']['home'])
            against_home = int(data['points']['against']['total']['home'])
            try:
                average_by_against_home = round(against_home / total_home_played, 2)
            except:
                average_by_against_home = 0
            try:
                calc_final_third_col = round((home_away_points * average_1) / average_by_against_home, 2)
            except:
                calc_final_third_col = 0

            # print(f'total against home played: {total_home_played}, total against points in home: {against_home}')
            # print(f"({home_away_points} x {average_1}) / {average_by_against_home} = {calc_final_third_col}")

            return [calc_final_second_col, calc_final_third_col]

        elif away == True:

            # print(team_id, league_id)
            resp = requests.get(
                f'{url}?season={season}&team={team_id}&league={league_id}&date={date}',
                headers=headers)
            pretty_json = json.loads(resp.text)
            data = pretty_json['response']
            if data['country']['id'] == None:
                resp = requests.get(
                    f'{url}?season={season.split("-")[0]}&team={team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                data = pretty_json['response']
            total_home_played = int(data['games']['played']['away'])
            for_home = int(data['points']['for']['total']['away'])
            try:
                average_by_for_home = round(for_home / total_home_played, 2)
            except:
                average_by_for_home = 0
            try:
                calc_final_first_col = round((home_home_points * average_2) / average_by_for_home, 2)
            except:
                calc_final_first_col = 0
            # print(f'total away played: {total_home_played}, total points in away: {for_home}')
            # print(f"({home_home_points} x {average_2}) / {average_by_for_home} = {calc_final_first_col}")

            total_home_played = int(data['games']['played']['away'])
            against_home = int(data['points']['against']['total']['away'])
            try:
                average_by_against_home = round(against_home / total_home_played, 2)
            except:
                average_by_against_home = 0
            try:
                calc_final_fourth_col = round((home_away_points * average_1) / average_by_against_home, 2)
            except:
                calc_final_fourth_col = 0

            # print(f'total against away played: {total_home_played}, total against points in away: {against_home}')
            # print(f"({home_away_points} x {average_1}) / {average_by_against_home} = {calc_final_fourth_col}")

            return [calc_final_first_col,calc_final_fourth_col]

    def get_additional_columns_data_handball(self,home_home_goals,home_away_goals,average_1,average_2,url,season,team_id,league_id,date,away=False):
        if away == False:
            # print(team_id, league_id)
            resp = requests.get(
                f'{url}?season={season}&team={team_id}&league={league_id}&date={date}',
                headers=headers)
            pretty_json = json.loads(resp.text)
            data = pretty_json['response']
            if data['country']['id'] == None:
                resp = requests.get(
                    f'{url}?season={season.split("-")[0]}&team={team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                data = pretty_json['response']
            total_home_played = int(data['games']['played']['home'])
            for_home = int(data['goals']['for']['total']['home'])
            try:
                average_by_for_home = round(for_home / total_home_played, 2)
            except:
                average_by_for_home = 0
            try:
                calc_final_second_col = round((home_home_goals * average_2) / average_by_for_home, 2)
            except:
                calc_final_second_col = 0
            # print(f'total home played: {total_home_played}, total goals in home: {for_home}')
            # print(f"({home_home_goals} x {average_2}) / {average_by_for_home} = {calc_final_second_col}")

            total_home_played = int(data['games']['played']['home'])
            against_home = int(data['goals']['against']['total']['home'])
            try:
                average_by_against_home = round(against_home / total_home_played, 2)
            except:
                average_by_against_home = 0
            try:
                calc_final_third_col = round((home_away_goals * average_1) / average_by_against_home, 2)
            except:
                calc_final_third_col = 0

            # print(f'total against home played: {total_home_played}, total against goals in home: {against_home}')
            # print(f"({home_away_goals} x {average_1}) / {average_by_against_home} = {calc_final_third_col}")

            return [calc_final_second_col, calc_final_third_col]

        elif away == True:

            # print(team_id, league_id)
            resp = requests.get(
                f'{url}?season={season}&team={team_id}&league={league_id}&date={date}',
                headers=headers)
            pretty_json = json.loads(resp.text)
            data = pretty_json['response']
            if data['country']['id'] == None:
                resp = requests.get(
                    f'{url}?season={season.split("-")[0]}&team={team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                data = pretty_json['response']
            total_home_played = int(data['games']['played']['away'])
            for_home = int(data['goals']['for']['total']['away'])
            try:
                average_by_for_home = round(for_home / total_home_played, 2)
            except:
                average_by_for_home = 0
            try:
                calc_final_first_col = round((home_home_goals * average_2) / average_by_for_home, 2)
            except:
                calc_final_first_col = 0
            # print(f'total away played: {total_home_played}, total goals in away: {for_home}')
            # print(f"({home_home_goals} x {average_2}) / {average_by_for_home} = {calc_final_first_col}")

            total_home_played = int(data['games']['played']['away'])
            against_home = int(data['goals']['against']['total']['away'])
            try:
                average_by_against_home = round(against_home / total_home_played, 2)
            except:
                average_by_against_home = 0
            try:
                calc_final_fourth_col = round((home_away_goals * average_1) / average_by_against_home, 2)
            except:
                calc_final_fourth_col = 0

            # print(f'total against away played: {total_home_played}, total against goals in away: {against_home}')
            # print(f"({home_away_goals} x {average_1}) / {average_by_against_home} = {calc_final_fourth_col}")

            return [calc_final_first_col,calc_final_fourth_col]


    def get_away_home_ids(self, url, away_home_ids, league_id):
        away_home_points_avg = []

        for id in away_home_ids:
            if len(away_home_points_avg) == 5:
                break
            print(
                f'------------------------------------------------------------------------------------------------------------{id[2]}------------------------------------------------------------------------------------------------------------')
            counter = 0
            found_in_first_season = False
            points = 0

            for season in seasons:
                resp = requests.get(
                    f'{url}?season={season}&team={id[1]}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={id[1]}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # count = False

                # print(pretty_json['response'].index())
                # index_value = next((index for (index, d) in enumerate(pretty_json['response']) if d["id"] == str(id[0])), None)
                # print(index_value)

                main_lst = pretty_json['response']
                # print(json.dumps(pretty_json,indent=3))
                main_lst.reverse()
                index_value = self.find(main_lst, 'id', id[0])

                if index_value != -1:
                    found_in_first_season = True

                if counter >= 5:
                    break
                else:
                    if found_in_first_season == True:
                        # print('This is index value ',index_value)
                        # print('Finding match ID: ', id[0])
                        for i in main_lst[index_value + 1:]:
                            # print(i)
                            if str(i['teams']['home']['id']) == str(id[1]) and i['scores']['home']['total'] != None:
                                if (str(i['scores']['home']['total']) != '20' and str(i['scores']['home']['total']) != '0') or (str(i['scores']['away']['total']) != '20' and str(i['scores']['away']['total']) != '0'):

                                    if i['scores']['home']['over_time'] != None:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(i['id']) + '    ' + str(i['scores']['home']['total']-i['scores']['home']['over_time']) + ' vs ' + str(i['scores']['away']['total']-i['scores']['away']['over_time']) + ' season: ' + season)
                                    else:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(i['id']) + '    ' + str(i['scores']['home']['total']) + ' vs ' + str(i['scores']['away']['total']) + ' season: ' + season)

                                    # print(i['id'])
                                    points += i['scores']['home']['total']
                                    if i['scores']['home']['over_time'] != None:
                                        points -= i['scores']['home']['over_time']

                                    counter += 1

                            if counter == 5:
                                break

                    # for i in  pretty_json['response']:
                    #     if str(i['id']) == str(id[0]):

                found_in_first_season = True
            print('Total points ', points)
            if counter == 0 or counter == 1:
                points = 0
            else:
                points = round(points / counter, 2)
            print(f'points {points} for team {id[2]} counter {counter}')
            away_home_points_avg.append(points)
        return away_home_points_avg

    def get_home_away_ids(self, url, home_away_ids, league_id):

        home_away_points_avg = []

        for id in home_away_ids:
            if len(home_away_points_avg) == 5:
                break
            print(f'------------------------------------------------------------------------------------------------------------{id[2]}------------------------------------------------------------------------------------------------------------')
            counter = 0
            found_in_first_season = False
            points = 0
            for season in seasons:
                resp = requests.get(
                    f'{url}?season={season}&team={id[1]}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={id[1]}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # count = False

                # print(pretty_json['response'].index())
                # index_value = next((index for (index, d) in enumerate(pretty_json['response']) if d["id"] == str(id[0])), None)
                # print(index_value)
                main_lst = pretty_json['response']
                # print(json.dumps(pretty_json,indent=3))
                main_lst.reverse()
                index_value = self.find(main_lst, 'id', id[0])
                print('length of list ',len(main_lst))
                if index_value != -1:
                    found_in_first_season = True

                if counter >= 5:
                    break
                else:
                    if found_in_first_season == True:
                        print('This is index value ',index_value)
                        print('Finding match ID: ',id[0])
                        for i in main_lst[index_value + 1:]:
                            # print(i)
                            if str(i['teams']['away']['id']) == str(id[1]) and i['scores']['away']['total'] != None:
                                if (str(i['scores']['home']['total']) != '20' and str(i['scores']['home']['total']) != '0') or (str(i['scores']['away']['total']) != '20' and str(i['scores']['away']['total']) != '0'):

                                    if i['scores']['home']['over_time'] != None and (i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(
                                            i['scores']['home']['total'] - i['scores']['home']['over_time']) + ' vs ' + str(
                                            i['scores']['away']['total'] - i['scores']['away'][
                                                'over_time']) + ' season: ' + season)
                                    else:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(i['scores']['home']['total']) + ' vs ' + str(
                                            i['scores']['away']['total']) + ' season: ' + season)

                                    points += i['scores']['away']['total']
                                    if i['scores']['away']['over_time'] != None:
                                        points -= i['scores']['away']['over_time']
                                    counter += 1

                            if counter == 5:
                                break

                    # for i in  pretty_json['response']:
                    #     if str(i['id']) == str(id[0]):

                found_in_first_season = True
            print('Total points ', points)
            if counter == 0 or counter == 1:
                points = 0
            else:
                points = round(points / counter, 2)
            print(f'points {points} for team {id[2]} counter {counter}')
            print(f'points {points} for team {id[2]}')

            home_away_points_avg.append(points)

        return home_away_points_avg

    def get_away_home_ids_handball(self, url, away_home_ids, league_id):
        seasons = ['2023-2024','2022-2023', '2021-2022']
        print(away_home_ids)
        away_home_points_avg = []
        for id in away_home_ids:
            if len(away_home_points_avg) == 5:
                break
            print(f'------------------------------------------------------------------------------------------------------------{id[2]}------------------------------------------------------------------------------------------------------------')
            counter = 0
            found_in_first_season = False
            points = 0
            for season in seasons:
                resp = requests.get(
                    f'{url}?season={season}&team={id[1]}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={id[1]}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # count = False

                # print(pretty_json['response'].index())
                # index_value = next((index for (index, d) in enumerate(pretty_json['response']) if d["id"] == str(id[0])), None)
                # print(index_value)
                main_lst = pretty_json['response']
                # print(json.dumps(pretty_json,indent=3))
                main_lst.reverse()
                index_value = self.find(main_lst, 'id', id[0])

                if index_value != -1:
                    found_in_first_season = True

                if counter >= 5:
                    break
                else:
                    if found_in_first_season == True:
                        # print('This is index value ',index_value)
                        # print('Finding match ID: ',id[0])
                        for i in main_lst[index_value + 1:]:
                            # print(i)
                            if str(i['teams']['home']['id']) == str(id[1]) and i['scores']['home'] != None:
                                if (i['scores']['home'] != 10 and i['scores']['away'] != 0) or (
                                        i['scores']['away'] != 10 and i['scores']['home'] != 0):

                                    print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                        i['id']) + '    ' + str(i['scores']['home']) + ' vs ' + str(
                                        i['scores']['away']) + ' season: ' + season)
                                    points += i['scores']['home']
                                    counter += 1

                            if counter == 5:
                                break

                    # for i in  pretty_json['response']:
                    #     if str(i['id']) == str(id[0]):

                found_in_first_season = True
            print('Total points ', points)
            if counter == 0 or counter == 1:
                points = 0
            else:
                points = round(points / counter, 2)
            print(f'points {points} for team {id[2]} counter {counter}')
            away_home_points_avg.append(points)
            print(f'points {points} for team {id[2]}')

        return away_home_points_avg

    def get_home_away_ids_handball(self, url, home_away_ids, league_id):
        seasons = ['2023-2024','2022-2023', '2021-2022']

        print(home_away_ids)
        home_away_points_avg = []
        for id in home_away_ids:
            if len(home_away_points_avg) == 5:
                break
            print(f'------------------------------------------------------------------------------------------------------------{id[2]}------------------------------------------------------------------------------------------------------------')
            counter = 0
            found_in_first_season = False
            points = 0
            for season in seasons:
                resp = requests.get(
                    f'{url}?season={season}&team={id[1]}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                # count = False

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={id[1]}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # print(pretty_json['response'].index())
                # index_value = next((index for (index, d) in enumerate(pretty_json['response']) if d["id"] == str(id[0])), None)
                # print(index_value)
                main_lst = pretty_json['response']
                # print(json.dumps(pretty_json,indent=3))
                main_lst.reverse()
                index_value = self.find(main_lst, 'id', id[0])

                if index_value != -1:
                    found_in_first_season = True

                if counter >= 5:
                    break
                else:
                    if found_in_first_season == True:
                        # print('This is index value ', index_value)
                        # print('Finding match ID: ', id[0])
                        for i in main_lst[index_value + 1:]:
                            # print(i)
                            if str(i['teams']['away']['id']) == str(id[1]) and i['scores']['away'] != None:
                                if (i['scores']['home'] != 10 and i['scores']['away'] != 0) or (
                                        i['scores']['away'] != 10 and i['scores']['home'] != 0):

                                    print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                        i['id']) + '    ' + str(i['scores']['home']) + ' vs ' + str(
                                        i['scores']['away']) + ' season: ' + season)
                                    # print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                    #     i['id']) + '    ' + str(i['scores']['home']['total']) + ' vs ' + str(
                                    #     i['scores']['away']['total']) + ' season: ' + season)
                                    points += i['scores']['away']
                                    counter += 1

                            if counter == 5:
                                break

                    # for i in  pretty_json['response']:
                    #     if str(i['id']) == str(id[0]):

                found_in_first_season = True
            if counter == 0 or counter == 1:
                points = 0
            else:
                points = round(points / counter, 2)
            print(f'points {points} for team {id[2]} counter {counter}')
            home_away_points_avg.append(points)

        return home_away_points_avg

    def get_teams_data_advance(self,date,home_team_id,away_team_id,league_id,final_score,league_name, country_name):

        if self.optionmenu_0.get() == 'Basketball':
            seasons = ['2023-2024','2022-2023', '2021-2022']

            url = 'https://v1.basketball.api-sports.io/games'

            # home = self.optionmenu_1.get().split('vs')[0].strip(' ').split('            ')[1].strip(' ')
            # away = self.optionmenu_1.get().split('vs')[1].strip(' ')

            # print(home)
            # print(away)

            # home_team_id, away_team_id, league_id = team_id_dict[self.optionmenu_1.get()][0], \
            #                                         team_id_dict[self.optionmenu_1.get()][1], \
            #                                         team_id_dict[self.optionmenu_1.get()][2]

            home_home_points = []
            home_away_points = []

            away_home_points = []
            away_away_points = []

            # home_away_points_avg = []

            home_away_ids = []
            away_home_ids = []

            can_be_done = False
            for season in seasons:
                #  fetching data for "home" home team

                temp_lst_1 = []
                temp_lst_2 = []
                resp = requests.get(
                    f'{url}?season={season}&team={home_team_id}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) > 0:
                    can_be_done = True
                if can_be_done == False:
                    if len(pretty_json['response']) == 0:

                        season = season.split('-')[0]
                        resp = requests.get(
                            f'{url}?season={season}&team={home_team_id}&league={league_id}',
                            headers=headers)
                        pretty_json = json.loads(resp.text)

                print('this is link ' + f'{url}?season={season}&team={home_team_id}&league={league_id}')
                print('this is status ',resp.status_code)
                print(pretty_json['response'])
                # date_index_counter = 0
                # for temp_date in pretty_json['response']:
                #     raw_date = temp_date['date'].split('T')[0]
                #     # if raw_date < str(date):
                #     print(raw_date)
                        # break
                # print(pretty_json)
                temp_lst_6 = []
                for i in pretty_json['response']:
                    if i['date'].split('T')[0] < str(date):
                        print(i['date'].split('T')[0])
                        if str(i['teams']['home']['id']) == str(home_team_id):
                            if (str(i['scores']['home']['total']) != '20' and str(
                                    i['scores']['home']['total']) != '0') or (
                                    str(i['scores']['away']['total']) != '20' and str(
                                    i['scores']['away']['total']) != '0'):
                                if i['scores']['home']['total'] != None and (
                                        i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                    total = i['scores']['home']['total']
                                    if i['scores']['home']['over_time'] != None:
                                        total -= i['scores']['home']['over_time']
                                    temp_lst_1.append(total)

                                    if i['scores']['home']['over_time'] != None:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(
                                            i['scores']['home']['total'] - i['scores']['home']['over_time']) + ' vs ' + str(
                                            i['scores']['away']['total'] - i['scores']['away'][
                                                'over_time']) + ' season: ' + season)
                                    else:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(i['scores']['home']['total']) + ' vs ' + str(
                                            i['scores']['away']['total']) + ' season: ' + season)
                                    # temp_lst_3.append(i['scores']['home']['total'] - i['scores']['home']['over_time'])

                                    match_id = i['id']
                                    away_team_here_id = i['teams']['away']['id']
                                    # print(i['teams']['home']['name'])
                                    temp_lst_6.append(
                                        [match_id, away_team_here_id, i['teams']['away']['name'], i['league']['season']])

                                if i['scores']['away']['total'] != None and (
                                        i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                    total = i['scores']['away']['total']
                                    if i['scores']['away']['over_time'] != None:
                                        total -= i['scores']['away']['over_time']
                                    temp_lst_2.append(total)

                temp_lst_6.reverse()
                # print(temp_lst_6)
                for z in temp_lst_6:
                    home_away_ids.append(z)

                temp_lst_1.reverse()
                temp_lst_2.reverse()

                for i in temp_lst_1:
                    home_home_points.append(i)
                    # print(i)

                for i in temp_lst_2:
                    home_away_points.append(i)
                    # print(i)

                #  fetching data for "home" away team

                # temp_lst = []
                # resp = requests.get(f'https://v1.basketball.api-sports.io/games?season={season}&team={home_team_id}', headers=headers)
                # pretty_json = json.loads(resp.text)
                # print(pretty_json)
                # for i in pretty_json['response']:
                #     if str(i['teams']['home']['id']) == str(home_team_id):
                #         if i['scores']['away']['total'] != None:
                #             temp_lst.append(i['scores']['away']['total'])
                # temp_lst.reverse()
                # for i in temp_lst:
                #     home_away_points.append(i)
                #     # print(i)

                temp_lst_3 = []
                temp_lst_4 = []
                resp = requests.get(
                    f'{url}?season={season}&team={away_team_id}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={away_team_id}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # print(pretty_json)

                temp_lst_5 = []
                for i in pretty_json['response']:
                    if i['date'].split('T')[0] < str(date):
                        print(i['date'].split('T')[0])
                        if str(i['teams']['away']['id']) == str(away_team_id):
                            if (str(i['scores']['home']['total']) != '20' and str(
                                    i['scores']['home']['total']) != '0') or (
                                    str(i['scores']['away']['total']) != '20' and str(
                                    i['scores']['away']['total']) != '0'):
                                if i['scores']['home']['total'] != None and (
                                        i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                    total = i['scores']['home']['total']
                                    if i['scores']['home']['over_time'] != None:
                                        total -= i['scores']['home']['over_time']

                                    temp_lst_3.append(total)
                                    if i['scores']['home']['over_time'] != None:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(
                                            i['scores']['home']['total'] - i['scores']['home']['over_time']) + ' vs ' + str(
                                            i['scores']['away']['total'] - i['scores']['away'][
                                                'over_time']) + ' season: ' + season)
                                    else:
                                        print(i['teams']['home']['name'] + ' vs ' + i['teams']['away']['name'] + ' ' + str(
                                            i['id']) + '    ' + str(i['scores']['home']['total']) + ' vs ' + str(
                                            i['scores']['away']['total']) + ' season: ' + season)
                                    # temp_lst_3.append(i['scores']['home']['total'] - i['scores']['home']['over_time'])

                                if i['scores']['away']['total'] != None and (
                                        i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                    total = i['scores']['away']['total']
                                    if i['scores']['away']['over_time'] != None:
                                        total -= i['scores']['away']['over_time']
                                    temp_lst_4.append(total)
                                    # temp_lst_4.append(i['scores']['away']['total'] - i['scores']['away']['over_time'])
                                    match_id = i['id']
                                    home_team_here_id = i['teams']['home']['id']
                                    # print(i['teams']['home']['name'])
                                    temp_lst_5.append(
                                        [match_id, home_team_here_id, i['teams']['home']['name'], i['league']['season']])
                                    # for team_season in seasons:
                                    #     away_home = requests.get(f'https://v1.basketball.api-sports.io/games?season={team_season}&team={home_team_here_id}',headers=headers)
                                    #     away_home_json = json.loads(away_home.text)
                                    #     # print(away_home_json)
                                    #     inner_temp = []
                                    #     count = False
                                    #     for j in away_home_json['response']:
                                    #         # print(j['teams']['home']['name'])
                                    #         if count == True:
                                    #             if str(j['teams']['home']['id']) == str(home_team_here_id):
                                    #                 if j['scores']['home']['total'] != None:
                                    #                     inner_temp.append(j['scores']['home']['total'])
                                    #         if str(j['id']) == str(match_id):
                                    #             count = True
                                    #     inner_temp.reverse()
                                    #     for temp in inner_temp:
                                    #         temp_lst_5.append(temp)
                                    #     # print(temp_lst_5)
                                    # away_home_ids.append(temp_lst_5)

                temp_lst_5.reverse()

                for z in temp_lst_5:
                    away_home_ids.append(z)
                    # print(i)

                temp_lst_3.reverse()
                temp_lst_4.reverse()

                for i in temp_lst_3:
                    away_home_points.append(i)
                    # print(i)

                for i in temp_lst_4:
                    away_away_points.append(i)
                    # print(i)

            # print(away_home_points_avg)
            print(away_home_points)
            print(home_home_points)
            print(away_away_points)
            # print(home_away_points_avg)
            print(home_away_points)
            print(away_home_ids[:5])
            print(home_away_ids[:5]) # for first column and fourth column

            # f'{url}?season={season}&team={team_id}&league={league_id}&date={date}',

            # self.get_additional_columns_data(away=False,url='https://v1.basketball.api-sports.io/statistics',
            #                                  season=season,team_id=team_id,league_id=league_id,date=date)


            away_home_points_avg = self.get_away_home_ids(url, away_home_ids, league_id)

            home_away_points_avg = self.get_home_away_ids(url, home_away_ids, league_id)

            if len(away_home_points_avg) >= 5 and len(home_away_points_avg) >= 5:

                for i in range(5):
                    if away_home_points_avg[i] == 0:
                        away_home_points_avg[i] = away_home_points[i]

                    if home_away_points_avg[i] == 0:
                        home_away_points_avg[i] = home_away_points[i]

                away_home_points_avg.append(round(sum(away_home_points_avg) / len(away_home_points_avg), 2))

                away_home_points = away_home_points[:5]
                away_home_points.append(round(sum(away_home_points) / len(away_home_points), 2))

                home_home_points = home_home_points[:5]
                home_home_points.append(round(sum(home_home_points) / len(home_home_points), 2))

                away_away_points = away_away_points[:5]
                away_away_points.append(round(sum(away_away_points) / len(away_away_points), 2))

                # away_away_points = away_away_points[:5]
                # away_away_points.append(round(sum(away_away_points) / len(away_away_points), 2))
                #

                home_away_points_avg.append(round(sum(home_away_points_avg) / len(home_away_points_avg), 2))

                home_away_points = home_away_points[:5]
                home_away_points.append(round(sum(home_away_points) / len(home_away_points), 2))

            # home_home_points[:5]
            # away_away_points[:5]
            # home_away_points_avg
            # home_away_points[:5]

            print(away_home_points_avg)
            print(away_home_points)
            print(home_home_points)
            print(away_away_points)
            print(home_away_points_avg)
            print(home_away_points)

            if len(away_home_points_avg) >= 6 and len(away_home_points) >= 6 and len(home_home_points) >= 6 and len(
                    away_away_points) >= 6 and len(home_away_points_avg) >= 6 and len(home_away_points) >= 6:

                resp = requests.get(
                    f'https://v1.basketball.api-sports.io/statistics?season=2023-2024&team={home_team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                        f'https://v1.basketball.api-sports.io/statistics?season=2023&team={home_team_id}&league={league_id}&date={date}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                        f'https://v1.basketball.api-sports.io/statistics?season=2022-2023&team={home_team_id}&league={league_id}&date={date}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                        f'https://v1.basketball.api-sports.io/statistics?season=2022&team={home_team_id}&league={league_id}&date={date}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] != None:
                    data = pretty_json['response']
                    print(data)
                    games_played_home = int(data['games']['played']['home'])
                    for_total_home = int(data['points']['for']['total']['home'])
                    against_total_home = int(data['points']['against']['total']['home'])
                    try:
                        average_of_total_against_home_points_by_games_played = against_total_home / games_played_home
                    except:
                        average_of_total_against_home_points_by_games_played = 0
                    try:
                        average_of_total_for_home_points_by_games_played = for_total_home / games_played_home
                    except:
                        average_of_total_for_home_points_by_games_played = 0
                else:
                    average_of_total_against_home_points_by_games_played = 'No data'
                    average_of_total_for_home_points_by_games_played = 'No data'

                resp = requests.get(
                    f'https://v1.basketball.api-sports.io/statistics?season=2023-2024&team={away_team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                        f'https://v1.basketball.api-sports.io/statistics?season=2023&team={away_team_id}&league={league_id}&date={date}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)
                    #print(f'https://v1.basketball.api-sports.io/statistics?season=2022&team={away_team_id}&league={league_id}&date={date}')
                    print(True)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                    f'https://v1.basketball.api-sports.io/statistics?season=2022-2023&team={away_team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                        f'https://v1.basketball.api-sports.io/statistics?season=2022&team={away_team_id}&league={league_id}&date={date}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)
                    #print(f'https://v1.basketball.api-sports.io/statistics?season=2022&team={away_team_id}&league={league_id}&date={date}')
                    print(True)

                if pretty_json['response']['country']['id'] != None:
                    data = pretty_json['response']
                    print(data)

                    games_played_away = int(data['games']['played']['away'])
                    for_total_away = int(data['points']['for']['total']['away'])
                    against_total_away = int(data['points']['against']['total']['away'])
                    try:
                        average_of_total_against_away_points_by_games_played = against_total_away / games_played_away
                    except:
                        average_of_total_against_away_points_by_games_played = 0
                    try:
                        average_of_total_for_away_points_by_games_played = for_total_away / games_played_away
                    except:
                        average_of_total_for_away_points_by_games_played = 0
                else:
                    average_of_total_against_away_points_by_games_played = 'No data'
                    average_of_total_for_away_points_by_games_played = 'No data'
                # print(against_total_away, '/', games_played_away)
                # print(for_total_home, '/', games_played_home)
                # print(against_total_home, '/', games_played_home)
                # print(for_total_away, '/', games_played_away)

                first_column_second_row = []
                second_column_second_row = []
                third_column_second_row = []
                fourth_column_second_row = []

                counter_for_scores = 0
                for team_id in away_home_ids[:5]:
                    print(average_of_total_against_home_points_by_games_played,
                          average_of_total_for_home_points_by_games_played)
                    if average_of_total_against_home_points_by_games_played != 'No data' and average_of_total_for_home_points_by_games_played != 'No data':
                        final_results_second_row = self.get_additional_columns_data(
                            home_home_points=away_home_points[counter_for_scores],
                            home_away_points=away_away_points[counter_for_scores],
                            average_1=average_of_total_against_home_points_by_games_played,
                            average_2=average_of_total_for_home_points_by_games_played,
                            away=False, url='https://v1.basketball.api-sports.io/statistics',
                            season='2023-2024', team_id=team_id[1], league_id=league_id, date=date)
                        if final_results_second_row == [0,0]:
                            final_results_second_row = self.get_additional_columns_data(
                            home_home_points=away_home_points[counter_for_scores],
                            home_away_points=away_away_points[counter_for_scores],
                            average_1=average_of_total_against_home_points_by_games_played,
                            average_2=average_of_total_for_home_points_by_games_played,
                            away=False, url='https://v1.basketball.api-sports.io/statistics',
                            season='2022-2023', team_id=team_id[1], league_id=league_id, date=date)
                    else:
                        final_results_second_row = ['No data', 'No data']
                    counter_for_scores += 1

                    print(final_results_second_row)
                    second_column_second_row.append(final_results_second_row[0])
                    third_column_second_row.append(final_results_second_row[1])

                print('---------------------------------------------------------------------')
                counter_for_scores = 0
                for team_id in home_away_ids[:5]:
                    print(average_of_total_against_away_points_by_games_played,
                          average_of_total_for_away_points_by_games_played)
                    if average_of_total_against_away_points_by_games_played != 'No data' and average_of_total_for_away_points_by_games_played != 'No data':
                        final_results_second_row = self.get_additional_columns_data(
                            home_home_points=home_away_points[counter_for_scores],
                            home_away_points=home_home_points[counter_for_scores],
                            average_1=average_of_total_against_away_points_by_games_played,
                            average_2=average_of_total_for_away_points_by_games_played,
                            away=True, url='https://v1.basketball.api-sports.io/statistics',
                            season='2023-2024', team_id=team_id[1], league_id=league_id, date=date)
                        if final_results_second_row == [0,0]:
                            final_results_second_row = self.get_additional_columns_data(
                            home_home_points=home_away_points[counter_for_scores],
                            home_away_points=home_home_points[counter_for_scores],
                            average_1=average_of_total_against_away_points_by_games_played,
                            average_2=average_of_total_for_away_points_by_games_played,
                            away=True, url='https://v1.basketball.api-sports.io/statistics',
                            season='2022-2023', team_id=team_id[1], league_id=league_id, date=date)
                    else:
                        final_results_second_row = ['No data', 'No data']
                    counter_for_scores += 1

                    print(final_results_second_row)
                    fourth_column_second_row.append(final_results_second_row[0])
                    first_column_second_row.append(final_results_second_row[1])

                try:
                    first_column_second_row.append(
                        round(sum(first_column_second_row) / len(first_column_second_row), 2))
                except:
                    first_column_second_row.append('None')
                try:
                    second_column_second_row.append(
                        round(sum(second_column_second_row) / len(second_column_second_row), 2))
                except:
                    second_column_second_row.append('None')
                try:
                    third_column_second_row.append(
                        round(sum(third_column_second_row) / len(third_column_second_row), 2))
                except:
                    third_column_second_row.append('None')
                try:
                    fourth_column_second_row.append(
                        round(sum(fourth_column_second_row) / len(fourth_column_second_row), 2))
                except:
                    fourth_column_second_row.append('None')

                print(first_column_second_row)
                print(second_column_second_row)
                print(third_column_second_row)
                print(fourth_column_second_row)

                final_second_row_results = [first_column_second_row, second_column_second_row, third_column_second_row,
                                            fourth_column_second_row]

                print('checking')
                print(away_away_points[-1], 'numerator')
                print(away_home_points[-1], 'denominator')
                print(home_away_points[-1], 'numerator')
                print(home_home_points[-1], 'denominator')
                print('checked')
                a = round(away_home_points[-1] / away_home_points_avg[-1], 2)  # for column 1 and 2
                b = round(home_away_points[-1] / home_away_points_avg[-1], 2)  # for column 5 and 6

                a_final = round(a * home_home_points[-1], 2)  # for column 3 and 4
                b_final = round(b * away_away_points[-1], 2)  # for column 3 and 4
                result = round(a_final + b_final, 2)  # for column 3 and 4

                f_result_1 = a
                f_result_2 = f'{a_final} = {result} = {b_final}'
                f_result_3 = b
                f_result_4 = round(home_home_points[-1] + away_away_points[-1], 2)

                higher_counter = 0
                higher_counter_2 = 0

                for i in range(5):
                    if away_home_points[i] >= away_home_points_avg[i]:
                        higher_counter += 1
                for i in range(5):
                    if home_away_points[i] >= home_away_points_avg[i]:
                        higher_counter_2 += 1

                final_counter = higher_counter + higher_counter_2

                higher_counter_text = f'{higher_counter} / 5'
                higher_counter_2_text = f'{higher_counter_2} / 5'
                final_counter_text = f'{final_counter} / 10'

                final_dict = [{
                    "away_home_points_avg" : away_home_points_avg,
                    "away_home_points" : away_home_points,
                    "home_home_points" : home_home_points,
                    "away_away_points" : away_away_points,
                    "home_away_points_avg" : home_away_points_avg,
                    "home_away_points" : home_away_points,
                    "f_result_1":f_result_1,
                    "f_result_2" : f_result_2,
                    "f_result_3": f_result_3,
                    "f_result_4":f_result_4,
                    "higher_counter_text":higher_counter_text,
                    "final_counter_text":final_counter_text,
                    "higher_counter_2_text":higher_counter_2_text,
                    "final_score":final_score,
                    "league_name":league_name,
                    "country_name":country_name,
                    "final_second_row_results":final_second_row_results

                }]

            else:
                final_dict = [{"final_score":final_score,
                               "league_name":league_name,
                               "country_name":country_name}]

            return final_dict

        elif self.optionmenu_0.get() == 'Handball':
            seasons = ['2023-2024','2022-2023', '2021-2022']

            url = 'https://v1.handball.api-sports.io/games'

            # home = self.optionmenu_1.get().split('vs')[0].strip(' ').split('            ')[1].strip(' ')
            # away = self.optionmenu_1.get().split('vs')[1].strip(' ')
            #
            # print(home)
            # print(away)

            # home_team_id, away_team_id, league_id = team_id_dict[self.optionmenu_1.get()][0], \
            #                                         team_id_dict[self.optionmenu_1.get()][1], \
            #                                         team_id_dict[self.optionmenu_1.get()][2]
            #
            home_home_points = []
            home_away_points = []

            away_home_points = []
            away_away_points = []

            home_away_ids = []
            away_home_ids = []

            for season in seasons:
                #  fetching data for "home" home team

                temp_lst_1 = []
                temp_lst_2 = []
                resp = requests.get(
                    f'{url}?season={season}&team={home_team_id}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={home_team_id}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # print(pretty_json)
                temp_lst_6 = []
                for i in pretty_json['response']:
                    if str(i['teams']['home']['id']) == str(home_team_id):
                        if (i['scores']['home'] != 10 and i['scores']['away'] != 0) or (i['scores']['away'] != 10 and i['scores']['home'] != 0):

                            if i['scores']['home'] != None and (
                                    i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                temp_lst_1.append(i['scores']['home'])
                                match_id = i['id']
                                away_team_here_id = i['teams']['away']['id']
                                # print(i['teams']['home']['name'])
                                temp_lst_6.append([match_id, away_team_here_id, i['teams']['away']['name']])

                            if i['scores']['away'] != None and (
                                    i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                temp_lst_2.append(i['scores']['away'])

                temp_lst_6.reverse()
                # print(temp_lst_6)
                for z in temp_lst_6:
                    home_away_ids.append(z)

                temp_lst_1.reverse()
                temp_lst_2.reverse()

                for i in temp_lst_1:
                    home_home_points.append(i)
                    # print(i)

                for i in temp_lst_2:
                    home_away_points.append(i)
                    # print(i)

                #  fetching data for "home" away team

                # temp_lst = []
                # resp = requests.get(f'https://v1.basketball.api-sports.io/games?season={season}&team={home_team_id}', headers=headers)
                # pretty_json = json.loads(resp.text)
                # print(pretty_json)
                # for i in pretty_json['response']:
                #     if str(i['teams']['home']['id']) == str(home_team_id):
                #         if i['scores']['away']['total'] != None:
                #             temp_lst.append(i['scores']['away']['total'])
                # temp_lst.reverse()
                # for i in temp_lst:
                #     home_away_points.append(i)
                #     # print(i)

                temp_lst_3 = []
                temp_lst_4 = []
                resp = requests.get(
                    f'{url}?season={season}&team={away_team_id}&league={league_id}',
                    headers=headers)
                pretty_json = json.loads(resp.text)

                if len(pretty_json['response']) == 0:
                    season = season.split('-')[0]
                    resp = requests.get(
                        f'{url}?season={season}&team={away_team_id}&league={league_id}',
                        headers=headers)
                    pretty_json = json.loads(resp.text)

                # print(pretty_json)
                temp_lst_5 = []
                for i in pretty_json['response']:
                    if str(i['teams']['away']['id']) == str(away_team_id):
                        if (i['scores']['home'] != 10 and i['scores']['away'] != 0) or (i['scores']['away'] != 10 and i['scores']['home'] != 0):

                            if i['scores']['home'] != None and (
                                    i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                temp_lst_3.append(i['scores']['home'])

                            if i['scores']['away'] != None and (
                                    i['status']['short'] == "FT" or i['status']['short'] == "AOT"):
                                temp_lst_4.append(i['scores']['away'])
                                match_id = i['id']
                                home_team_here_id = i['teams']['home']['id']
                                # print(i['teams']['home']['name'])
                                temp_lst_5.append([match_id, home_team_here_id, i['teams']['home']['name']])
                                # for team_season in seasons:
                                #     away_home = requests.get(f'https://v1.basketball.api-sports.io/games?season={team_season}&team={home_team_here_id}',headers=headers)
                                #     away_home_json = json.loads(away_home.text)
                                #     # print(away_home_json)
                                #     inner_temp = []
                                #     count = False
                                #     for j in away_home_json['response']:
                                #         # print(j['teams']['home']['name'])
                                #         if count == True:
                                #             if str(j['teams']['home']['id']) == str(home_team_here_id):
                                #                 if j['scores']['home']['total'] != None:
                                #                     inner_temp.append(j['scores']['home']['total'])
                                #         if str(j['id']) == str(match_id):
                                #             count = True
                                #     inner_temp.reverse()
                                #     for temp in inner_temp:
                                #         temp_lst_5.append(temp)
                                #     # print(temp_lst_5)
                                # away_home_ids.append(temp_lst_5)

                temp_lst_5.reverse()

                for z in temp_lst_5:
                    away_home_ids.append(z)
                    # print(i)

                temp_lst_3.reverse()
                temp_lst_4.reverse()

                for i in temp_lst_3:
                    away_home_points.append(i)
                    # print(i)

                for i in temp_lst_4:
                    away_away_points.append(i)
                    # print(i)
            # print('this is home away',away_home_ids)

            # print('this is away home',home_away_ids)

            home_away_points_avg = self.get_home_away_ids_handball(url, home_away_ids, league_id)
            away_home_points_avg = self.get_away_home_ids_handball(url, away_home_ids, league_id)

            if len(away_home_points_avg) >= 5 and len(home_away_points_avg) >= 5:

                for i in range(5):
                    if away_home_points_avg[i] == 0:
                        away_home_points_avg[i] = away_home_points[i]

                    if home_away_points_avg[i] == 0:
                        home_away_points_avg[i] = home_away_points[i]

                away_home_points_avg.append(round(sum(away_home_points_avg) / len(away_home_points_avg), 2))

                away_home_points = away_home_points[:5]
                away_home_points.append(round(sum(away_home_points) / len(away_home_points), 2))

                home_home_points = home_home_points[:5]
                home_home_points.append(round(sum(home_home_points) / len(home_home_points), 2))

                away_away_points = away_away_points[:5]
                away_away_points.append(round(sum(away_away_points) / len(away_away_points), 2))

                # away_away_points = away_away_points[:5]
                # away_away_points.append(round(sum(away_away_points) / len(away_away_points), 2))
                #

                home_away_points_avg.append(round(sum(home_away_points_avg) / len(home_away_points_avg), 2))

                home_away_points = home_away_points[:5]
                home_away_points.append(round(sum(home_away_points) / len(home_away_points), 2))

            # home_home_points[:5]
            # away_away_points[:5]
            # home_away_points_avg
            # home_away_points[:5]

            print(away_home_points_avg)
            print(away_home_points)
            print(home_home_points)
            print(away_away_points)
            print(home_away_points_avg)
            print(home_away_points)

            if len(away_home_points_avg) >= 6 and len(away_home_points) >= 6 and len(home_home_points) >= 6 and len(
                    away_away_points) >= 6 and len(home_away_points_avg) >= 6 and len(home_away_points) >= 6:
                print(home_team_id,league_id,date)
                resp = requests.get(
                    f'https://v1.handball.api-sports.io/teams/statistics?season=2023&team={home_team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                    f'https://v1.handball.api-sports.io/teams/statistics?season=2022&team={home_team_id}&league={league_id}&date={date}',
                    headers=headers)
                    pretty_json = json.loads(resp.text)
                data = pretty_json['response']
                print('this is ', data)
                games_played_home = int(data['games']['played']['home'])
                for_total_home = int(data['goals']['for']['total']['home'])
                against_total_home = int(data['goals']['against']['total']['home'])
                try:
                    average_of_total_against_home_goals_by_games_played = against_total_home / games_played_home
                except:
                    average_of_total_against_home_goals_by_games_played = 0
                try:
                    average_of_total_for_home_goals_by_games_played = for_total_home / games_played_home
                except:
                    average_of_total_for_home_goals_by_games_played = 0

                resp = requests.get(
                    f'https://v1.handball.api-sports.io/teams/statistics?season=2023&team={away_team_id}&league={league_id}&date={date}',
                    headers=headers)
                pretty_json = json.loads(resp.text)
                if pretty_json['response']['country']['id'] == None:
                    resp = requests.get(
                    f'https://v1.handball.api-sports.io/teams/statistics?season=2022&team={away_team_id}&league={league_id}&date={date}',
                    headers=headers)
                    pretty_json = json.loads(resp.text)
                data = pretty_json['response']
                games_played_away = int(data['games']['played']['away'])
                for_total_away = int(data['goals']['for']['total']['away'])
                against_total_away = int(data['goals']['against']['total']['away'])
                try:
                    average_of_total_against_away_goals_by_games_played = against_total_away / games_played_away
                except:
                    average_of_total_against_away_goals_by_games_played = 0
                try:
                    average_of_total_for_away_goals_by_games_played = for_total_away / games_played_away
                except:
                    average_of_total_for_away_goals_by_games_played = 0

                print(against_total_away, '/', games_played_away)
                print(for_total_home, '/', games_played_home)
                print(against_total_home, '/', games_played_home)
                print(for_total_away, '/', games_played_away)

                first_column_second_row = []
                second_column_second_row = []
                third_column_second_row = []
                fourth_column_second_row = []

                counter_for_scores = 0
                for team_id in away_home_ids[:5]:
                    final_results_second_row = self.get_additional_columns_data_handball(
                        home_home_goals=away_home_points[counter_for_scores],
                        home_away_goals=away_away_points[counter_for_scores],
                        average_1=average_of_total_against_home_goals_by_games_played,
                        average_2=average_of_total_for_home_goals_by_games_played,
                        away=False, url='https://v1.handball.api-sports.io/teams/statistics',
                        season='2023', team_id=team_id[1], league_id=league_id, date=date)
                    if final_results_second_row == [0,0]:
                        final_results_second_row = self.get_additional_columns_data_handball(
                        home_home_goals=away_home_points[counter_for_scores],
                        home_away_goals=away_away_points[counter_for_scores],
                        average_1=average_of_total_against_home_goals_by_games_played,
                        average_2=average_of_total_for_home_goals_by_games_played,
                        away=False, url='https://v1.handball.api-sports.io/teams/statistics',
                        season='2022', team_id=team_id[1], league_id=league_id, date=date)
                    counter_for_scores += 1

                    print(final_results_second_row)
                    second_column_second_row.append(final_results_second_row[0])
                    third_column_second_row.append(final_results_second_row[1])

                print('---------------------------------------------------------------------')
                counter_for_scores = 0
                for team_id in home_away_ids[:5]:
                    final_results_second_row = self.get_additional_columns_data_handball(
                        home_home_goals=home_away_points[counter_for_scores],
                        home_away_goals=home_home_points[counter_for_scores],
                        average_1=average_of_total_against_away_goals_by_games_played,
                        average_2=average_of_total_for_away_goals_by_games_played,
                        away=True, url='https://v1.handball.api-sports.io/teams/statistics',
                        season='2023', team_id=team_id[1], league_id=league_id, date=date)
                    if final_results_second_row == [0,0]:
                        final_results_second_row = self.get_additional_columns_data_handball(
                        home_home_goals=home_away_points[counter_for_scores],
                        home_away_goals=home_home_points[counter_for_scores],
                        average_1=average_of_total_against_away_goals_by_games_played,
                        average_2=average_of_total_for_away_goals_by_games_played,
                        away=True, url='https://v1.handball.api-sports.io/teams/statistics',
                        season='2022', team_id=team_id[1], league_id=league_id, date=date)

                    counter_for_scores += 1

                    print(final_results_second_row)
                    fourth_column_second_row.append(final_results_second_row[0])
                    first_column_second_row.append(final_results_second_row[1])

                try:
                    first_column_second_row.append(
                        round(sum(first_column_second_row) / len(first_column_second_row), 2))
                except:
                    first_column_second_row.append('None')
                try:
                    second_column_second_row.append(
                        round(sum(second_column_second_row) / len(second_column_second_row), 2))
                except:
                    second_column_second_row.append('None')
                try:
                    third_column_second_row.append(
                        round(sum(third_column_second_row) / len(third_column_second_row), 2))
                except:
                    third_column_second_row.append('None')
                try:
                    fourth_column_second_row.append(
                        round(sum(fourth_column_second_row) / len(fourth_column_second_row), 2))
                except:
                    fourth_column_second_row.append('None')

                print(first_column_second_row)
                print(second_column_second_row)
                print(third_column_second_row)
                print(fourth_column_second_row)

                final_second_row_results = [first_column_second_row, second_column_second_row, third_column_second_row,
                                            fourth_column_second_row]

                print('checking')
                print(away_away_points[-1], 'numerator')
                print(away_home_points[-1], 'denominator')
                print(home_away_points[-1], 'numerator')
                print(home_home_points[-1], 'denominator')
                print('checked')
                a = round(away_home_points[-1] / away_home_points_avg[-1], 2)  # for column 1 and 2
                b = round(home_away_points[-1] / home_away_points_avg[-1], 2)  # for column 5 and 6

                a_final = round(a * home_home_points[-1], 2)  # for column 3 and 4
                b_final = round(b * away_away_points[-1], 2)  # for column 3 and 4
                result = round(a_final + b_final, 2)  # for column 3 and 4

                f_result_1 = a
                f_result_2 = f'{a_final} = {result} = {b_final}'
                f_result_3 = b
                f_result_4 = round(home_home_points[-1] + away_away_points[-1], 2)

                higher_counter = 0
                higher_counter_2 = 0

                for i in range(5):
                    if away_home_points[i] >= away_home_points_avg[i]:
                        higher_counter += 1
                for i in range(5):
                    if home_away_points[i] >= home_away_points_avg[i]:
                        higher_counter_2 += 1

                final_counter = higher_counter + higher_counter_2

                higher_counter_text = f'{higher_counter} / 5'
                higher_counter_2_text = f'{higher_counter_2} / 5'
                final_counter_text = f'{final_counter} / 10'

                final_dict = [{
                    "away_home_points_avg": away_home_points_avg,
                    "away_home_points": away_home_points,
                    "home_home_points": home_home_points,
                    "away_away_points": away_away_points,
                    "home_away_points_avg": home_away_points_avg,
                    "home_away_points": home_away_points,
                    "f_result_1": f_result_1,
                    "f_result_2": f_result_2,
                    "f_result_3": f_result_3,
                    "f_result_4": f_result_4,
                    "higher_counter_text": higher_counter_text,
                    "final_counter_text": final_counter_text,
                    "higher_counter_2_text": higher_counter_2_text,
                    "final_score": final_score,
                    "league_name":league_name,
                    "country_name":country_name,
                    "final_second_row_results":final_second_row_results

                }]

            else:
                final_dict = [{"final_score":final_score,
                               "league_name":league_name,
                               "country_name":country_name}]

            return final_dict

    def get_data(self,index):
        if self.optionmenu_1.get() == 'Select date first':
            tkinter.messagebox.showinfo('Error', 'Please select a date first')
        else:
            
            if index == None:
                index = int(self.optionmenu_1.get().split('.')[0])
            # self.complete_data = {}
            print(now_date)
            single_team_data = self.complete_data[index]
            print(single_team_data)
            final_data = self.get_teams_data_advance(single_team_data[0],single_team_data[1],
                                                     single_team_data[2],single_team_data[3],
                                                     single_team_data[4],single_team_data[5], single_team_data[6])

            left_1 = 0
            left_2 = 0
            right_1 = 0
            right_2 = 0
            if 'away_home_points_avg' in final_data[0] and single_team_data[4] != '':
                print('new hehe')

                print(single_team_data[4])
                print(final_data)
                if single_team_data[4] != '':
                    total_score = single_team_data[4].split(':')
                    total_score = int(total_score[0]) + int(total_score[1])
                    above_text = float(final_data[0]['f_result_4'])
                    lower_text = int(final_data[0]['final_counter_text'].split('/')[0])
                    if lower_text >= 8:
                        if total_score > above_text:
                            left_1+=1
                        else:
                            left_2+=1
                    elif lower_text <= 2:
                        if total_score > above_text:
                            right_1+=1
                        else:
                            right_2+=1
                print('left ',left_1)
                print(left_2)
                print(right_1)
                print(right_2)
            self.different_counters_left.configure(text=f'{left_1} / {left_2}')
            self.different_counters_right.configure(text=f'{right_1} / {right_2}')

            # print(len(final_data))
            # print(final_data)

            if 'away_home_points_avg' not in final_data[0]:

                final_score = final_data[0]['final_score']
                league_name = final_data[0]['league_name']
                country_name = final_data[0]['country_name']

                self.table.delete(*self.table.get_children())
                self.result_label_1.configure(text='')
                self.result_label_2.configure(text='')
                self.result_label_3.configure(text='')
                self.result_label_4.configure(text='')
                self.result_label_5.configure(text='')
                self.result_label_6.configure(text='')
                self.result_label_7.configure(text='')
                self.final_score.configure(text=final_score)
                self.league_name.configure(text=league_name)
                self.country_name.configure(text=country_name)
                self.result_label_8.configure(text='Not enough data for one of the teams')
                self.result_label_8.place(x=280, y=210)
                # self.result_label.place(x=128, y=300)

            else:
                self.table.delete(*self.table.get_children())

                away_home_points_avg = final_data[0]['away_home_points_avg']
                away_home_points = final_data[0]['away_home_points']
                home_home_points = final_data[0]['home_home_points']
                away_away_points = final_data[0]['away_away_points']
                home_away_points_avg = final_data[0]['home_away_points_avg']
                home_away_points = final_data[0]['home_away_points']
                f_result_1 = final_data[0]['f_result_1']
                f_result_2 = final_data[0]['f_result_2']
                f_result_3 = final_data[0]['f_result_3']
                f_result_4 = final_data[0]['f_result_4']
                higher_counter_text = final_data[0]['higher_counter_text']
                final_counter_text = final_data[0]['final_counter_text']
                higher_counter_2_text = final_data[0]['higher_counter_2_text']
                final_score = final_data[0]['final_score']
                league_name = final_data[0]['league_name']
                country_name = final_data[0]['country_name']
                final_second_row_results = final_data[0]['final_second_row_results']

                indexer = 1
                for i in range(6):
                    self.table.insert("", 'end', text="L" + str(indexer),
                                      values=(away_home_points_avg[i], away_home_points[i],
                                              home_home_points[i], away_away_points[i],
                                              home_away_points_avg[i], home_away_points[i]), tags='TkTextFont')
                    indexer += 1

                for i in range(4):
                    self.table.insert("", 'end', text="L" + str(indexer),
                                      values=('', '','', '','', ''), tags='TkTextFont')
                    indexer += 1

                for i in range(5):
                    self.table.insert("", 'end', text="L" + str(indexer),
                                      values=(final_second_row_results[0][i], final_second_row_results[1][i],'', '',final_second_row_results[2][i],final_second_row_results[3][i]), tags='TkTextFont')
                    indexer += 1

                self.table.insert("", 'end', text="L" + str(indexer),
                                  values=(final_second_row_results[0][-1], final_second_row_results[1][-1],'', '',final_second_row_results[2][-1],final_second_row_results[3][-1]), tags='average_color_change')


                # print(away_home_points_avg)
                # print(away_home_points)
                # print(home_home_points)
                # print(away_away_points)
                # print(home_away_points_avg)
                # print(home_away_points)

                if int(higher_counter_text.split('/')[0]) >= 4:
                    fg_color_left = '#22AA49'
                elif int(higher_counter_text.split('/')[0]) <= 1:
                    fg_color_left = '#CE2027'
                else:
                    fg_color_left = 'white'

                if int(higher_counter_2_text.split('/')[0]) >= 4:
                    fg_color_right = '#22AA49'
                elif int(higher_counter_2_text.split('/')[0]) <= 1:
                    fg_color_right = '#CE2027'
                else:
                    fg_color_right = 'white'

                
                if int(final_counter_text.split('/')[0]) >= 8:
                    fg_color_middle = '#22AA49'
                elif int(final_counter_text.split('/')[0]) <= 2:
                    fg_color_middle = '#CE2027'
                elif int(final_counter_text.split('/')[0]) <= 7 and int(final_counter_text.split('/')[0]) >= 5:
                    fg_color_middle = '#01a1e8'
                else:
                    fg_color_middle = 'white'

                self.result_label_1.configure(text=f_result_1)
                self.result_label_2.configure(text=f_result_2)
                self.result_label_3.configure(text=f_result_3)
                self.result_label_4.configure(text=f_result_4)
                self.result_label_5.configure(text=higher_counter_text, text_color=fg_color_left)
                self.result_label_6.configure(text=final_counter_text, text_color=fg_color_middle)
                self.result_label_7.configure(text=higher_counter_2_text, text_color=fg_color_right)
                self.final_score.configure(text=final_score)
                self.league_name.configure(text=league_name)
                self.country_name.configure(text=country_name)
                self.result_label_8.place_forget()

##################################################  Handball #####################################################


            #     self.table.delete(*self.table.get_children())
            #
            #     indexer = 1
            #     for i in range(6):
            #         self.table.insert("", 'end', text="L" + str(indexer),
            #                           values=(away_home_points_avg[i], away_home_points[i],
            #                                   home_home_points[i], away_away_points[i],
            #                                   home_away_points_avg[i], home_away_points[i]), tags='TkTextFont')
            #         indexer += 1
            #
            #     self.result_label_1.configure(text=f_result_1)
            #     self.result_label_2.configure(text=f_result_2)
            #     self.result_label_3.configure(text=f_result_3)
            #     self.result_label_4.configure(text=f_result_4)
            #     self.result_label_8.configure(text='')
            #
            # else:
            #     self.table.delete(*self.table.get_children())
            #
            #     self.result_label_8.configure(text='Not enough data for one of the teams')
            #     # self.result_label.place(x=128, y=300)

class front_frame(customtkinter.CTk):
    COUNT = 0

    def __init__(self):
        super().__init__()

        style = ttk.Style()

        style.theme_use("default")

        style.configure("Treeview",
                        background="#343638",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#F3F1E9",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        font=(None, 17))
        style.map("Treeview.Heading",
                  background=[('active', '#3484F0')])

        self.on_closing = None
        self.var = customtkinter.StringVar(self)
        self.title("ClassApp")
        # self.iconbitmap("Files/Images/camera.ico")
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # self.window_width = screen_width
        # self.window_height = screen_height
        # self.geometry("%dx%d" % (self.window_width, self.window_height))
        self.geometry(f"1330x730")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        # self.button_2 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Delete Item",
        #                                         corner_radius=15,
        #                                         border_width=1.5,
        #                                         border_color="#3484F0",  # alternative red: #f03933
        #                                         fg_color="#343638",
        #                                         cursor='hand2',
        #                                         command=None)
        # self.button_2.grid(row=3, column=0, pady=15, padx=20)
        #
        # self.button_3 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Edit Item",
        #                                         corner_radius=15,
        #                                         border_width=1.5,
        #                                         border_color="#3484F0",
        #                                         fg_color="#343638",
        #                                         cursor='hand2',
        #                                         command=None)
        # self.button_3.grid(row=4, column=0, pady=15, padx=20)

        self.preload_btn = customtkinter.CTkButton(master=self,
                                                text="PRE-LOAD",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=lambda : self.des_frame_for_pre(),
                                                cursor='hand2', font=("Roboto Medium", -30))
        self.preload_btn.pack(pady=(230,100), ipadx=40, ipady=5)

        self.single_btn = customtkinter.CTkButton(master=self,
                                                text="SINGLE",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=lambda: self.des_frame_for_single(),
                                                cursor='hand2', font=("Roboto Medium", -30))
        self.single_btn.pack( ipadx=60, ipady=5)

        self.mainloop()

    def des_frame_for_pre(self):
        self.destroy()
        Pre_load_App()

    def des_frame_for_single(self):
        self.destroy()
        Single_load_App()

# if __name__ == "__main__":
#     app = front_frame()
#
#     app.mainloop()
if __name__ == '__main__':

    frontFrame = front_frame()
    # frontFrame.mainloop()