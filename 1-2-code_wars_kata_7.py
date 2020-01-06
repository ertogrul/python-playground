#s = "10+4+57"
#ev = eval(s)
#print (ev)

url = ""


def remove_url_anchor(url):
    result_url =""
    # print(url)
    
    if (url[7] == '/'):
        # print('https case')  
        url = url.replace('https://', '')   
    elif (url[7] == 'w'):
        # print('http case')
        url = url.replace('http://', '')  

    for i in url:
        # print (i)
        if (i == 'h'):
            print (url[7])
            print (url[8])
        #if (i == '#' or i == "?" or i == "/"):
        if (i == '#'):
            break
        else:
            result_url = result_url + i
            # print(result_url)
    return result_url

# print (remove_url_anchor('http://www.codewars.com#about'))
print (remove_url_anchor('www.codewars.com#about'))

# remove_url_anchor('www.codewars.com?page=1')