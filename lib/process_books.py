#!/usr/bin/python3

import os
import json
from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter

def read_file(file_name):
  with open(file_name, 'r+', encoding='utf-8') as file:
    file_text = file.read()
  return file_text

def process_books(books):
  sentence_tokenized_books = list()
  #word_tokenized_books = list()
  for book in books:
    sentence_tokenizer = PunktSentenceTokenizer()
    sentence_tokenized_book = sentence_tokenizer.tokenize(book)
    clean_tokenized_sentences = list()
    for sentence in sentence_tokenized_book:
      clean_tokenized_sentence = sentence.replace("\n"," ").replace("-", " ").replace(":"," ").replace('“','').replace('”','').replace("\t"," ")
      clean_tokenized_sentences.append(clean_tokenized_sentence)
    sentence_tokenized_books.append(clean_tokenized_sentences)
    #for sentence in sentence_tokenized_book:
    #  word_tokenized_sentence = [word.lower().strip('.').strip('?').strip('!') for word in sentence.replace(",","").replace("-"," ").replace(":","").split()]
    #  word_tokenized_sentences.append(word_tokenized_sentence)
    #word_tokenized_books.append(word_tokenized_sentences)
  return sentence_tokenized_books

def merge_books(books):
  all_sentences = list()
  for book in books:
    for sentence in book:
      all_sentences.append(sentence)
  return all_sentences

# list of books in dir
book_files = sorted([book_file for book_file in os.listdir() if book_file[-4:] == '.txt'])
print(book_files)

# read in books
books = list()
for book_file in book_files:
  books.append(read_file(book_file))

# process time
processed_books = process_books(books)

# merge books
all_the_sentences = merge_books(processed_books)

# write to file
pwd = os.getcwd()

bookfile = pwd + '/' + 'book_file.py'

with open(bookfile, 'w', encoding='utf-8') as b:
    json.dump(all_the_sentences, b, ensure_ascii=False)
