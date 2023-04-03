import io
import sys
from tkinter import TOP, Toplevel, ttk
import customtkinter as ctk
import requests
import json

from PIL import Image, ImageTk

pokemonSets = ctk.CTk()
pokemonSets.geometry('1250x750')
pokemonSets.title('Pokémon TCG')

# retrieve series json file of series from GitHub
setsJson = requests.get("https://api.pokemontcg.io/v2/sets?orderBy=series&orderBy=releaseDate")
setsLoad = setsJson.text
setsData = json.loads(setsLoad)

# filter list of cards by base set
filtered_base_sets = [
    dictionary for dictionary in setsData['data']
    if dictionary['series'] == 'Base'
]

# filter list of cards by gym set
filtered_gym_sets = [
    dictionary for dictionary in setsData['data']
    if dictionary['series'] == 'Gym'
]

# filter list of cards by neo set
filtered_neo_sets = [
    dictionary for dictionary in setsData['data']
    if dictionary['series'] == 'Neo'
]

filtered_legendary_sets = [
    dictionary for dictionary in setsData['data']
    if dictionary['series'] == 'Other'
]

filtered_ecard_sets = [
    dictionary for dictionary in setsData['data']
    if dictionary['series'] == 'E-Card'
]

filtered_ex_sets = [
    dictionary for dictionary in setsData['data']
    if dictionary['series'] == 'EX'
]

scrollable_frame = ctk.CTkScrollableFrame(pokemonSets, width=1250, height=750)
scrollable_frame.pack()

def basePromoCards():

    baseSetPromoWindow = Toplevel(pokemonSets)
    baseSetPromoWindow.title("Wizards Black Star Promos")
    baseSetPromoWindow.geometry("1250x750")

    try:
        r = requests.get(filtered_base_sets[2]['images']['logo'])

    except requests.exceptions.RequestException as error:
        print(error)
        set.destroy() # <-- close window
        sys.exit(1)

    fp = io.BytesIO(r.content) # <-- create file-like object in memory
    image = Image.open(fp) # <-- use file-like object in memory
    new_image = image.resize((150, 100))
    photo = ImageTk.PhotoImage(new_image)

    label_image = ttk.Label(master=baseSetPromoWindow)  # <-- place for image

    label_image.config(image=photo) # <-- show image in label
    label_image.image=photo # <-- solution for problem with garbage-collector & PhotoImage

    label_image.pack()

    # Treeview
    table = ttk.Treeview(baseSetPromoWindow,
                         columns=('Card No', 'Name', 'Type', 'Rarity', 'Market'),
                         show='headings')
    table.heading('Card No', text='Card No')
    table.heading('Name', text='Name')
    table.heading('Type', text='Type')
    table.heading('Rarity', text='Rarity')
    table.heading('Market', text='Market Value')
    table.pack(fill='both', expand=True)

    # retrieve series json file of series from GitHub
    cardsJson = requests.get("https://api.pokemontcg.io/v2/cards?orderBy=-number&q=id:basep")
    cardsLoad = cardsJson.text
    cardsData = json.loads(cardsLoad)

    for cards in cardsData['data']:

        # Number Column
        card_no = cards['number']

        # Name Column
        name = cards['name']

        # Type Column
        try:
            card_type = cards['types'][0]
        except KeyError:
            if cards['supertype'] == "Trainer":
                card_type = "Trainer"
            if cards['supertype'] == "Energy":
                card_type = "Energy"

        # Rarity Column
        try:
            rarity = cards['rarity']
        except KeyError:
            rarity = "-"

        # Standard Market Column
        try:
            market_price_standard = cards['tcgplayer']['prices']['normal']['market']
            format_number_standard = "${:,.2f}".format(market_price_standard)
        except KeyError:
            try:
                market_price_standard = cards['tcgplayer']['prices']['holofoil']['market']
                format_number_standard = "${:,.2f}".format(market_price_standard)
            except KeyError:
                format_number_standard = "-"

        data = (card_no, name, card_type, rarity, format_number_standard)
        table.insert(parent='', index=0, values=data)

    table.insert(parent='', index=ctk.END)

