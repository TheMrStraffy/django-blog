from django.shortcuts import render
from django.http import HttpRequest, Http404

from datetime import date

# Create your views here.
posts_list = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Carmelo",
        "date": date(2023, 5, 24),
        "title": "Mountain Hiking",
        "excerpt": "there's nothing like the views you get when hiking in the mountains",
        "content": """
            Vitae error sint, recusandae ut obcaecati facilis error ad aliquam. At quisquam cum saepe consectetur earum nesciunt, voluptatum libero cumque, ea esse ipsa, fuga alias deleniti perferendis dolor debitis, architecto consectetur saepe maxime vitae rem perferendis? Eligendi distinctio dolorum reprehenderit ab reiciendis cum sit fuga, deleniti aliquid praesentium amet quasi aperiam doloremque, quo debitis quos, beatae id unde quae perferendis fuga rem nemo dignissimos vitae, ipsam rem ea laborum similique. Impedit consequatur quidem dolorum numquam magnam et?
        """
    }
]


def index(request: HttpRequest):
    return render(request, 'blog/index.html')


def posts(request: HttpRequest):
    context = None
    return render(request, 'blog/all-posts.html', context)


def post(request: HttpRequest, slug: str):
    data_response = None
    return render(request, 'blog/post-detail.html')
    # try:
    #     data_response = posts_lists[post]
    #     print(post)
    #     print(data_response)

    #     context = {
    #         'post': data_response
    #     }
    #     return render(request, 'blog/includes/post.html', context)
    # except:
    #     raise Http404()
