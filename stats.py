def word_count(file_contents):
	words = file_contents.split()
	return len(words)


def character_count(file_contents):
	lowercase = file_contents.lower()

	chr_count_dict = {}
	for chr in lowercase:
		if chr in chr_count_dict:
			chr_count_dict[chr] += 1
		else:
			chr_count_dict[chr] = 1
	return chr_count_dict

def sort_on(item_tuple):
	return item_tuple[1]

def dict_sort(chr_count_dict):

	items = list(chr_count_dict.items())
	items.sort(reverse=True, key=sort_on)
	sort_list = []
	for item, count in items:
		dict_entry = {"char": item, "num": count}
		sort_list.append(dict_entry)
	
	return(sort_list)

def search_func(file_contents):
	lower = file_contents.lower()
	split = lower.split()
	search_count = 0
	search_term = input("Search for term: ")
	for word in split:
		if word == search_term:
			search_count += 1
	print (f"{search_term} was found {search_count} times")
	
	repeat = input("Search again? [y]/[n]")
	if repeat == "y":
		search_func(file_contents)
	else:
		print ("============= END ===============") 

	