def baseCards():

    baseSetWindow = Toplevel(pokemonSets)
    baseSetWindow.title("Base Set")
    baseSetWindow.geometry("1250x750")

    try:
        r = requests.get(filtered_base_sets[0]['images']['logo'])

    except requests.exceptions.RequestException as error:
        print(error)
        set.destroy() # <-- close window
        sys.exit(1)

    fp = io.BytesIO(r.content) # <-- create file-like object in memory
    image = Image.open(fp) # <-- use file-like object in memory
    new_image = image.resize((275, 100))
    photo = ImageTk.PhotoImage(new_image)

    label_image = ttk.Label(master=baseSetWindow)  # <-- place for image

    label_image.config(image=photo) # <-- show image in label
    label_image.image=photo # <-- solution for problem with garbage-collector & PhotoImage

    label_image.pack()

    # Treeview
    table = ttk.Treeview(baseSetWindow,
                         columns=('Card No', 'Name', 'Type', 'Rarity', 'Market'),
                         show='headings')
    table.heading('Card No', text='Card No')
    table.heading('Name', text='Name')
    table.heading('Type', text='Type')
    table.heading('Rarity', text='Rarity')
    table.heading('Market', text='Market Value')
    table.pack(fill='both', expand=True)

    # retrieve series json file of series from GitHub
    cardsJson = requests.get("https://api.pokemontcg.io/v2/cards?orderBy=-number&q=id:base1")
    cardsLoad = cardsJson.text
    cardsData = json.loads(cardsLoad)

    for cards in cardsData['data']:

        # Number Column
        card_no = cards['number']

        # Name Column
        name = cards['name']

        # Type Column
        try:
            card_type = cards['types'][0]
        except KeyError:
            if cards['supertype'] == "Trainer":
                card_type = "Trainer"
            if cards['supertype'] == "Energy":
                card_type = "Energy"

        # Rarity Column
        try:
            rarity = cards['rarity']
        except KeyError:
            rarity = "-"

        # Standard Market Column
        try:
            market_price_standard = cards['tcgplayer']['prices']['normal']['market']
            format_number_standard = "${:,.2f}".format(market_price_standard)
        except KeyError:
            try:
                market_price_standard = cards['tcgplayer']['prices']['holofoil']['market']
                format_number_standard = "${:,.2f}".format(market_price_standard)
            except KeyError:
                format_number_standard = "-"

        data = (card_no, name, card_type, rarity, format_number_standard)
        table.insert(parent='', index=0, values=data)

    table.insert(parent='', index=ctk.END)

def baseJungleCards():

    baseJungleSetWindow = Toplevel(pokemonSets)
    baseJungleSetWindow.title("Jungle")
    baseJungleSetWindow.geometry("1250x750")

    try:
        r = requests.get(filtered_base_sets[1]['images']['logo'])

    except requests.exceptions.RequestException as error:
        print(error)
        set.destroy() # <-- close window
        sys.exit(1)

    fp = io.BytesIO(r.content) # <-- create file-like object in memory
    image = Image.open(fp) # <-- use file-like object in memory
    new_image = image.resize((200, 100))
    photo = ImageTk.PhotoImage(new_image)

    label_image = ttk.Label(master=baseJungleSetWindow)  # <-- place for image

    label_image.config(image=photo) # <-- show image in label
    label_image.image=photo # <-- solution for problem with garbage-collector & PhotoImage

    label_image.pack()

    # Treeview
    table = ttk.Treeview(baseJungleSetWindow,
                         columns=('Card No', 'Name', 'Type', 'Rarity', 'Market'),
                         show='headings')
    table.heading('Card No', text='Card No')
    table.heading('Name', text='Name')
    table.heading('Type', text='Type')
    table.heading('Rarity', text='Rarity')
    table.heading('Market', text='Market Value')
    table.pack(fill='both', expand=True)

    # retrieve series json file of series from GitHub
    cardsJson = requests.get("https://api.pokemontcg.io/v2/cards?orderBy=-number&q=id:base2")
    cardsLoad = cardsJson.text
    cardsData = json.loads(cardsLoad)

    for cards in cardsData['data']:

        # Number Column
        card_no = cards['number']

        # Name Column
        name = cards['name']

        # Type Column
        try:
            card_type = cards['types'][0]
        except KeyError:
            if cards['supertype'] == "Trainer":
                card_type = "Trainer"
            if cards['supertype'] == "Energy":
                card_type = "Energy"

        # Rarity Column
        try:
            rarity = cards['rarity']
        except KeyError:
            rarity = "-"

        # Standard Market Column
        try:
            market_price_standard = cards['tcgplayer']['prices']['unlimited']['market']
            format_number_standard = "${:,.2f}".format(market_price_standard)
        except KeyError:
            try:
                market_price_standard = cards['tcgplayer']['prices']['unlimitedHolofoil']['market']
                format_number_standard = "${:,.2f}".format(market_price_standard)
            except KeyError:
                format_number_standard = "-"

        data = (card_no, name, card_type, rarity, format_number_standard)
        table.insert(parent='', index=0, values=data)

    table.insert(parent='', index=ctk.END)

