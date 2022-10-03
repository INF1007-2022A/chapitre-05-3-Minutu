#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	number=0
	for i in text:
		if i.isalnum()==True:
			number+=1

	return number

def get_word_length_histogram(text):
	words=[]
	words+= text.split(' ')
	list=[]
	histogramme=[]
	for word in words:
		number_letters=get_num_letters(word)
		list.append(number_letters)
	for i in range(max(list)+1):
		histogramme.append(0)

	for mot in words:
		number_letters=get_num_letters(mot)
		histogramme[number_letters]+=1

	return histogramme

def format_histogram(histogram):
	ROW_CHAR = "*"
	formatted_histogram=''
	del histogram[0]
	number=1

	for i in histogram:
		ROW_CHARS=ROW_CHAR*i
		row= f'{number:>4}'+' '+ f'{ROW_CHARS:}'+'\n'
		formatted_histogram+=row
		number+=1
	return formatted_histogram

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	SPACE=' '
	horizontal_histogram_list=[]
	row_bottom=''
	for i in range((len(histogram)+1)):
		row_bottom+=(LINE_CHAR)
	horizontal_histogram_list.append(row_bottom)
	while max(histogram)!=0:
		n=0
		empty_row=''
		for i in histogram:

			if i ==0:
				n+=1
				empty_row+=(SPACE)
			elif i!=0:
				histogram[n]=histogram[n]-1
				empty_row+=(BLOCK_CHAR)
				n+=1
		horizontal_histogram_list.append(empty_row)
	formatted_horizontal_histogram=''
	for x in range(len(horizontal_histogram_list)):
		formatted_horizontal_histogram= formatted_horizontal_histogram+horizontal_histogram_list[len(horizontal_histogram_list)-1-x]+'\n'
	return formatted_horizontal_histogram


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
