from instapy import InstaPy
from instapy import smart_run



my_username=''
my_password =''


session = InstaPy(username=my_username,password=my_password,headless_browser=False)



with smart_run(session):
    session.set_relationship_bounds(enabled=true,delimit_by_numbers=True,max_followers=500,min_followers=30,min_following=50)
    session.set_do_follow(true,percentage=100)