def baseFossilCards():

    baseFossilSetWindow = Toplevel(pokemonSets)
    baseFossilSetWindow.title("Fossil")
    baseFossilSetWindow.geometry("1250x750")

    try:
        r = requests.get(filtered_base_sets[3]['images']['logo'])

    except requests.exceptions.RequestException as error:
        print(error)
        set.destroy() # <-- close window
        sys.exit(1)

    fp = io.BytesIO(r.content) # <-- create file-like object in memory
    image = Image.open(fp) # <-- use file-like object in memory
    new_image = image.resize((200, 100))
    photo = ImageTk.PhotoImage(new_image)

    label_image = ttk.Label(master=baseFossilSetWindow)  # <-- place for image

    label_image.config(image=photo) # <-- show image in label
    label_image.image=photo # <-- solution for problem with garbage-collector & PhotoImage

    label_image.pack()

    # Treeview
    table = ttk.Treeview(baseFossilSetWindow,
                         columns=('Card No', 'Name', 'Type', 'Rarity', 'Market'),
                         show='headings')
    table.heading('Card No', text='Card No')
    table.heading('Name', text='Name')
    table.heading('Type', text='Type')
    table.heading('Rarity', text='Rarity')
    table.heading('Market', text='Market Value')
    table.pack(fill='both', expand=True)

    # retrieve series json file of series from GitHub
    cardsJson = requests.get("https://api.pokemontcg.io/v2/cards?orderBy=-number&q=id:base3")
    cardsLoad = cardsJson.text
    cardsData = json.loads(cardsLoad)

    for cards in cardsData['data']:

        # Number Column
        card_no = cards['number']

        # Name Column
        name = cards['name']

        # Type Column
        try:
            card_type = cards['types'][0]
        except KeyError:
            if cards['supertype'] == "Trainer":
                card_type = "Trainer"
            if cards['supertype'] == "Energy":
                card_type = "Energy"

        # Rarity Column
        try:
            rarity = cards['rarity']
        except KeyError:
            rarity = "-"

        # Standard Market Column
        try:
            market_price_standard = cards['tcgplayer']['prices']['unlimited']['market']
            format_number_standard = "${:,.2f}".format(market_price_standard)
        except KeyError:
            try:
                market_price_standard = cards['tcgplayer']['prices']['unlimitedHolofoil']['market']
                format_number_standard = "${:,.2f}".format(market_price_standard)
            except KeyError:
                format_number_standard = "-"

        data = (card_no, name, card_type, rarity, format_number_standard)
        table.insert(parent='', index=0, values=data)

    table.insert(parent='', index=ctk.END)

