from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Aboutus, ContactUs
from django.db.models import Q

def aboutus(request):
    data = Aboutus.objects.last()
    return render(request, 'blogapp/about.html', {'data':data})

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('id_name')
        phone = request.POST.get('id_phone')
        email = request.POST.get('id_email')
        message = request.POST.get('id_message')
        contact = ContactUs.objects.create(name=name, phone=phone, email=email, message=message)
        return redirect(contactus)
    return render(request, 'blogapp/contact.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogapp/index.html'

class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'blogapp/index.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('search_post')
        print(query)
        # post_list = Post.objects.filter(Q(title__icontains=query), Q(status=1))
        post_list = Post.objects.filter(status=1, title__icontains=query)
        for i in post_list:
            print(i.title)
        return post_list

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blogapp/post.html'
