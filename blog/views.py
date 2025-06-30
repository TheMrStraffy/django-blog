from django.shortcuts import render
from django.http import HttpRequest, Http404

from datetime import date

# Create your views here.
posts_list = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Vicio",
        "date": date(2023, 5, 24),
        "title": "Mountain Hiking",
        "excerpt": "there's nothing like the views you get when hiking in the mountains",
        "content": """
            Vitae error sint, recusandae ut obcaecati facilis error ad aliquam. At quisquam cum saepe consectetur earum nesciunt, voluptatum libero cumque, ea esse ipsa, fuga alias deleniti perferendis dolor debitis, architecto consectetur saepe maxime vitae rem perferendis? Eligendi distinctio dolorum reprehenderit ab reiciendis cum sit fuga, deleniti aliquid praesentium amet quasi aperiam doloremque, quo debitis quos, beatae id unde quae perferendis fuga rem nemo dignissimos vitae, ipsam rem ea laborum similique. Impedit consequatur quidem dolorum numquam magnam et?
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Carmelo",
        "date": date(2021, 5, 24),
        "title": "Into The Woods",
        "excerpt": "these woods are incrediboool!",
        "content": """
            Vitae error sint, recusandae ut obcaecati facilis error ad aliquam. At quisquam cum saepe consectetur earum nesciunt, voluptatum libero cumque, ea esse ipsa, fuga alias deleniti perferendis dolor debitis, architecto consectetur saepe maxime vitae rem perferendis? Eligendi distinctio dolorum reprehenderit ab reiciendis cum sit fuga, deleniti aliquid praesentium amet quasi aperiam doloremque, quo debitis quos, beatae id unde quae perferendis fuga rem nemo dignissimos vitae, ipsam rem ea laborum similique. Impedit consequatur quidem dolorum numquam magnam et?
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "John",
        "date": date(2022, 5, 24),
        "title": "Programming Is Fun",
        "excerpt": "Such smart, so fun, real coding, such brain power.",
        "content": """Vitae error sint, 
        recusandae ut obcaecati facilis error ad aliquam.
          At quisquam cum saepe consectetur earum nesciunt, 
          voluptatum libero cumque, ea esse ipsa, fuga alias deleniti perferendis dolor debitis, architecto consectetur saepe maxime vitae rem perferendis? Eligendi distinctio dolorum reprehenderit ab reiciendis cum sit fuga, deleniti aliquid praesentium amet quasi aperiam doloremque, quo debitis quos, beatae id unde quae perferendis fuga rem nemo dignissimos vitae, ipsam rem ea laborum similique. Impedit consequatur quidem dolorum numquam magnam et?
        """
    }
]


def index(request: HttpRequest):
    sorted_posts = sorted(
        posts_list, key=lambda post: post['date'], reverse=True)

    # takes two from the start of the list
    # if it was `[-2:]` then it would take the last 2 from the list
    latest_posts = sorted_posts[:3]

    context = {
        'posts': latest_posts
    }

    return render(request, 'blog/index.html', context)


def posts(request: HttpRequest):

    context = {
        'posts': posts_list,
    }

    return render(request, 'blog/all-posts.html', context)


def post(request: HttpRequest, slug: str):
    post = None
    try:
        post = next(post for post in posts_list if post['slug'] == slug)

        context = {
            'post': post
        }
        return render(request, 'blog/post-detail.html', context)
    except:
        raise Http404()