def base2Cards():

    baseSet2Window = Toplevel(pokemonSets)
    baseSet2Window.title("Base Set 2")
    baseSet2Window.geometry("1250x750")

    try:
        r = requests.get(filtered_base_sets[4]['images']['logo'])

    except requests.exceptions.RequestException as error:
        print(error)
        set.destroy() # <-- close window
        sys.exit(1)

    fp = io.BytesIO(r.content) # <-- create file-like object in memory
    image = Image.open(fp) # <-- use file-like object in memory
    new_image = image.resize((200, 100))
    photo = ImageTk.PhotoImage(new_image)

    label_image = ttk.Label(master=baseSet2Window)  # <-- place for image

    label_image.config(image=photo) # <-- show image in label
    label_image.image=photo # <-- solution for problem with garbage-collector & PhotoImage

    label_image.pack()

    # Treeview
    table = ttk.Treeview(baseSet2Window,
                         columns=('Card No', 'Name', 'Type', 'Rarity', 'Market'),
                         show='headings')
    table.heading('Card No', text='Card No')
    table.heading('Name', text='Name')
    table.heading('Type', text='Type')
    table.heading('Rarity', text='Rarity')
    table.heading('Market', text='Market Value')
    table.pack(fill='both', expand=True)

    # retrieve series json file of series from GitHub
    cardsJson = requests.get("https://api.pokemontcg.io/v2/cards?orderBy=-number&q=id:base4")
    cardsLoad = cardsJson.text
    cardsData = json.loads(cardsLoad)

    for cards in cardsData['data']:

        # Number Column
        card_no = cards['number']

        # Name Column
        name = cards['name']

        # Type Column
        try:
            card_type = cards['types'][0]
        except KeyError:
            if cards['supertype'] == "Trainer":
                card_type = "Trainer"
            if cards['supertype'] == "Energy":
                card_type = "Energy"

        # Rarity Column
        try:
            rarity = cards['rarity']
        except KeyError:
            rarity = "-"

        # Standard Market Column
        try:
            market_price_standard = cards['tcgplayer']['prices']['normal']['market']
            format_number_standard = "${:,.2f}".format(market_price_standard)
        except KeyError:
            try:
                market_price_standard = cards['tcgplayer']['prices']['holofoil']['market']
                format_number_standard = "${:,.2f}".format(market_price_standard)
            except KeyError:
                format_number_standard = "-"

        data = (card_no, name, card_type, rarity, format_number_standard)
        table.insert(parent='', index=0, values=data)

    table.insert(parent='', index=ctk.END)

def baseTeamRocketCards():

    baseTeamRocketSetWindow = Toplevel(pokemonSets)
    baseTeamRocketSetWindow.title("Team Rocket")
    baseTeamRocketSetWindow.geometry("1250x750")

    try:
        r = requests.get(filtered_base_sets[5]['images']['logo'])

    except requests.exceptions.RequestException as error:
        print(error)
        set.destroy() # <-- close window
        sys.exit(1)

    fp = io.BytesIO(r.content) # <-- create file-like object in memory
    image = Image.open(fp) # <-- use file-like object in memory
    new_image = image.resize((300, 100))
    photo = ImageTk.PhotoImage(new_image)

    label_image = ttk.Label(master=baseTeamRocketSetWindow)  # <-- place for image

    label_image.config(image=photo) # <-- show image in label
    label_image.image=photo # <-- solution for problem with garbage-collector & PhotoImage

    label_image.pack()

    # Treeview
    table = ttk.Treeview(baseTeamRocketSetWindow,
                         columns=('Card No', 'Name', 'Type', 'Rarity', 'Market'),
                         show='headings')
    table.heading('Card No', text='Card No')
    table.heading('Name', text='Name')
    table.heading('Type', text='Type')
    table.heading('Rarity', text='Rarity')
    table.heading('Market', text='Market Value')
    table.pack(fill='both', expand=True)

    # retrieve series json file of series from GitHub
    cardsJson = requests.get("https://api.pokemontcg.io/v2/cards?orderBy=-number&q=id:base5")
    cardsLoad = cardsJson.text
    cardsData = json.loads(cardsLoad)

    for cards in cardsData['data']:

        # Number Column
        card_no = cards['number']

        # Name Column
        name = cards['name']

        # Type Column
        try:
            card_type = cards['types'][0]
        except KeyError:
            if cards['supertype'] == "Trainer":
                card_type = "Trainer"
            if cards['supertype'] == "Energy":
                card_type = "Energy"

        # Rarity Column
        try:
            rarity = cards['rarity']
        except KeyError:
            rarity = "-"

        # Standard Market Column
        try:
            market_price_standard = cards['tcgplayer']['prices']['unlimited']['market']
            format_number_standard = "${:,.2f}".format(market_price_standard)
        except KeyError:
            try:
                market_price_standard = cards['tcgplayer']['prices']['unlimitedHolofoil']['market']
                format_number_standard = "${:,.2f}".format(market_price_standard)
            except KeyError:
                format_number_standard = "-"

        data = (card_no, name, card_type, rarity, format_number_standard)
        table.insert(parent='', index=0, values=data)

    table.insert(parent='', index=ctk.END)

