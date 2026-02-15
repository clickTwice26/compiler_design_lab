import sys
findout = {
    "identifiers" : [],
    "keywords" : [],
    "operator" : [],
    "header_files" : []
}   

library = {
    "keywords": {
        "data_type" : ["int", "float", "double"]
    },
    "preprocessors" : ["#"],
    "header_file_extension" : [".h"],
    "delimiter" : [";"],
    "numbers" : []
}
def getParsedLine(text : str, spliter : str = " "):
    print(text)
    parsed_line = ""
    possible_delimiters = ["(", ";"]
    count_till_delimiter = 1
    
    for i in text:
        if i in possible_delimiters:
            delimiter = i
            break
        count_till_delimiter += 1

    counter = 0
    while text[counter] != delimiter:
        parsed_line+= text[counter]

        counter+=1
    parsed_line = parsed_line.split(spliter)
    for i in parsed_line:
        if not (len(i) >1):
            parsed_line.remove(i)

    return {
        "parsed_line" : parsed_line,
        "delimiter" : delimiter,
        "count_till_delimiter" : count_till_delimiter
        
    }
    

def isPreprocessor(line : str, delimiter : str = '>') -> dict:
    #this function will be called after getting 
    # delimiter = \n
    # print(line[0:line.index("\n")])
    #parsed_line = 
    #finding the spliter
    response = {
        "preprocessor_type" : None,
        "header_file_name": None,
        "identifier_name": None,
        "value": None
    }  
    spliter : str = None
    if line.startswith("#define"):
        spliter = " "
        response["preprocessor_type"] = "define"
        line = line.split(" ")
        response["identifier_name"] = line[1]
        response["value"] = line[2]

    if line.startswith("#include"):
        line = line.split("<")
        response["preprocessor_type"] = "include"
        response["header_file_name"] = line[1]
    print(response)
    return response
    # response["preprocessor_key"] = 
    

   # for i in line:
   
    #    if 
text = open("test.c", "r").read();
newline_counter : int = 0
index_counter : int = 0
char_count : int = 0
print(text)
single_word = ""

while char_count < len(text):
    # print(char_count)
    if text[char_count] == "#":
        print("Preprocessor found")
        line_for_parsing = ""
        j = char_count
        while text[j] != '>':
            line_for_parsing+=text[j]
            j+=1
        isPreprocessor(line_for_parsing)
        char_count=j+1
        continue
    if single_word.strip() in ["int", "float", "auto", "break"]:
        print(f"Keyword : {single_word.strip()}")
        single_word = single_word.strip()
        if single_word in library["keywords"]["data_type"]:

            p_line = getParsedLine(text[char_count:], spliter=" ")
            if p_line["delimiter"] == '(':
                print(f"Function : {p_line["parsed_line"]}")
                # print(char_count)
                char_count= char_count + p_line["count_till_delimiter"]
                # print(char_count)
                # print(f"{text[char_count]}")
                # sys.exit(0)
  
                

        single_word = ""

       
    
        continue
    if single_word.lstrip().endswith((" ", "=")):
        print(f"Identifier : {single_word}")
        single_word = ""
        
    # print(f"Line for parsing {single_word} , last char_index {j}")

    if text[char_count] not in [")", "{", "}"]:
        single_word+=text[char_count] 
    # print(f"single word {single_word}, {char_count}")
    
    char_count+=1

# print(text.index("\n"))
# print(newline_counter)
# print(text)
