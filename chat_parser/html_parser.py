# -*- coding: utf-8 -*-

from __future__ import absolute_import

from bs4 import BeautifulSoup

from .chat_objects import *


def get_emails_html():
    "returns the html from the emails file"
    html = None
    with open('emails.html', 'r') as emails_file:
        html = emails_file.read()

    return html


def get_h2s_positions(html):
    "return a list of all the index of H2 in the given html"
    import re
    starts = [match.start() for match in re.finditer(re.escape('<h2>'), html)]
    return starts


def get_h3s_positions(html):
    "return a list of all the index of H3 in the given html"
    import re
    starts = [match.start() for match in re.finditer(re.escape('<h3>'), html)]
    return starts


def validate_conversation_group_html(html):
    parsed_html = BeautifulSoup(html)
    h2 = parsed_html.find('h2')
    return 'Bate-papo' in h2.get_text()


def get_conversations_groups_html(html):
    "returns a list of string that represent each conversations group of this html"
    h2s_indexes = get_h2s_positions(html)
    conversations_groups = []

    last_h2_index = h2s_indexes[0]
    for h2_index in h2s_indexes[1:]:
        conversation_group_html = html[last_h2_index:h2_index]
        if(validate_conversation_group_html(conversation_group_html)):
            conversations_groups.append(conversation_group_html)
        last_h2_index = h2_index

    #: add the last one
    conversation_group_html = html[last_h2_index:]
    if(validate_conversation_group_html(conversation_group_html)):
        conversations_groups.append(conversation_group_html)

    return conversations_groups


def get_conversations_html(html):
    "returns a list of string that represent each conversation of this html"
    h3s_indexes = get_h3s_positions(html)
    conversations = []
    last_h3_index = h3s_indexes[0]
    if len(h3s_indexes) > 1:
        for h3_index in h3s_indexes[1:]:
            conversation_html = html[last_h3_index:h3_index]
            conversations.append(conversation_html)
            last_h3_index = h3_index

        #: add the last one
        conversation_html = html[last_h3_index:]
        conversations.append(conversation_html)
    else:
            conversation_html = html[last_h3_index:]
            conversations.append(conversation_html)

    return conversations


def get_messages(conversation_html):
    "return the list of messages in a html"
    parsed_html = BeautifulSoup(conversation_html)
    msgs = []
    span = parsed_html.find('span')
    while span is not None:
        msg, next_span = message_and_next_span_from_html(span)
        msgs.append(msg)
        span = next_span

    return msgs


def message_and_next_span_from_html(span_html):
    "return the Message object for this html and also the next span html"
    author_span = span_html.findNext('span', attrs={'style': 'font-weight:bold'})
    author = author_span.get_text()
    msg = span_html.get_text().replace(author+": ", '')
    return Message(author, msg), author_span.findNext('span')


def get_conversation_date(conversation_html):
    "returns the date of the conversation html"
    parsed_html = BeautifulSoup(conversation_html)
    date = parsed_html.findAll('p')[1].get_text()
    return date


def get_conversation_group(conversations_group_html):
    "returns the conversation group of the given html"
    conversation_list = []
    for conversation_html in get_conversations_html(conversations_group_html):
        msgs = get_messages(conversation_html)
        date = get_conversation_date(conversation_html)
        conversation = Conversation(date, msgs)
        conversation_list.append(conversation)

    conversation_group = ConversationGroup(conversation_list)
    return conversation_group


def perc_done(done, total):
    "the percentage done of all the conversations groups"
    print "%.f" % (done / total * 100), "%"


def parse_html():
    "parse the emails html and return them in python objects"

    html = get_emails_html()

    conversations_groups_html = get_conversations_groups_html(html)

    total = len(conversations_groups_html)
    done = 0.0

    conversations_group_list = []
    for conversations_group_html in conversations_groups_html:
        perc_done(done, total)
        conversations_group_list.append(get_conversation_group(conversations_group_html))
        done = done + 1
    perc_done(done, total)

    return conversations_group_list