class originalSeries:

    original_label = ctk.CTkLabel(scrollable_frame, text="Original Series", font=ctk.CTkFont(size=30, weight="bold"))
    original_label.pack(pady=10, side=TOP)

    def basePromoInfo():
        json_data = filtered_base_sets

        try:
            r = requests.get(json_data[2]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_base_sets[2]['name']

        base_button1 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50, command=basePromoCards)
        base_button1.pack(pady=5)

    def baseSetInfo():
        json_data = filtered_base_sets

        try:
            r = requests.get(json_data[0]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image, size=[30,20])

        name = filtered_base_sets[0]['name'] + " Set"

        base_button2 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50, command=baseCards)
        base_button2.pack(pady=5)

    def jungleInfo():
        json_data = filtered_base_sets

        try:
            r = requests.get(json_data[1]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_base_sets[1]['name']

        base_button3 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50, command=baseJungleCards)
        base_button3.pack(pady=5)

    def fossilInfo():
        json_data = filtered_base_sets

        try:
            r = requests.get(json_data[3]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_base_sets[3]['name']

        base_button4 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50, command=baseFossilCards)
        base_button4.pack(pady=5)

    def baseSet2Info():
        json_data = filtered_base_sets

        try:
            r = requests.get(json_data[4]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_base_sets[4]['name']

        base_button5 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50, command=base2Cards)
        base_button5.pack(pady=5)

    def teamRocketInfo():
        json_data = filtered_base_sets

        try:
            r = requests.get(json_data[5]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_base_sets[5]['name']

        base_button6 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50, command=baseTeamRocketCards)
        base_button6.pack(pady=5)

    basePromoInfo()
    baseSetInfo()
    jungleInfo()
    fossilInfo()
    baseSet2Info()
    teamRocketInfo()

def gymHeroesCards():

    gymHeroesSetWindow = Toplevel(pokemonSets)
    gymHeroesSetWindow.title("Gym Heroes")
    gymHeroesSetWindow.geometry("1250x750")

    try:
        r = requests.get(filtered_gym_sets[0]['images']['logo'])

    except requests.exceptions.RequestException as error:
        print(error)
        set.destroy() # <-- close window
        sys.exit(1)

    fp = io.BytesIO(r.content) # <-- create file-like object in memory
    image = Image.open(fp) # <-- use file-like object in memory
    new_image = image.resize((300, 100))
    photo = ImageTk.PhotoImage(new_image)

    label_image = ttk.Label(master=gymHeroesSetWindow)  # <-- place for image

    label_image.config(image=photo) # <-- show image in label
    label_image.image=photo # <-- solution for problem with garbage-collector & PhotoImage

    label_image.pack()

    # Treeview
    table = ttk.Treeview(gymHeroesSetWindow,
                         columns=('Card No', 'Name', 'Type', 'Rarity', 'Market'),
                         show='headings')
    table.heading('Card No', text='Card No')
    table.heading('Name', text='Name')
    table.heading('Type', text='Type')
    table.heading('Rarity', text='Rarity')
    table.heading('Market', text='Market Value')
    table.pack(fill='both', expand=True)

    # retrieve series json file of series from GitHub
    cardsJson = requests.get("https://api.pokemontcg.io/v2/cards?orderBy=-number&q=id:gym1")
    cardsLoad = cardsJson.text
    cardsData = json.loads(cardsLoad)

    for cards in cardsData['data']:

        # Number Column
        card_no = cards['number']

        # Name Column
        name = cards['name']

        # Type Column
        try:
            card_type = cards['types'][0]
        except KeyError:
            if cards['supertype'] == "Trainer":
                card_type = "Trainer"
            if cards['supertype'] == "Energy":
                card_type = "Energy"

        # Rarity Column
        try:
            rarity = cards['rarity']
        except KeyError:
            rarity = "-"

        # Standard Market Column
        try:
            market_price_standard = cards['tcgplayer']['prices']['unlimited']['market']
            format_number_standard = "${:,.2f}".format(market_price_standard)
        except KeyError:
            try:
                market_price_standard = cards['tcgplayer']['prices']['unlimitedHolofoil']['market']
                format_number_standard = "${:,.2f}".format(market_price_standard)
            except KeyError:
                format_number_standard = "-"

        data = (card_no, name, card_type, rarity, format_number_standard)
        table.insert(parent='', index=0, values=data)

    table.insert(parent='', index=ctk.END)

