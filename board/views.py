from django.shortcuts import render, redirect, get_object_or_404
from .forms import BoardForm
from .models import Board
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required()
def create_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user  # 로그인한 사용자를 작성자로 저장
            board.save()
            return redirect('board_list')
    else:
        form = BoardForm()
    return render(request, 'board/create_board.html', {'form': form})


def board_list(request):
    boards = Board.objects.all()
    return render(request, 'board/board_list.html', {'boards': boards})


# try except 구문을 이용한 상세보기
# def board_detail(request, board_id):
#     try:
#         board = Board.objects.get(pk=board_id)
#     except Board.DoesNotExist:
#         messages.error(request, '삭제된 글입니다')
#         return redirect('board.html')
#     return render(request, 'board/board_detail.html', {'board': board})


# django에서 제공하는 detailview를 활용함
class BoardDetail(DetailView):
    model = Board
    template_name = 'board/board_detail.html'


@login_required()
def board_edit(request, pk):
    board = Board.objects.get(pk=pk)

    if board.author != request.user:
        messages.error(request, '작성자만 수정이 가능합니다')
        return redirect('board_detail', board_id=board.id)

    else:

        if request.method == "POST":
            board.title = request.POST['title']
            board.content = request.POST['content']
            # board.id = request.POST['id']

            board.save()
            return redirect('board_detail', pk=board.pk)

        else:
            boardform = BoardForm(instance=board)
            return render(request, 'board/board_edit.html', {'boardform': boardform})

# django 내장 함수 UpdateView를 활용한 코드
# @login_required()
# class BoardUpdateView(UpdateView):
#     model = Board
#     form_class = BoardForm
#     template_name = 'board_edit.html'
#
#     def form_vaild(self, form):
#         board = form.save(commit=False)
#         board.id = self.request.user
#         board.(save)
#         return redirect('/board/{}/'.format(board.pk))

# django 내장 함수 FormView를 활용한 코드
# @login_required()
# class BoardEdit(FormView):
#     form_class = BoardForm
#     template_name = 'board_edit.html'
#
#     def get(self, request, pk):
#         board = get_object_or_404(Board, pk=pk)
#         form = self.form_clas(instance=board)
#         context = {'form': form, 'board': board}
#         return render(request, self.template_name, context)
#
#     def board(self, request, pk):
#         board = get_object_or_404(Board, pk=pk)
#         form = self.form_class(request.POST, instance=board)
#         if form.is_vaild():
#             form.save()
#             return redirect('board_detail', pk=board.pk)
#         context = {'form': form, 'board': board}
#         return render(request, self.template_name, context)
