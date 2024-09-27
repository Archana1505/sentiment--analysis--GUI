import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob

def analyze_sentiment():
    text = text_input.get("1.0", tk.END)
    if text.strip() == "":
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    
    # Perform sentiment analysis
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        result = "Positive"
    elif polarity < 0:
        result = "Negative"
    else:
        result = "Neutral"
    
    # Display result
    result_label.config(text=f"Sentiment: {result} (Polarity: {polarity})")

# Create the main window
root = tk.Tk()
root.title("Sentiment Analysis GUI")
root.geometry("600x400")
root.config(bg="black")

 #heading
h=tk.Label(root,text="SENTIMENT ANALYSIS",bg="black",font=("Areal",20),fg="white")
h.place(x=100,y=20)
# Create text input
text_input = tk.Text(root, height=10, width=50)
text_input.place(x=10,y=100,height=100,width=580)

# Create analyze button
analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment,bg="pink",fg="black")
analyze_button.place(x=200,y=220,height=50)

# Create result label
result_label = tk.Label(root, text="Sentiment: ",bg="pink",fg="black")
result_label.place(x=200,y=280,height=50)

# Run the application
root.mainloop()