def gymChallengeCards():

    gymChallengeSetWindow = Toplevel(pokemonSets)
    gymChallengeSetWindow.title("Gym Challenge")
    gymChallengeSetWindow.geometry("1250x750")

    try:
        r = requests.get(filtered_gym_sets[1]['images']['logo'])

    except requests.exceptions.RequestException as error:
        print(error)
        set.destroy() # <-- close window
        sys.exit(1)

    fp = io.BytesIO(r.content) # <-- create file-like object in memory
    image = Image.open(fp) # <-- use file-like object in memory
    new_image = image.resize((300, 100))
    photo = ImageTk.PhotoImage(new_image)

    label_image = ttk.Label(master=gymChallengeSetWindow)  # <-- place for image

    label_image.config(image=photo) # <-- show image in label
    label_image.image=photo # <-- solution for problem with garbage-collector & PhotoImage

    label_image.pack()

    # Treeview
    table = ttk.Treeview(gymChallengeSetWindow,
                         columns=('Card No', 'Name', 'Type', 'Rarity', 'Market'),
                         show='headings')
    table.heading('Card No', text='Card No')
    table.heading('Name', text='Name')
    table.heading('Type', text='Type')
    table.heading('Rarity', text='Rarity')
    table.heading('Market', text='Market Value')
    table.pack(fill='both', expand=True)

    # retrieve series json file of series from GitHub
    cardsJson = requests.get("https://api.pokemontcg.io/v2/cards?orderBy=-number&q=id:gym2")
    cardsLoad = cardsJson.text
    cardsData = json.loads(cardsLoad)

    for cards in cardsData['data']:

        # Number Column
        card_no = cards['number']

        # Name Column
        name = cards['name']

        # Type Column
        try:
            card_type = cards['types'][0]
        except KeyError:
            if cards['supertype'] == "Trainer":
                card_type = "Trainer"
            if cards['supertype'] == "Energy":
                card_type = "Energy"

        # Rarity Column
        try:
            rarity = cards['rarity']
        except KeyError:
            rarity = "-"

        # Standard Market Column
        try:
            market_price_standard = cards['tcgplayer']['prices']['unlimited']['market']
            format_number_standard = "${:,.2f}".format(market_price_standard)
        except KeyError:
            try:
                market_price_standard = cards['tcgplayer']['prices']['unlimitedHolofoil']['market']
                format_number_standard = "${:,.2f}".format(market_price_standard)
            except KeyError:
                format_number_standard = "-"

        data = (card_no, name, card_type, rarity, format_number_standard)
        table.insert(parent='', index=0, values=data)

    table.insert(parent='', index=ctk.END)

class gymSeries:

    gym_label = ctk.CTkLabel(scrollable_frame, text="Gym Series", font=ctk.CTkFont(size=30, weight="bold"))
    gym_label.pack(pady=10, side=TOP)

    def gymHeroesInfo():
        json_data = filtered_gym_sets

        try:
            r = requests.get(json_data[0]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)


        name = filtered_gym_sets[0]['name']

        gym_button2 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50, command=gymHeroesCards)
        gym_button2.pack(pady=5)

    def gymChallengeInfo():
        json_data = filtered_gym_sets

        try:
            r = requests.get(json_data[1]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_gym_sets[1]['name']

        gym_button2 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50, command=gymChallengeCards)
        gym_button2.pack(pady=5)

    gymHeroesInfo()
    gymChallengeInfo()

