from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from .models import Post,Comment, PostLike
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.template.loader import render_to_string
from django.http import JsonResponse
from profileapp.models import Friend

class PostList(LoginRequiredMixin,FormMixin,ListView):
    model=Post
    form_class=CommentForm
    template_name = 'signup/loginhome.html'
    ordering = ['-Published_date']

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        a_list = list(PostLike.objects.filter(likeuser=self.request.user).values('postlike_id'))
        b_list = []
        for j in a_list:
            b_list.append(j['postlike_id'])
        print(b_list)
        context['like_data'] = b_list
        fr_list = list(Friend.objects.filter(frienduser1=self.request.user).filter(friendstatus=False).filter(is_request_sent=False).values('frienduser2_id'))
        frgt_list = []
        for k in fr_list:
            frgt_list.append(k['frienduser2_id'])
        context['frgt_data'] = len(frgt_list)
        return context

class PostCreate(LoginRequiredMixin,CreateView):
    model=Post
    fields = ['Title',
              'Description',
              'Upload_Image',
              'Upload_Video',
              'Upoad_file'
    ]

    def form_valid(self,form):
        form.instance.postuser = self.request.user
        return super().form_valid(form)

class PostDetail(LoginRequiredMixin,FormMixin,DetailView):
    model=Post
    form_class=CommentForm

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        a_list = list(PostLike.objects.filter(likeuser=self.request.user).values('postlike_id'))
        b_list = []
        for j in a_list:
            b_list.append(j['postlike_id'])
        context['like_data'] = b_list
        return context

class PostUpdate(LoginRequiredMixin,UpdateView):
    model=Post
    fields = ['Title',
              'Description',
              'Upload_Image',
              'Upload_Video',
              'Upoad_file'
    ]

class PostDelete(LoginRequiredMixin,DeleteView):
    model=Post
    success_url = "/login/"


class MyPostList(LoginRequiredMixin,FormMixin,ListView):
    template_name = 'blog/mypost_list.html'
    form_class=CommentForm
    ordering = ['-Published_date']

    def get_queryset(self):
        return Post.objects.filter(postuser=self.request.user).order_by('-Published_date')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        a_list = list(PostLike.objects.filter(likeuser=self.request.user).values('postlike_id'))
        b_list = []
        for j in a_list:
            b_list.append(j['postlike_id'])
        context['like_data'] = b_list
        return context


@login_required
# def PostComment(request,pk):
#     if request.method == 'POST':
#         form = CommentForm(request.POST,request.FILES)
#         if form.is_valid():
#             f = form.save(commit=False)
#             f.commentuser = request.user
#             f.post_id = pk
#             f.save()
#     return redirect('signinhome')

def PostComment(request,pk):
    if request.is_ajax():
        comment = request.POST['comment']
        a = Comment(commentuser=request.user, post_id=pk, Comment=comment)
        a.save()

        count = Post.objects.get(pk=pk)
        context = {'i':count}
        html = render_to_string('blog/comment_section.html', context, request=request)
        return JsonResponse({'form':html})
    else:
        return redirect('signinhome')


@login_required
# def CommentDelete(request,pk):
#     a = Comment.objects.get(pk=pk)
#     a.delete()
#     return redirect('signinhome')

def CommentDelete(request,pk):
    b = Comment.objects.get(pk=pk)
    a = Comment.objects.get(pk=pk)
    a.delete()

    count = Post.objects.get(pk=b.post_id)

    context = {'i':count}
    if request.is_ajax():
        html = render_to_string('blog/comment_section.html', context, request=request)
        return JsonResponse({'form':html})
    else:
        return redirect('signinhome')


@login_required
def PostLikes(request,pk):
    count = PostLike.objects.filter(likeuser=request.user).filter(postlike_id=pk).count()
    if count == 0:
        a = PostLike(likeuser=request.user, postlike_id=pk)
        a.save()
    else:
        a = PostLike.objects.filter(likeuser=request.user).filter(postlike_id=pk)
        a.delete()

    a_list = list(PostLike.objects.filter(likeuser=request.user).values('postlike_id'))
    b_list = []
    for j in a_list:
        b_list.append(j['postlike_id'])
    print('11111111111111111111111111111111111111111111')
    print(b_list)

    count = Post.objects.get(pk=pk)

    context = {'i':count,'like_data':b_list}
    if request.is_ajax():
        html = render_to_string('blog/like_section.html', context, request=request)
        return JsonResponse({'form':html})
    else:
        return redirect('signinhome')

@login_required
def PostLikesDetail(request,pk):
    count = PostLike.objects.filter(likeuser=request.user).filter(postlike_id=pk).count()
    if count == 0:
        a = PostLike(likeuser=request.user, postlike_id=pk)
        a.save()
    else:
        a = PostLike.objects.filter(likeuser=request.user).filter(postlike_id=pk)
        a.delete()

    a_list = list(PostLike.objects.filter(likeuser=request.user).values('postlike_id'))
    b_list = []
    for j in a_list:
        b_list.append(j['postlike_id'])
    print('11111111111111111111111111111111111111111111')
    print(b_list)

    count = Post.objects.get(pk=pk)

    context = {'object':count,'like_data':b_list}
    if request.is_ajax():
        html = render_to_string('blog/like_section_detail.html', context, request=request)
        return JsonResponse({'form':html})
    else:
        return redirect('signinhome')
