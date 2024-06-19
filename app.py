import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from instabot import Bot

# Function to handle bot actions
def run_bot():
    username = username_entry.get()
    password = password_entry.get()
    target_user = target_user_entry.get()
    action = action_var.get()

    bot = Bot()
    try:
        bot.login(username=username, password=password)
        
        if action == 'follow':
            bot.follow(target_user)
            messagebox.showinfo('Action Completed', f'Followed {target_user} successfully!')
        elif action == 'like':
            bot.like_user(target_user, amount=5)  # Liking 5 posts of the target user
            messagebox.showinfo('Action Completed', f'Liked posts of {target_user} successfully!')
        elif action == 'comment':
            user_id = bot.get_user_id_from_username(target_user)
            user_posts = bot.get_user_medias(user_id, filtration=False)
            if user_posts:
                most_recent_post = user_posts[0]
                bot.comment(most_recent_post, 'Nice post!')
                messagebox.showinfo('Action Completed', f'Commented on {target_user}\'s post successfully!')
            else:
                messagebox.showerror('Error', f'No posts found for user {target_user}')
        elif action == 'unfollow':
            bot.unfollow(target_user)
            messagebox.showinfo('Action Completed', f'Unfollowed {target_user} successfully!')

    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')

    bot.logout()

# Create main application window
root = tk.Tk()
root.title('Instagram Bot')

# Create a frame with ttkbootstrap style
style = ttk.Style()
style.theme_use('clam')  # Choose a Bootstrap theme (e.g., 'clam')
frame = ttk.Frame(root, padding='20')
frame.grid(row=0, column=0, sticky='nsew')

# Widgets
username_label = ttk.Label(frame, text='Instagram Username:')
username_entry = ttk.Entry(frame, width=30)
password_label = ttk.Label(frame, text='Instagram Password:')
password_entry = ttk.Entry(frame, show='*', width=30)
target_user_label = ttk.Label(frame, text='Target Username:')
target_user_entry = ttk.Entry(frame, width=30)
action_label = ttk.Label(frame, text='Action:')
action_var = tk.StringVar()
action_combobox = ttk.Combobox(frame, textvariable=action_var, values=['follow', 'like', 'comment', 'unfollow'], width=27)

submit_button = ttk.Button(frame, text='Run Bot', command=run_bot)

# Layout using grid
username_label.grid(row=0, column=0, sticky='w', pady=5)
username_entry.grid(row=0, column=1, padx=10, pady=5)
password_label.grid(row=1, column=0, sticky='w', pady=5)
password_entry.grid(row=1, column=1, padx=10, pady=5)
target_user_label.grid(row=2, column=0, sticky='w', pady=5)
target_user_entry.grid(row=2, column=1, padx=10, pady=5)
action_label.grid(row=3, column=0, sticky='w', pady=5)
action_combobox.grid(row=3, column=1, padx=10, pady=5)

submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Expandable layout
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(4, weight=1)

# Start the Tkinter main loop
root.mainloop()
