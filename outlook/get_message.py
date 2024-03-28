import datetime
import os
import win32com.client


def get_message(item: str):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6).Folders.Item(item)
    messages = inbox.Items
    return messages


def save_attachments(subject: str, path: str,
                     file_ext: str, messages, ) -> None:
    today = datetime.date.today()

    for message in messages:
        x = message.ReceivedTime
        if message.Subject == subject and x.strftime("%Y-%m-%d") == str(today):
            for attachment in message.Attachments:
                if file_ext in str(attachment):
                    print(attachment.FileName)
                    attachment.SaveAsFile(os.path.join(path, str(attachment)))
    return None


save_attachments("ГСМ", r"C:\Users\ivanovko\Desktop\DT2024\GSM_AMT\DT_2024\03_march",
                 ".xls", get_message("ГСМ АМТ"))
