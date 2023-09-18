from bs4 import BeautifulSoup
import  requests
USERNAME = input("Enter username: ")
city, state, country, profession = '', '', '', ''
try:
    url = requests.get('https://www.codechef.com/users/' + USERNAME)
    page_source = BeautifulSoup(url.content,'lxml')
    #print(page_source)
    
# For Username
    uls = page_source.find('ul', class_="side-nav")
    for ul in uls:
        newsoup = BeautifulSoup(str(ul), 'lxml')
        lis = newsoup.find_all('li')
        for li in lis:
            if "Username" in li.text:
                username = (li.text.split("★"))[1]
            '''if "City" in li.text:
                city = li.text.split(':')[1]'''
            if "Country" in li.text:
                country = li.text.split(':')[1]
            '''if "State" in li.text:
                state = li.text.split(':')[1]'''
            if "Student/Professional" in li.text:
                profession = li.text.split(':')[1]
    # Other Content
    try:
        # ratings of the user
        rating = page_source.findAll('div', class_="rating-number")[0].text
        global_rating = page_source.findAll('strong', class_="global-rank")[0].text
        # For Solved Problems count
        problems_count = page_source.findAll('section', class_="problems-solved")
        
        cnt = 0
        fully_practice = 0
        fully_others = 0
        partial_practice = 0
        partial_others = 0
        for i in problems_count:
            cnt = cnt + 1
            newsoup = BeautifulSoup(str(i), 'lxml').find_all('article')
            
            # For Completely Solved
            if(cnt == 1):
                full_para = BeautifulSoup(str(newsoup[0]), 'lxml').find_all('p')
                count = 0
                for j in full_para:
                    if(count==0):
                        fully_practice = len(BeautifulSoup(str(j), 'lxml').find_all('a'))
                    count+=1
                fully_others = (count-1)
                
                # For Partially Solved
                
                if(len(newsoup)==1):{
                    print("Partially solved Problems -0 Practice Problems and 0 Other Problems")
                }
                else:
                    partial_para = BeautifulSoup(str(newsoup[1]), 'lxml').find_all('p')
                    count = 0
                    for j in partial_para :
                        if(count==0):
                            partial_practice = len(BeautifulSoup(str(j), 'lxml').find_all('a'))
                            count+=1
                        partial_others = (count-1)
                
        
        highest_rating = page_source.findAll('small')
        for i in highest_rating:
            if 'Highest Rating' in i.text:
                highest = i.text.split()[2][:-1]
                
        img = page_source.findAll('div', class_='user-details-container')
        for i in img:
            avatar = BeautifulSoup(str(i), 'lxml').find_all('img')[0]['src']
    except Exception as e:
        print("Couldn't get the data->", e)

    print('\nUsername: '+ str(username) + 'Global Rank: ' + global_rating)
    #print('Location: ' + city + ', ' + state)
    print('location:'+country)
    print('Profession/Student: ' + profession)
    print('Highest Rating:' + highest)
    print('Avatar Url:', avatar)
    print("Fully solved Problems - {0} Practice Problems and {1} Other Problems".format(fully_practice,fully_others) )
    print("Partially solved Problems - {0} Practice Problems and {1} Other Problems".format(partial_practice,partial_others) )
    


except Exception as e:
    print("Couldn't parse the url->", e)    
