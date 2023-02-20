import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

# global variable to stop the process
stop = False

# function to stop the process
def stop_process():
    global stop
    stop = True

# function to check if a Facebook page is active
def check_facebook_page(page_url):
    try:
        service = Service('chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(page_url)
        active = 'Facebook' in driver.title
        driver.quit()
        return active
    except WebDriverException:
        return False

# function to show results in a table
def show_results_in_table(page_urls):
    global stop
    results_df = pd.DataFrame(columns=['Page URL', 'Active'])
    for page_url in page_urls:
        # check if the process has been stopped
        if stop:
            messagebox.showinfo("Process stopped", "The process was stopped before completing all pages.")
            return
        active = check_facebook_page(page_url)
        results_df = pd.concat([results_df, pd.DataFrame({'Page URL': page_url, 'Active': active}, index=[0])])
    results_df.reset_index(drop=True, inplace=True)
    table_window = tk.Toplevel(root)
    table_window.title('Facebook Pages')
    table_frame = ttk.Frame(table_window)
    table_frame.pack(padx=10, pady=10)
    table = ttk.Treeview(table_frame, columns=('Page URL', 'Active'))
    table.heading('Page URL', text='Page URL')
    table.heading('Active', text='Active')
    table.column('Page URL', width=200)
    table.column('Active', width=100)
    for i, row in results_df.iterrows():
        table.insert('', 'end', values=(row['Page URL'], 'Yes' if row['Active'] else 'No'))
    table.pack()

# function to generate random Facebook page URLs
def generate_page_urls(num_pages):
    # page_urls = []
    # while len(page_urls) < num_pages:
    #     page_id = ''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyz', k=15))
    #     page_url = f'https://www.facebook.com/{page_id}/'
    #     if check_facebook_page(page_url):
    #         page_urls.append(page_url)
    # return page_urls
    
    return [
            'https://www.facebook.com/groups/1702893316597552',
            'https://www.facebook.com/groups/foziamalikdreamland/?ref=group_browse_new',
            'https://www.facebook.com/groups/foziamaliklovesoonvalley/',
            'https://www.facebook.com/groups/shan009/?ref=group_browse_new',
            'https://www.facebook.com/groups/Djsalman786/'
            ]

# function to start the process
def start_process():
    global stop
    stop = False
    num_pages = int(num_pages_entry.get())
    page_urls = generate_page_urls(num_pages)
    show_results_in_table(page_urls)

# create the main window
root = tk.Tk()
root.title('Facebook Page Checker')

# create a label and entry for number of pages to check
num_pages_label = ttk.Label(root, text='Number of pages to check:')
num_pages_label.pack(padx=10, pady=10)
num_pages_entry = ttk.Entry(root)
num_pages_entry.pack(padx=10, pady=10)

# create a start button
start_button = ttk.Button(root, text='Start', command=start_process)
start_button.pack(padx=10, pady=10)

# create a stop button
stop_button = ttk.Button(root, text='Stop', command=stop_process)
stop_button.pack(padx=10, pady=10)

root.mainloop()
