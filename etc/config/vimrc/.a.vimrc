syntax enable
" set viminfo='25,\"50,n~/.viminfo'
set undodir=/Users/wuchenglin/.vimundo/
set hidden
set mouse=v
set history=50
set nobackup

filetype plugin indent on
"set cindent
set tabstop=4
set shiftwidth=4
"set softtabstop=4
set expandtab
set number
set showcmd
set showmatch
set smartcase
set incsearch
set hlsearch
:hi Search ctermbg=7
set autowrite
"set foldmethod=syntax
set fileencoding=UTF-8

let g:mapleader=','
let g:solarized_termcolors=256

:nnoremap <leader>ev :vsplit $MYVIMRC<cr>
:nnoremap <leader>sv :source $MYVIMRC<cr>
:nnoremap <leader>" viw<esc>a"<esc>hbi"<esc>lel
:nnoremap <leader>( viw<esc>a)<esc>hbi(<esc>lel
:nnoremap W w
:nnoremap w W
:nnoremap B b
:nnoremap b B
:vnoremap <leader>' <esc>`>a'<esc>`<i'<esc>`>
:inoremap jk <esc>
" :inoremap <Up> <esc>ka
" :inoremap <Down> <esc>ji
" :inoremap <Right> <esc>li
" :inoremap <Left> <esc>hi
:onoremap p i(
:onoremap r /return<cr>
:onoremap i( :<c-u>normal! f(vi(<cr>

map <Leader> <Plug>(easymotion-prefix)

" :nnoremap <c-s> <esc>:wi<cr>
" :nnoremap <c-q> <esc>:wq<cr>
" :inoremap <c-s> <esc>:wi<cr>
" :inoremap <c-q> <esc>:wq<cr>

source $VIMRUNTIME/vimrc_example.vim

let g:pydiction_location = '~/.vim/bundle/pydiction/complete-dict'

set nobackup
set nowritebackup