class neoSeries:

    neo_label = ctk.CTkLabel(scrollable_frame, text="Neo Series", font=ctk.CTkFont(size=30, weight="bold"))
    neo_label.pack(pady=10, side=TOP)

    def neo1Info():
        json_data = filtered_neo_sets

        try:
            r = requests.get(json_data[0]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)


        name = filtered_neo_sets[0]['name']

        neo_button1 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        neo_button1.pack(pady=5)

    def neo2Info():
        json_data = filtered_neo_sets

        try:
            r = requests.get(json_data[1]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_neo_sets[1]['name']

        neo_button2 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        neo_button2.pack(pady=5)

    def neo3Info():
        json_data = filtered_neo_sets

        try:
            r = requests.get(json_data[2]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_neo_sets[2]['name']

        neo_button3 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        neo_button3.pack(pady=5)

    def neo4Info():
        json_data = filtered_neo_sets

        try:
            r = requests.get(json_data[3]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_neo_sets[3]['name']

        neo_button4 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        neo_button4.pack(pady=5)

    neo1Info()
    neo2Info()
    neo3Info()
    neo4Info()

class legendarySeries:

    legendary_label = ctk.CTkLabel(scrollable_frame, text="Legendary Series", font=ctk.CTkFont(size=30, weight="bold"))
    legendary_label.pack(pady=10, side=TOP)

    def legendaryInfo():
        json_data = filtered_legendary_sets

        try:
            r = requests.get(json_data[1]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image, size=[10,15])


        name = filtered_legendary_sets[1]['name']

        leg_button1 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        leg_button1.pack(pady=5)

    legendaryInfo()

class ecardSeries:

    ecard_label = ctk.CTkLabel(scrollable_frame, text="e-Card Series", font=ctk.CTkFont(size=30, weight="bold"))
    ecard_label.pack(pady=10, side=TOP)

    def ecard1Info():
        json_data = filtered_ecard_sets

        try:
            r = requests.get(json_data[0]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)


        name = filtered_ecard_sets[0]['name']

        ecard_button1 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ecard_button1.pack(pady=5)

    def ecard2Info():
        json_data = filtered_ecard_sets

        try:
            r = requests.get(json_data[1]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ecard_sets[1]['name']

        ecard_button2 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ecard_button2.pack(pady=5)

    def ecard3Info():
        json_data = filtered_ecard_sets

        try:
            r = requests.get(json_data[2]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ecard_sets[2]['name']

        ecard_button3 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ecard_button3.pack(pady=5)

    ecard1Info()
    ecard2Info()
    ecard3Info()

class exSeries:

    ex_label = ctk.CTkLabel(scrollable_frame, text="EX Series", font=ctk.CTkFont(size=30, weight="bold"))
    ex_label.pack(pady=10, side=TOP)

    def ex1Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[0]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)


        name = filtered_ex_sets[0]['name']

        ex_button1 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button1.pack(pady=5)

    def ex2Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[1]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[1]['name']

        ex_button2 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button2.pack(pady=5)

    def ex3Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[2]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[2]['name']

        ex_button3 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button3.pack(pady=5)

    def ex4Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[3]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[3]['name']

        ex_button4 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button4.pack(pady=5)

    def ex5Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[4]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[4]['name']

        ex_button5 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button5.pack(pady=5)

    def ex6Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[7]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[7]['name']

        ex_button6 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button6.pack(pady=5)

    def ex7Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[8]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[8]['name']

        ex_button7 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button7.pack(pady=5)

    def ex8Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[9]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[9]['name']

        ex_button8 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button8.pack(pady=5)

    def ex9Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[10]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[10]['name']

        ex_button9 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button9.pack(pady=5)

    def ex10Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[11]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[11]['name']

        ex_button10 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button10.pack(pady=5)

    def ex11Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[12]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[12]['name']

        ex_button11 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button11.pack(pady=5)

    def ex12Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[13]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[13]['name']

        ex_button12 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button12.pack(pady=5)

    def ex13Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[16]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[16]['name']

        ex_button13 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button13.pack(pady=5)

    def ex14Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[17]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[17]['name']

        ex_button14 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button14.pack(pady=5)

    def ex15Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[18]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[18]['name']

        ex_button15 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button15.pack(pady=5)

    def ex16Info():
        json_data = filtered_ex_sets

        try:
            r = requests.get(json_data[19]['images']['symbol'])

        except requests.exceptions.RequestException as error:
            print(error)
            set.destroy()  # <-- close window
            sys.exit(1)

        fp = io.BytesIO(r.content)  # <-- create file-like object in memory
        image = Image.open(fp)  # <-- use file-like object in memory
        photo = ctk.CTkImage(image)

        name = filtered_ex_sets[19]['name']

        ex_button16 = ctk.CTkButton(scrollable_frame, text=name, fg_color="white", text_color="black", image=photo, width=1200, height=50)
        ex_button16.pack(pady=5)

    ex1Info()
    ex2Info()
    ex3Info()
    ex4Info()
    ex5Info()
    ex6Info()
    ex7Info()
    ex8Info()
    ex9Info()
    ex10Info()
    ex11Info()
    ex12Info()
    ex13Info()
    ex14Info()
    ex15Info()
    ex16Info()


#pprint(filtered_base_sets)

pokemonSets.mainloop()
