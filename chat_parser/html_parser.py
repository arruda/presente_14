# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup


def get_emails_html():
    "returns the html from the emails file"
    html = None
    with open('emails.html', 'r') as emails_file:
        html = emails_file.read()

    return html


def parse_html():
    "parse the emails html and return them in python objects"

    pased_html = BeautifulSoup(get_emails_html())

    print parsed_html.body.find('div', attrs={'class':'container'}).text
