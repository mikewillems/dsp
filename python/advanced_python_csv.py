with open('emails.csv', 'w+') as f:
    for a in emails:
        f.writelines(a+'\n')