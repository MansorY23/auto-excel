import datetime
import os
import win32com.client
from pathlib import Path
from typing import Union
import logging


def get_message(item: str):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6).Folders.Item(item)
    messages = inbox.Items
    return messages


def save_attachments(subject: str,
                     path: Union[str, Path],
                     file_ext: str, item) -> Path:
    today = datetime.date.today()
    messages = get_message(item)

    for message in messages:
        x = message.ReceivedTime
        if message.Subject == subject and x.strftime("%Y-%m-%d") == str(today):
            for attachment in message.Attachments:
                if file_ext in str(attachment):
                    attachment.SaveAsFile(path)
                    logging.info(f"excel успешно сохранён в директории:\n {path}")

    return Path(path)
