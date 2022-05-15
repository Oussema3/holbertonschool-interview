#!/usr/bin/python3
"""
    Querie the Reddit API
"""
import itertools
import requests
# Libraries imported in your Python files must be organized in alphabetical
# order

# initiate a result dictionary
result_dict = {}


def sort_dictionary(result_dict):
    """
    sort the dictionary
    """
    sorted_by_values = sorted(result_dict.items(),
                              key=lambda kv: kv[1],
                              reverse=True)

    sorted_dict = []
    for _, v in itertools.groupby(sorted_by_values, lambda item: item[1]):
        sorted_dict.extend(sorted(v))

    return dict(sorted_dict)


def get_reddit(subreddit):
    """
    Make the Request
    """
    try:
        base_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&t='all'"
        request = requests.get(base_url, headers={'User-agent': 'my-app/0.0.1'}, allow_redirects=False)
    except:
        print('An Error Occured')
    return request.json()


def get_post_titles(r):
    '''
    Get a List of post titles
    '''
    posts = []
    for post in r['data']['children']:
        x = post['data']['title']
        posts.append(x)
    return posts


def count_words(subreddit, word_list):
    """
    Method:
        to querie the Reddit API, parse the title of all hot articles,
        and print a sorted count of given keywords (case-insensitive,
        delimited by spaces. Javascript should count as javascript,
        but java should not).
    Parameters:
        subreddit:
        word_list:
    Returns:
        prints a sorted count of given keywords.
        (case-insensitive, delimited by spaces)
    """
    global result_dict
    if len(word_list) == 0:
        for k, v in result_dict.items():
            if v != 0:
                print("{}: {}".format(k, v))
        return
    else:
        # do the work!
        request_api = get_reddit(subreddit)
        titles_list = get_post_titles(request_api)

        # count_python = 0
        # for title in titles_list:
        #     count_python  += title.lower().count("python")
        #     print(count_python)

        # work on the first element of the list
        word_to_count = word_list[0].lower()
        for title in titles_list:
            # save the count result into the dictionary
            # add or append data to the dictionary
            if word_to_count in result_dict:
                prev_count = result_dict[word_to_count]
            else:
                prev_count = 0
            new_count = title.lower().count(word_to_count)
            # print(word_to_count)
            # print(title)
            # print(new_count)
            result_dict[word_to_count] = new_count + prev_count

        result_dict = sort_dictionary(result_dict)
        # print(result_dict)
        # remove the first element from the word_list
        word_list.pop(0)
        # recall the function with new wordlist
        count_words(subreddit, word_list)
